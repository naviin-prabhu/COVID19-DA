from app.api.models import CountryIn, CountryOut, CountryUpdate
from app.api.db import countries, database

async def add_country(payload: CountryIn):
    query = countries.insert().values(**payload.dict())

    return await  database.execute(query=query)

async def get_all_countries():
    query=countries.select()
    return await database.fetch_all(query=query)

async def get_country(id):
    query=countries.delete().where(countries.c.id==id)
    return await database.fetch_one(query=query)

async def delete_country(id: int):
    query=countries.delete().where(countries.c.id==id)
    return await  database.execute(query=query)

async def update_country(id: int, payload:CountryIn):
    query=(
        countries.update().where(countries.c.id==id)
        .values(**payload.dict())
    )

    return await database.execute(query=query)