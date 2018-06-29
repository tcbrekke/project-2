import numpy as np 
import pandas as pd
import json

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

import psycopg2
import os

from flask import Flask, render_template, jsonify, request, redirect

# from flask_sqlalchemy import SQLAlchemy

# DATABASE_URL = os.environ['DATABASE_URL']

# app = Flask(__name__)

# db = SQLAlchemy(app)
engine = create_engine("postgresql://tcbrekke:password@localhost/project2scratch")
connection = engine.connect()
inspector = inspect(engine)

Base = automap_base()
Base.prepare(engine, reflect=True)

region_affordability_table = Base.classes.region_affordability
city_single_family_table = Base.classes.city_single_family
county_single_family_table = Base.classes.county_single_family
county_multi_family_table = Base.classes.county_multi_family

session = Session(engine)

table = session.query(region_affordability_table).all()

region_affordability_list = list(np.ravel(table))
# ra_json = json.dumps(region_affordability_list)
# ra_df = pd.read_sql(region_affordability_table, connection)
# print(ra_df)
# print(table)
# print(region_affordability_list)
# print(region_affordability_table)
# print(json.dumps(connection.execute("SELECT * FROM region_affordability;")))
def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

radf = (pd.read_sql('region_affordability', connection))
print(radf.to_json(orient="index"))
print(region_affordability_list)



# @app.route('/region_affordability')
# def ra():
# 	results = session.query(region_affordability_table).first()

# 	region_affordability_list = list(np.ravel(results))
# 	return jsonify(region_affordability_list)
# 	# print(type(region_affordability_list))
# 	# return json.dumps(region_affordability_list)

# @app.route('/city_single_family')
# def cisf():
# 	results = session.query(city_single_family_table).all()

# 	city_single_family_list = list(np.ravel(results))
# 	return jsonify(city_single_family_list)

# @app.route('/county_single_family')
# def cosf():
# 	results = session.query(county_single_family_db).all()

# 	county_single_family_list = list(np.ravel(results))
# 	return jsonify(county_single_family_list)

# @app.route('/county_multi_family')
# def comf():
# 	results = session.query(county_multi_family_db).all()

# 	county_multi_family_list = list(np.ravel(results))
# 	return jsonify(county_multi_family_list)

# if __name__ == "__main__":
#     app.run(debug=True)