from fastapi import  FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from datetime import datetime, date

app=FastAPI()


fakeCountryDB=[
    {
        'countriesAndTerritories': 'Poland',     
        'dateRep': '2020-09-09',
        'cases': 132,
        'deaths':10,
        'caseAvg_14day_per100k': 65.36
    }
]

class CountryData(BaseModel):
    countriesAndTerritories: str
    dateRep: date
    cases: int
    deaths:int
    caseAvg_14day_per100k: float

@app.get('/', response_model=List[CountryData])
async def index():
    countryData = CountryData(fakeCountryDB[0])
    return countryData

    
# @app.post('/', status_code=201)
# async def addCountryData(payload:CountryData):
#     country=payload.dict()
#     fakeCountryDB.append(country)
#     return {'id': len(fakeCountryDB)-1}

# @app.put('/{id}')
# async def update_country(id: int, payload: CountryData):
#     country=payload.dict()
#     country_length=len(fakeCountryDB)
#     if 0<= id <= country_length:
#         fakeCountryDB[id]=country
#         return None
#     raise HTTPException(status_code=404, detail="Country with given id not found, no data was changed")

# @app.delete('/{id}')
# async def deleteCountry(id: int):
#     country_length=len(fakeCountryDB)
#     if 0 <= id <= country_length:
#         del fakeCountryDB[id]
#         return None
#     raise HTTPException(status_code=404, detail="Country with given id not found, nothing was deleted")