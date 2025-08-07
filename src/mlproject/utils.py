#mysql nunchi deniki connection kavaliga adi ikkada chestam 

#utils anedi oka generic functionality kosam like data base nunchi data ni read cheyyadam kosam ala
import os
import sys
from mlproject.exception import CustomException
from mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv() # Load values from .env file

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    logging.info("Reading SQL database started ")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db

        )
        logging.info(f"Connection Established: {mydb}")
        df=pd.read_sql_query('Select * from student', mydb)
        print(df.head())
        return df
        
    except Exception as ex:
        raise




