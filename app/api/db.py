from sqlalchemy import (Column, Integer, MetaData, String, Date, Float, Table, create_engine, ARRAY)

from databases import Database

from credentials.dbCredentials import *

engine = create_engine(DATABASE_URL)
metadata = MetaData()

countries = Table(
    'countries',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('date', Date,primary_key=True),
    Column('countriesAndTerritories', String(50)),
    Column('cases', Integer),
    Column('deaths', Integer),
    Column('caseAvg_14day_per100k', Float)
)

database=Database(DATABASE_URL)

