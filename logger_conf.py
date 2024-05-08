import logging

logger = logging.getLogger(__name__)
handler = logging.FileHandler('logs.log')
format = logging.Formatter("%(asctime)s -%(name)s - %(levelname)s - %(message)s")

logger.setLevel(10)
handler.setFormatter(format)
logger.addHandler(handler)