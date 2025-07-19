from colored_logger import setup_logger

logger = setup_logger("training" , "logs.log")

logger.info("helpp")
logger.warning("helpp")
logger.error("helpp")
logger.critical("helpp")