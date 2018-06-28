import psycopg2
import pandas as pd
import os
from sqlalchemy import create_engine

host = "localhost"
user = "tcbrekke"
database = "project2scratch"

DATABASE_URL = os.environ['DATABASE_URL']

city_sfr_csv = os.path.join("Resources", "City_Zhvi_SingleFamilyResidence(main)CLEAN.csv")

engine = create_engine(DATABASE_URL)

city_sfr_df = pd.read_csv(city_sfr_csv)

city_sfr_df.to_sql('city_sfr', engine, if_exists = 'replace')
pd.read_sql('city_sfr', engine)
print(engine.table_names())
