import psycopg2
import pandas as pd
import os
from sqlalchemy import create_engine
# DATABASE_URL = os.environ['DATABASE_URL']

host = "localhost"
user = "tcbrekke"
database = "project2scratch"

DATABASE_URL = f"postgresql://tcbrekke:password@localhost/project2scratch"

city_sfr_csv = os.path.join("Resources", "City_Zhvi_SingleFamilyResidence(main)CLEAN.csv")

engine = create_engine(DATABASE_URL)

city_sfr_df = pd.read_csv(city_sfr_csv)
city_sfr_df.head()

city_sfr_df.to_sql('city_sfr', engine, if_exists = 'replace')
pd.read_sql('city_sfr', engine).head()
print(engine.table_names())
