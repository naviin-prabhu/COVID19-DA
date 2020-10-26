from sqlalchemy import (Column, Integer, MetaData, String, Date, Float, Table, create_engine, ARRAY)

from databases import Database

DATABASE_URL = 'postgresql://naviin:naviin@localhost:5433/covid_db'

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

