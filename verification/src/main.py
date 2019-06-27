import os
import sentry_sdk

if os.getenv('EMPIRE_SENTRY_DSN'):
    sentry_sdk.init(
        dsn=os.getenv('EMPIRE_SENTRY_DSN')
    )

import logging
import signal
import sys

from tornado.ioloop import IOLoop
from referee import Referee

from logs import init_logging



if __name__ == "__main__":
    host = sys.argv[1]
    port = int(sys.argv[2])
    user_connection_id = sys.argv[3]
    docker_id = sys.argv[4]
    try:
        log_level = int(sys.argv[5])
    except IndexError:
        init_logging(logging.INFO)
    else:
        init_logging(log_level, config={
            'root': {
                'handlers': ['console'],
            }
        })

    logger = logging.getLogger()
    logger.info("START Host:{} PORT:{} CONNECTION_ID:{} DOCKER_ID:{}".format(
        host, port, user_connection_id, docker_id))

    def handle_signal(sig, frame):
        IOLoop.instance().add_callback(IOLoop.instance().stop)
    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    io_loop = IOLoop.instance()

    referee = Referee(host, port, user_connection_id=user_connection_id, docker_id=docker_id,
                      io_loop=io_loop)
    referee.start()
    io_loop.start()
