from logging import basicConfig
from logging import getLogger

__all__ = ["init", "logger"]

logger = getLogger(__name__)


def init(name, level):
    basicConfig(level=level)
    logger.name = name
