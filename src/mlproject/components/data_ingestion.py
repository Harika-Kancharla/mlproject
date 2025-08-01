# Database ---> data --->train test split
# data base edaina avvacchu like MySQL or MongoDB , based on situation, depends on data pipelines which are made by data engineers
# Finally output of data ingestion step is having data in form train test split format
#stud.csv(ekkada uncho vacchindi) undiga nrmlga big data engineers pipeline vadi database lo pedtaru but manam manual ga data base lo pedtam

# MySQL --> Train test split --?dataset

import os
import sys
from mlproject.exception import CustomException
from mlproject.logger import logging
import pandas as pd
from mlproject.utils import read_sql_data
from sklearn.model_selection import train_test_split

# dataclass valla input parameters anni easy and fast ga iccheygalam
from dataclasses import dataclass

#parameters predefine cheskocchu kabatti data class vademu
@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            ##reading the data from mysql
            df=read_sql_data()
            logging.info("Reading completed from mysql database")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True) 
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Data Ingestion is Completd")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
