import psycopg2
import pandas as pd
import os
import sqlalchemy

DATABASE_URL = os.environ['DATABASE_URL']

city_sfr_csv = os.path.join("Resources", "City_Zhvi_SingleFamilyResidence(main)CLEAN.csv")

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

city_sfr_df = pd.read_csv(city_sfr_csv)
city_sfr_df.head()

city_sfr_df.to_sql('city_sfr.sqlite', conn, if_exists = 'replace')
pd.read_sql('city_sfr.sql').head()
