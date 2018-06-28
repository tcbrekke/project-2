import psycopg2
import pandas as pd
import os
from sqlalchemy import create_engine

host = "localhost"
user = "tcbrekke"
database = "project2scratch"

DATABASE_URL = os.environ['DATABASE_URL']

region_affordability_csv = os.path.join("Resources", "Affordability_Wide_2018Q1_PublicCLEAN.csv")
city_single_family_csv = os.path.join("Resources", "City_Zhvi_SingleFamilyResidence(main)CLEAN.csv")
county_single_family_csv = os.path.join("Resources", "County_Zhvi_SingleFamilyResidenceCLEAN.csv")
county_multi_family_csv = os.path.join("Resources", "County_Zri_AllHomesPlusMultifamilyCLEAN.csv")

engine = create_engine(DATABASE_URL)

region_affordability_df = pd.read_csv(region_affordability_csv)
city_single_family_df = pd.read_csv(city_single_family_csv)
county_single_family_df = pd.read_csv(county_single_family_csv)
county_multi_family_df = pd.read_csv(county_multi_family_csv)

region_affordability_df.to_sql('region_affordibility', engine, if_exists = 'replace')
city_single_family_df.to_sql('city_single_family', engine, if_exists = 'replace')
county_single_family_df.to_sql('county_single_family', engine, if_exists = 'replace')
county_multi_family_df.to_sql('county_multi_family', engine, if_exists = 'replace')