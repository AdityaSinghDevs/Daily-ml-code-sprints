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


def setup_logger(name:str, log_path:None, levelname = "INFO")-> logging.Logger:
    '''
    This function/method represents the proper flow of writing a logger 
    1.logger obj
    2.set levels
    3.check for duplicacy
    4.form handlers
    5.form formatters
    6.add formatter to handlers
    7.add handlers
    8.return logger outside duplicacy check
    
    Args:
        name (str) : Takes the name of logger, usage of __name__ preferred
        log_path (str) : Takes the file path and name for logging if storing logs in a file is needed
        levelname (str)<optional> : Takes in logger level [DEBUG, INFO, WARNING, ERROR, CRITICAL], Set to INFO by default

    Returns:
        logger: Configured logging instance.
    '''

    logger = logging.getLogger(name)

    if not logger.hasHandlers():

        level = getattr(logging, levelname.upper(), logging.INFO)
        logger.setLevel(level)

        console_handler = logging.StreamHandler()
        file_handler  = logging.FileHandler(log_path , mode="a", encoding="utf-8")

        formatter = logging.Formatter("{asctime} - {levelname} - {name} : {message}" , style="{" , datefmt="%Y-%m-%d %H:%M")

        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger