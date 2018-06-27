import numpy as np 
import pandas as pd

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

import psycopg2
import os

from flask import Flask, render_template, jsonify, request, redirect

from flask_sqlalchemy import SQLAlchemy

DATABASE_URL = os.environ['DATABASE_URL']

app = Flask(__name__)

db = SQLAlchemy(app)

conn = psycopg2.connect(DATABASE_URL, sslmode='require')