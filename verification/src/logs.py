import logging.config
import os
import sys
from itertools import chain


class StreamSplitHandler(logging.Handler):

    FMT = '%(name)s:%(levelname)s %(message)s  FILE: %(pathname)s:%(lineno)s'

    def __init__(self):
        logger_fmt = logging.Formatter(fmt=self.FMT, datefmt='%H:%M:%s')
        self.stderr_handler = logging.StreamHandler(sys.stderr)
        self.stderr_handler.setFormatter(logger_fmt)
        self.stdout_handler = logging.StreamHandler(sys.stdout)
        self.stdout_handler.setFormatter(logger_fmt)
        logging.Handler.__init__(self)

    def emit(self, record):
        if record.levelno < logging.WARNING:
            self.stdout_handler.emit(record)
        else:
            self.stderr_handler.emit(record)


def init_logging(log_level, config=None):
    config = config or {}

    config_template = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'console': {
                '()': 'coloredlogs.ColoredStreamHandler',
                'show_hostname': False,
            },
            'std_split': {
                '()': StreamSplitHandler,
            },
            # 'sentry': {
            #     'level': 'ERROR',
            #     'class': 'raven.handlers.logging.SentryHandler',
            #     'dsn': os.getenv('SENTRY_DSN'),
            # },
        },
        'loggers': {
        },
        'root': {
            'handlers': ['std_split', 'sentry'],
        },
    }

    for key, value in config.items():
        try:
            config_template[key].update(value)
        except KeyError:
            config_template[key] = value

    # Set the level and handlers for all loggers.
    loggers = config_template['loggers'].values()
    if 'root' in config_template:
        loggers = chain(loggers, [config_template['root']])
    for logger in loggers:
        if 'handlers' not in logger:
            logger['handlers'] = ['console']
        if 'level' not in logger:
            logger['level'] = log_level
        if 'propagate' not in logger:
            logger['propagate'] = False

    logging.config.dictConfig(config_template)
