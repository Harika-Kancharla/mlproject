# nrmlga krish vedio lo ayite ila pedte  from src.mlproject.logger import logging em error rale but naku error vastundi , so kinda teminal lo execture ila cheyyali: 
# You must tell Python to treat src/ as root. so terminal lo $env:PYTHONPATH="src"; python app.py
from mlproject.logger import logging
from mlproject.exception import CustomException
from mlproject.components.data_ingestion import DataIngestion
from mlproject.components.data_ingestion import DataIngestionConfig

import sys

if __name__=="__main__":
    logging.info("The execution has started ")

    try:
        #a=1/0
        
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
        



