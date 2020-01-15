# -*- coding: UTF-8 -*-
from enum import Enum

from flask import jsonify


class STATUS(Enum):
    ERROR = {"code": -1, "msg": "error"}
    SUCCESS = {"code": 0, "msg": "success"}
    INVALID_PARAMS = {"code": 1001, "msg": "invalid parameter"}
    METHOD_NOT_ALLOWED = {"code": 1002, "msg": "method not allowed"}
    NOT_FOUND = {"code": 1003, 'msg': 'not found source'}


def custom_response(status, data=None, msg=None, code=200):
    if isinstance(status, Enum):
        status = status.value
    _msg = msg if msg else status['msg']
    return jsonify({
        'code': status['code'],
        'msg': _msg,
        'data': data
    })
