import numpy as np 
import pandas as pd

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from config import api_key

import requests

url = f"https://www.quandl.com/api/v3/datasets/ZILLOW/{AREA}"

#Sample
