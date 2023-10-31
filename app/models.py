from typing import List
from pydantic import BaseModel, Field

class DeveloperRecord(BaseModel):
    release_year: int = Field(alias='Año')
    Cantidad_de_Items: int = Field(alias='Cantidad de Items')
    Contenido_Free: str = Field(alias='Contenido Free')

class DeveloperResponse(BaseModel):
    records: List[DeveloperRecord]  
    
class UserdataResponse(BaseModel):
    Usuario: str
    Dinero_gastado: float 
    Porcentaje_de_recomendación: str 
    Cantidad_de_items: int

class ReviewAnalysis(BaseModel):
    Negativos: int
    Positivos: int

class DeveloperReviewsAnalysisResponse(BaseModel):
    Desarrollador: str
    Reviews: ReviewAnalysis
