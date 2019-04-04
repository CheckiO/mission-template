from .base import BaseHandler
import sys


class SimplePrintHandler(BaseHandler):
    def handler_pre_test(self, data, request_id, stream_r):
        super().handler_pre_test(data, request_id, stream_r)
        print('\n'+'-'*20)
        print('TEST: {}'.format(data['representation']))

    def handler_result(self, data, request_id, stream_r):
        super().handler_result(data, request_id, stream_r)
        print('\n'+'-'*20)
        if data['success']:
            print('RESULT:SUCCESS')
        else:
            print('RESULT:INCOMPLETE')
        sys.exit(0)


    def handler_stdout(self, line, request_id, stream_r):
        print(line, end='')

    def handler_stderr(self, line, request_id, stream_r):
        print(line, end='')
