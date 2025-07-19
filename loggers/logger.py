import logging

def get_logger(__name__:str, log_path:str, levelname= "INFO" )->logging.Logger:
    logger = logging.getLogger(__name__)

    console_log = logging.StreamHandler()
    file_log = logging.FileHandler(log_path , mode='a', encoding="utf-8")

    if not logger.hasHandlers():
        logger.addHandler(console_log)
        logger.addHandler(file_log)
    
    formatter = logging.Formatter("{asctime} - {levelname} - {name} - {message}", style="{" , datefmt="%Y-%m-%d %H:%M")

    console_log.setFormatter(formatter)
    file_log.setFormatter(formatter)
    logger.setLevel(levelname)

    return logger