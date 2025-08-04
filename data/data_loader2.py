import os 
from typing import Optional, List
import pandas as pd
from logger_data import data_loader_logger

default_logger = data_loader_logger()

def data_loader(file_path:str, req_col: Optional[List[str]] = None , drop_na : bool = True, logger = None) -> pd.DataFrame:

    logger  = logger or default_logger

    if not os.path.exists(file_path):
        logger.error(f"File does not exist : {file_path}")
        raise FileNotFoundError(f"No such file : {file_path} ")
    
    logger.info(f" File found : {file_path}")

    extension = os.path.splitext(file_path)[1].lower()
    if extension == ".csv":
        df= pd.read_csv(file_path)
        logger.info(f"CSV file found : {file_path}")
    elif extension == ".xlsx":
        df= pd.read_excel(file_path)
        logger.info(f"Excel file found : {file_path}")
    else:
        logger.error(f"Unsupported file format : {extension}")
        raise ValueError(f"Unsupported file format : {extension}")
    
    if req_col is not None : 
        missing = set(req_col) - set(df.columns)
        if missing:
            raise ValueError(f"Missing required columns : {missing}")
    
    if drop_na:
        if req_col:
            df = df.dropna(subset = req_col)
            
        else:
            df = df.dropna()    

    if df.empty:
        logger.warning("The dataframe is empty")
    
    num_duplicates = df.duplicated().sum()

    if num_duplicates > 0 :
        logger.info(f"Found {num_duplicates} duplicate rows.")

    return df 

'''
data_loader.py was initially written based on core logic from scratch. Around 40–45% of improvements were made with the help of LLM tools to refine edge cases, improve error handling, typing, and return logic. I intentionally started with a raw version to evaluate what I could write independently, then used tooling to strengthen robustness for production-readiness.
'''