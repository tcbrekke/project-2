import numpy as np 
import pandas as pd

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

import psycopg2
import os

from flask import Flask, render_template, jsonify, request, redirect

from flask_sqlalchemy import SQLAlchemy

# DATABASE_URL = os.environ['DATABASE_URL']

# app = Flask(__name__)

# db = SQLAlchemy(app)

Base = automap_base()

engine = create_engine("postgres://dfpdtekrylpjsy:f81dc88e3ae281c5952015a8cf9af3f4af3d20c05130917c07b80c2197a449b4@ec2-54-225-76-243.compute-1.amazonaws.com:5432/df7r9o4t55h9oc")

Base.prepare(engine, reflect=True)

Base.classes.table1.__table__.columns.keys()