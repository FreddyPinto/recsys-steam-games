from fastapi import APIRouter, HTTPException, status
from models import * 
from data import df_endpoint1, df_endpoint2, df_endpoint3, df_endpoint4

router = APIRouter()

@router.get("/developer/{desarrollador}", response_description="Retorna cantidad de items y porcentaje de contenido Free por año según empresa desarrolladora.",response_model=DeveloperResponse)
def get_developer(desarrollador: str):
    df_dev = df_endpoint1[df_endpoint1['developer'] == desarrollador].reset_index()
    df_dev['is_free'] = df_dev['price'] == 0
    result = df_dev.groupby('release_year').agg({'item_id': 'count', 'is_free': 'mean'})
    result.columns = ['Cantidad de Items', 'Contenido Free']
    result['Contenido Free'] = (result['Contenido Free'] * 100).round(2).astype(str) + '%'
    result = result.reset_index().rename(columns={'release_year': 'Año'})
    records = result.reset_index().to_dict('records')
    
    return DeveloperResponse(records=records)



@router.get("/userdata/{User_id}",response_description="Retorna cantidad de dinero gastado por el usuario, el porcentaje de recomendación y cantidad de items.", response_model=UserdataResponse)
def userdata(User_id: str):
    df_user = df_endpoint2[df_endpoint2['user_id'] == User_id].reset_index()
    dinero_gastado = df_user['total_spend'][0]
    cantidad_items = df_user['items_count'][0]
    porcentaje_recomendacion = (df_user[df_user['recommend'] == True]['recommend'].count()/cantidad_items * 100).round(2)

    result = UserdataResponse(
        Usuario=User_id,
        Dinero_gastado=dinero_gastado,
        Porcentaje_de_recomendación=f"{porcentaje_recomendacion}%",
        Cantidad_de_items=cantidad_items
    )

    return result


@router.get("/UserForGenre/{genero}", response_description="Retorna el usuario que acumula más horas jugadas para el género dado y una lista de la acumulación de horas jugadas por año de lanzamiento.")
def UserForGenre(genero: str):
    df_genre = df_endpoint3[genero].reset_index()
    user_max_hours = df_genre.groupby('user_id')[genero].sum().idxmax()
    hours_by_year = df_genre[df_genre['user_id'] == user_max_hours].groupby('release_year')[genero].sum().reset_index()
    hours_by_year.columns = ['Año', 'Horas']
    hours_by_year['Horas'] = hours_by_year['Horas'].astype(int)

    result = {
        f"Usuario con más horas jugadas para Género {genero} " : user_max_hours,
        "Horas jugadas": hours_by_year.to_dict('records')
    }

    return result

@router.get("/best_developer_year/{año}", response_description="Retorna el top 3 de desarrolladores con juegos MÁS recomendados por usuarios para el año dado.")
def best_developer_year(year: int):
    df_year = df_endpoint4[(df_endpoint4['posted_year'] == str(year)) & (df_endpoint4['recommend'] == True) & (df_endpoint4['sentiment_analysis'] == 2)]
    top_developers = df_year['developer'].value_counts().nlargest(3).index.tolist()

    result = [{"Puesto 1" : top_developers[0]},
              {"Puesto 2" : top_developers[1]},
              {"Puesto 3" : top_developers[2]}]

    return result

@router.get("/developer_reviews_analysis/{desarrollador}",response_description="Según el desarrollador, se retorna un diccionario con el nombre del desarrollador como llave y una lista con la cantidad total de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor positivo o negativo.", response_model=DeveloperReviewsAnalysisResponse)
def developer_reviews_analysis(desarrollador: str):
    df_dev = df_endpoint4[df_endpoint4['developer'] == desarrollador]
    sentiment_counts = df_dev['sentiment_analysis'].value_counts()
    negative_reviews = sentiment_counts.get(0, 0)
    positive_reviews = sentiment_counts.get(1, 0) + sentiment_counts.get(2, 0)

    reviews = ReviewAnalysis(Negativos=negative_reviews, Positivos=positive_reviews)
    result = DeveloperReviewsAnalysisResponse(Desarrollador=desarrollador, Reviews=reviews)

    return result
