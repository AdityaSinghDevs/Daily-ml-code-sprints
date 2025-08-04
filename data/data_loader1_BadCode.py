import os 
import pandas as pd
from data.logger_data import data_loader_logger

def data_loader(file_path : str , req_col : None , drop_na = True):

    #FIXES:
    #req_col : str, is invalid typng, interpreted as default value, it shud be a list or None , therefore req_col : Optional[List[str]] = None, 
    #drop_na = True, is fine, but shud be explicitly stated , hence drop_na : bool = True

    logger = data_loader_logger() #FIX : Logger needs to be globally declared , set it for injection as well for testing 

    if os.path.exists(file_path):
        logger.info("File exists") #FIxes : Use proper exception

        name, extension = os.path.splitext(file_path)

        #FIXES : use indexing with lowercase and propper logging, rest alr, 
        if extension == ".csv" : 
            df  = pd.read_csv(file_path)
            
        elif extension == ".xlsx":
            df  = pd.read_excel(file_path)
        else:
            logger.debug("Unsuporrted Format")

        
        if req_col is not None: #This alright
            missing  = set(req_col) - set(df.columns)
            if missing:
                raise ValueError(f"missing required columns : {missing}")
            
        if drop_na is True: #fix this using proper condition
           df = df.dropna(subset = req_col)

        if df.empty == True : #dont compare with true for no reason 
            logger.warning("The dataframe is empty")

        if df.duplicated() == True : #df.duplicated returns series not boolean
            logger.debug("duplicate data")

        df.to_csv(f"output.csv") # A loader should not write it should just load and return 

   

#THIS MIGHT BE THE SHITTIEST CODE I HAVE WRITTEN IN A WHILE, NEED TO WORK A LOT ON FLOWS    
       


    else:
        logger.error("FILE DOESN''T EXIST")

    
    return None  



