from typing import List
from fastapi import Header, APIRouter, FastAPI, HTTPException
from app.api.models import CountryIn, CountryOut, CountryUpdate
from app.api import db_manager


# fakeCountryDB=[
#     {
#         'countriesAndTerritories': 'Poland',     
#         #'dateReported': '2020-09-09',
#         'cases': 132,
#         'deaths':10,
#         'caseAvg_14day_per100k': 65.36
#     }
# ]

cData=APIRouter()

@cData.get('/', response_model=List[CountryOut])
async def index(): 
    return await db_manager.get_all_countries()

    
@cData.post('/', status_code=201)
async def addCountryData(payload:CountryIn):
    country_id=await db_manager.add_country(payload)
    response = {
        'id':country_id,
        **payload.dict()
    }
    return response

# @cData.put('/{id}')
# async def update_country(id: int, payload: CountryIn):
#     country=payload.dict()
#     fakeCountryDB[id]=country
#     return None
#     #raise HTTPException(status_code=404, detail="Country with given id not found, no data was changed")


@cData.put('/{id}')
async def update_country(id: int, payload: CountryIn):
    country=await db_manager.get_country(id)
    if not country:
        raise HTTPException(status_code=404, detail="Country with given id not found, no data was changed")
    update_data=payload.dict(exclude_unset=True)
    country_in_db=CountryIn(**country)

    updated_country = country_in_db.copy(update=update_data)

    return await db_manager.update_country(id, updated_country)


@cData.delete('/{id}')
async def deleteCountry(id: int):
    country = await db_manager.get_country(id)
    if not country:
        raise HTTPException(status_code=404, detail="Country with given id not found, no data was deleted")

        return await db_manager.delete_country(id)
