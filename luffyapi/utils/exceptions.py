from rest_framework.views import exception_handler
from django.db import DatabaseError
from rest_framework.response import Response
from rest_framework import status
#自定义处理函数 新增关于数据库的错误等等 保存到log

import logging
logger = logging.getLogger('django')

def custom_exception_handler(exc, context):
    '''
    自定义异常处理
    
    :param exc: 本次请求发送的异常信息
    :param context: 请求的上下文信息[ request/response , time, 行号等等]

    '''
    response = exception_handler(exc, context)
    if response is not None:
        # 来到这里 : 1. 没出错, 2. 出错了但是django不会处理
        view = context['view'] 
        if isinstance(exc,DatabaseError):
            logger.error('[%s]: %s' % (view, exc)) # 记录到日志文件
            response = Response({'error_message': 'Internal server error'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)

        if isinstance(exc,ZeroDivisionError):
            logger.error('[%s]: %s' % (view, exc)) # 记录到日志文件
            response = Response({'error_message': 'ZeroDivisionError'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
            
    return response 
