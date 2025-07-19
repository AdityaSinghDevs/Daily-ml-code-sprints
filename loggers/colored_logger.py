import logging
import logging.handlers
from colorlog import ColoredFormatter


def setup_logger(name:str, filename = None , loglevel = "INFO"):

    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        console_handler = logging.StreamHandler()

        level = getattr(logging , loglevel.upper() , logging.INFO)
        logger.setLevel(level)

        color_formatter = ColoredFormatter(
            "{log_color}{asctime} -{levelname} - {name} : {message}", style ="{"
            ,datefmt = "%Y-%m-%d %H:%M",
            log_colors={
                'DEBUG' : 'cyan',
                'INFO' : 'green',
                'WARNING' : 'yellow',
                'ERROR': 'red',
                'CRITICAL' : 'bold_red',
            },
            reset=True
        )
        file_formatter = logging.Formatter("{asctime} - {levelname} - {name} : {message}", style ="{"
            ,datefmt = "%Y-%m-%d %H:%M",)
        console_handler.setFormatter(color_formatter)

        if filename:
            file_handler = logging.handlers.RotatingFileHandler(
            filename,
            maxBytes = 5*1024*1024, #5MB
            backupCount=3,
            encoding = "utf-8",
         )
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        

    return logger


