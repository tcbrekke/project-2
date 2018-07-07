import psycopg2
import pandas as pd
import os
from sqlalchemy import create_engine

#Set DATABASE_URL to the database URL served by Heroku Postgres
DATABASE_URL = os.environ['DATABASE_URL']

region_affordability_csv = os.path.join("Resources", "Affordability_Wide_2018Q1_PublicCLEAN.csv")
city_single_family_csv = os.path.join("Resources", "City_Zhvi_SingleFamilyResidence(main)CLEAN.csv")
county_single_family_csv = os.path.join("Resources", "County_Zhvi_SingleFamilyResidenceCLEAN.csv")
county_multi_family_csv = os.path.join("Resources", "County_Zri_AllHomesPlusMultifamilyCLEAN.csv")

engine = create_engine(DATABASE_URL)
connection = engine.connect()

region_affordability_df = pd.read_csv(region_affordability_csv)
city_single_family_df = pd.read_csv(city_single_family_csv)
county_single_family_df = pd.read_csv(county_single_family_csv)
county_multi_family_df = pd.read_csv(county_multi_family_csv)

region_affordability_df.to_sql('region_affordability', engine, if_exists = 'replace')
connection.execute("ALTER TABLE region_affordability ADD PRIMARY KEY (index);")

city_single_family_df.to_sql('city_single_family', engine, if_exists = 'replace')
connection.execute("ALTER TABLE city_single_family ADD PRIMARY KEY (index);")

county_single_family_df.to_sql('county_single_family', engine, if_exists = 'replace')
connection.execute("ALTER TABLE county_single_family ADD PRIMARY KEY (index);")

county_multi_family_df.to_sql('county_multi_family', engine, if_exists = 'replace')
connection.execute("ALTER TABLE county_multi_family ADD PRIMARY KEY (index);")