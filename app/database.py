# from models import *
import pandas as pd
import os


def load_data():
    data_dir = os.path.join(os.path.dirname(__file__),
                            '..', 'data', 'processed')

    df_pseudo_db1 = pd.read_parquet(
        os.path.join(data_dir, 'pseudo-db1.parquet'))
    df_pseudo_db2 = pd.read_parquet(
        os.path.join(data_dir, 'pseudo-db2.parquet'))

    return df_pseudo_db1, df_pseudo_db2


df_pseudo_db1, df_pseudo_db2 = load_data()


async def PlayTimeGenre(genre: str):

    genre_lower = genre.lower()

    df_genre = df_pseudo_db1[df_pseudo_db1['genres'].str.lower(
    ).str.contains(genre_lower)]

    if df_genre.empty:
        return None

    playtime_by_year = df_genre.groupby(
        'release_year')['playtime_forever'].sum()

    max_playtime_year = int(playtime_by_year.idxmax())
    response = {
        f"Año de lanzamiento con más horas jugadas para el género {genre.capitalize()}": max_playtime_year}

    return response


async def UserForGenre(genre: str):

    genre_lower = genre.lower()

    df_genre = df_pseudo_db1[df_pseudo_db1['genres'].str.lower(
    ).str.contains(genre_lower)]

    if df_genre.empty:
        return None

    playtime_by_user_year = df_genre.groupby(['user_id', 'release_year'])[
        'playtime_forever'].sum().reset_index()

    max_playtime_user = playtime_by_user_year.groupby(
        'user_id')['playtime_forever'].sum().idxmax()

    playtime_by_year = playtime_by_user_year[playtime_by_user_year['user_id'] == max_playtime_user][['release_year', 'playtime_forever']].rename(
        columns={'release_year': 'Año', 'playtime_forever': 'Horas'}).applymap(round).to_dict('records')

    response = {f"Usuario con más horas jugadas para el género {genre.capitalize()}": max_playtime_user,
                "Horas jugadas": playtime_by_year}

    return response


async def UsersRecommend(year: int):

    if ~df_pseudo_db2['posted_year'].isin([year]).any():
        return None

    df_year = df_pseudo_db2[(df_pseudo_db2['posted_year'] == year) & (
        df_pseudo_db2['recommend'] == True) & (df_pseudo_db2['sentiment_analysis'] > 0)]

    recommendations = df_year.groupby('item_name').size()

    top_games = recommendations.sort_values(ascending=False).head(3)

    response = [{"Puesto {}".format(i+1): game}
                for i, game in enumerate(top_games.index)]

    return response


async def UsersWorstDeveloper(year: int):

    if ~df_pseudo_db2['posted_year'].isin([year]).any():
        return None

    df_year = df_pseudo_db2[(df_pseudo_db2['posted_year'] == year) & (
        df_pseudo_db2['recommend'] == False) & (df_pseudo_db2['sentiment_analysis'] == 0)]

    if df_year.empty:
        return {f"No non-recommended games were found for the year {year}"}

    not_recommendations = df_year.groupby('developer').size()

    top_games = not_recommendations.sort_values(ascending=False).head(3)

    response = [{"Puesto {}".format(i+1): game}
                for i, game in enumerate(top_games.index)]

    return response


async def get_sentiment_by_developer(developer: str):

    developer_lower = developer.lower()

    df_dev = df_pseudo_db2[df_pseudo_db2["developer"].str.lower()
                           == developer_lower]

    if df_dev.empty:

        return None

    sentiment_counts = df_dev['sentiment_analysis'].value_counts()
    negative_reviews = sentiment_counts.get(0, 0)
    neutral_reviews = sentiment_counts.get(1, 0)
    positive_reviews = sentiment_counts.get(2, 0)

    response = {
        developer_lower.capitalize(): [
            {"Negative": int(negative_reviews)},
            {"Neutral": int(neutral_reviews)},
            {"Positive": int(positive_reviews)}
        ]
    }

    return response
