from typing import List, Optional
from datetime import date
from pydantic import BaseModel

class CountryIn(BaseModel):

    countriesAndTerritories: str
    date: date
    cases: int
    deaths:int
    caseAvg_14day_per100k: float

class CountryOut(CountryIn):
    id: int

    
class CountryUpdate(CountryIn):
    countriesAndTerritories: Optional[str]=None
    date: date
    cases: Optional[int]=None
    deaths:Optional[int]=None
    caseAvg_14day_per100k: Optional[float]=None
