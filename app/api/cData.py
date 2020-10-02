from typing import List
from fastapi import Header, APIRouter, FastAPI, HTTPException
from app.api.models import CountryData


fakeCountryDB=[
    {
        'countriesAndTerritories': 'Poland',     
        'dateReported': '2020-09-09',
        'cases': 132,
        'deaths':10,
        'caseAvg_14day_per100k': 65.36
    }
]

cData=APIRouter()

@cData.get('/', response_model=List[CountryData])
async def index(): 
    return fakeCountryDB

    
@cData.post('/', status_code=201)
async def addCountryData(payload:CountryData):
    country=payload.dict()
    fakeCountryDB.append(country)
    return {'id': len(fakeCountryDB)-1}

@cData.put('/{id}')
async def update_country(id: int, payload: CountryData):
    country=payload.dict()
    country_length=len(fakeCountryDB)
    if 0<= id <= country_length:
        fakeCountryDB[id]=country
        return None
    raise HTTPException(status_code=404, detail="Country with given id not found, no data was changed")

@cData.delete('/{id}')
async def deleteCountry(id: int):
    country_length=len(fakeCountryDB)
    if 0 <= id <= country_length:
        del fakeCountryDB[id]
        return None
    raise HTTPException(status_code=404, detail="Country with given id not found, nothing was deleted")