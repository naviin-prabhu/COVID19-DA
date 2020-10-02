from typing import List
from datetime import date
from pydantic import BaseModel

class CountryData(BaseModel):

    countriesAndTerritories: str
    dateReported: date
    cases: int
    deaths:int
    caseAvg_14day_per100k: float
