import logging

import logmatic


def define_logger(log_component='no name'):
    """ Define a  logger with 3 default levels
    :param log_component: name of the component which generates the log
    :return: logger object
    """
    logger = logging.getLogger(log_component)

    handler = logging.StreamHandler()
    handler.setFormatter(logmatic.JsonFormatter())

    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.setLevel(logging.DEBUG)

    return logger
