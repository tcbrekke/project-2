import numpy as np 
import pandas as pd
import json

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

import psycopg2
import os

from flask import Flask, render_template, jsonify, request, redirect

from flask_sqlalchemy import SQLAlchemy

# DATABASE_URL = os.environ['DATABASE_URL']

app = Flask(__name__)

db = SQLAlchemy(app)
engine = create_engine("postgres://dfpdtekrylpjsy:f81dc88e3ae281c5952015a8cf9af3f4af3d20c05130917c07b80c2197a449b4@ec2-54-225-76-243.compute-1.amazonaws.com:5432/df7r9o4t55h9oc")
connection = engine.connect()

Base = automap_base()
Base.prepare(engine, reflect=True)

region_affordability_table = Base.classes.region_affordability
city_single_family_table = Base.classes.city_single_family
county_single_family_table = Base.classes.county_single_family
county_multi_family_table = Base.classes.county_multi_family

session = Session(engine)

@app.route('/region_affordability')
def ra():
	# results = session.query(region_affordability_table)
	results_df = pd.read_sql('region_affordability', connection)

	return results_df.to_json(orient="index")


	# region_affordability_list = list(np.ravel(results))
	# return jsonify(region_affordability_list)
	# print(type(region_affordability_list))
	# return json.dumps(region_affordability_list)

@app.route('/city_single_family')
def cisf():
	# results = session.query(city_single_family_db).all()

	# city_single_family_list = list(np.ravel(results))
	# return jsonify(city_single_family_list)
	results_df = pd.read_sql('city_single_family', connection)

	return results_df.to_json(orient="index")


@app.route('/county_single_family')
def cosf():
	# results = session.query(county_single_family_db).all()

	# county_single_family_list = list(np.ravel(results))
	# return jsonify(county_single_family_list)
	results_df = pd.read_sql('county_single_family', connection)

	return results_df.to_json(orient="index")

@app.route('/county_multi_family')
def comf():
	# results = session.query(county_multi_family_db).all()

	# county_multi_family_list = list(np.ravel(results))
	# return jsonify(county_multi_family_list)
	results_df = pd.read_sql('county_multi_family', connection)

	return results_df.to_json(orient="index")

if __name__ == "__main__":
    app.run(debug=True)