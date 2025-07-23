import logging 

def data_loader_logger():
    logger = logging.getLogger("data_loader")

    if not logger.hasHandlers():
        data_loader  = logging.FileHandler("data.log" , mode = 'a' , encoding='utf-8')
        logger.setLevel("DEBUG")
        format = logging.Formatter("{asctime} - {name} - {levelname} : {message}", style="{", datefmt="%Y-%m-%d %H:%M" )

        data_loader.setFormatter(format)

        logger.addHandler(data_loader)

    return logger




