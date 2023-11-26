# from models import Message
import pandas as pd
import os


def load_data():
    data_dir = os.path.join(os.path.dirname(__file__),
                            'data', 'processed')

    df_pseudo_db1 = pd.read_parquet(
        os.path.join(data_dir, 'pseudo-db1.parquet'))
    df_pseudo_db2 = pd.read_parquet(
        os.path.join(data_dir, 'pseudo-db2.parquet'))

    return df_pseudo_db1, df_pseudo_db2


df_pseudo_db1, df_pseudo_db2 = load_data()


async def PlayTimeGenre(genre: str):

    if genre.upper() == "RPG":
        genre = genre.upper()
    else:
        genre = genre.title()

    if genre not in df_pseudo_db1.columns:
        return None

    df_genre = df_pseudo_db1[genre].reset_index()

    playtime_by_year = df_genre.groupby('release_year')[genre].sum()

    max_playtime_year = (playtime_by_year.idxmax())
    response = {
        f"Year with the most hours played for Genre {genre}": int(max_playtime_year)}

    return response


async def UserForGenre(genre: str):
    if genre.upper() == "RPG":
        genre = genre.upper()
    else:
        genre = genre.title()

    if genre not in df_pseudo_db1.columns:
        return None

    df_genre = df_pseudo_db1[genre].reset_index()
    user_max_hours = df_genre.groupby('user_id')[genre].sum().idxmax()
    playtime_by_year = df_genre[df_genre['user_id'] == user_max_hours].groupby(
        'release_year')[genre].sum().reset_index()
    playtime_by_year.columns = ['Year', 'Hours']
    playtime_by_year = playtime_by_year[playtime_by_year['Hours'] > 0]
    playtime_by_year['Hours'] = playtime_by_year['Hours'].round().astype(int)

    response = {
        f"User with most hours played for Genre {genre} ": user_max_hours,
        "Playtime": playtime_by_year.to_dict('records')
    }

    return response


async def UsersRecommend(year: int):

    if ~df_pseudo_db2['posted_year'].isin([year]).any():
        return None

    df_year = df_pseudo_db2[(df_pseudo_db2['posted_year'] == year) & (
        df_pseudo_db2['recommend'] == True) & (df_pseudo_db2['sentiment_analysis'] > 0)]

    recommendations = df_year.groupby('item_name').size()

    top_games = recommendations.sort_values(ascending=False).head(3)

    response = [{"Rank {}".format(i+1): game}
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

    response = [{"Rank {}".format(i+1): game}
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
