import logging

logger = logging.getLogger(__name__)


def setup_logging():
    """
    Инициализация одного общего логгера
    """
    logging.basicConfig(level=logging.INFO)
