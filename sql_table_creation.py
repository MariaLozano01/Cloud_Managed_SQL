import dbm
import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

from dotenv import load_dotenv
import os
load_dotenv()
MYSQL_HOSTNAME = os.getenv("MYSQL_HOSTNAME")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:3306/{MYSQL_DATABASE}'
engine = create_engine(connection_string)

MYSQL_DATABASE 

table_patients = """
create table if not exists patients (
    id int auto_increment,
    mrn varchar(255) default null unique,
    first_name varchar(255) default null,
    last_name varchar(255) default null,
    zip_code varchar(255) default null,
    dob varchar(255) default null,
    gender varchar(255) default null,
    contact_mobile varchar(255) default null,
    contact_home varchar(255) default null,
    PRIMARY KEY (id) 
); 
"""

table_medications = """
create table if not exists medications (
    id int auto_increment,
    mrn varchar(255) default null,
    med_ndc varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES patients(mrn) ON DELETE CASCADE);  
    """

table_treatment_process = """
create table if not exists treatment_process(
    id int auto_increment,
    mrn varchar(255) default null unique,
    treatment_name varchar(255) default null,
    treatment_type varchar(255) default null,
    PRIMARY KEY (id) 
); 
"""
table_patient_conditions = """
create table if not exists patient_conditions (
    id int auto_increment,
    mrn varchar(255) default null,
    icd10_code varchar(255) default null,
    icd10_descriptions varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES patients(mrn) ON DELETE CASCADE ); """

table_social_determinants = """
create table if not exists social_determinants(
    id int auto_increment,
    LOINC_NUM varchar(255) default null,
    COMPONENT varchar(255) default null,
    PRIMARY KEY (id)
);
"""
engine.execute(table_patients)
engine.execute(table_medications)
engine.execute(table_treatment_process)
engine.execute(table_patient_conditions)
engine.execute(table_social_determinants)

gcp_tables = engine.table_names()

#-----------------------ON GCP Terminal------------------------------------------
#sudo apt-get update
#sudo apt install mysql-client mysql-server
#sudo mysql 
#mysql -u USERNAME -h HOST NUMBER -p 
#mysql --host HOST NUMBER --user= root 
    #mysql --host HOST NUMBER --user=root --password

