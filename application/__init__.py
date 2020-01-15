# -*- coding: UTF-8 -*-
import glob
import importlib
import logging
import sys
import time
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from application.config import config_map
from application.utils.logger import JSONFormatter

# db
db = SQLAlchemy()

# logger
formatter = JSONFormatter()
json_handler = logging.StreamHandler(sys.stdout)
json_handler.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)


def load_blueprint(app, path):
    for file_path in glob.glob(path, recursive=True):
        module_name = file_path.split(".")[0].replace("/", ".")
        print('name ', module_name)
        try:
            module = importlib.import_module(module_name)

            if "__init__" in file_path:
                continue

            if hasattr(module, "_DO_NOT_LOAD_BP"):
                logger.warning("ignore module %s because of attribute _DO_NOT_LOAD_BP settled", module_name)
                continue

            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, Blueprint):
                    logging.info("register %s to flask", attr_name)
                    app.register_blueprint(attr)
        except AttributeError:
            logging.error("failed to load module %s", module_name)


def create_app(env='development'):
    """程序工厂函数"""
    app = Flask(__name__)
    app.uptime = time.time()

    # 加载配置文件
    app.config.from_object(config_map[env])

    # 初始化插件
    db.init_app(app)

    # 加载蓝图模块
    load_blueprint(app, 'application/api/**/*.py')
    logger.info("application started on %s, found %s api", env, len(list(app.url_map.iter_rules())) - 1)
    return app
