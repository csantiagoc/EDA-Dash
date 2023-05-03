import pandas as pd
import re
import nltk

nltk.download("stopwords")
from nltk.corpus import stopwords


df = pd.read_csv("data.csv")


def get_top_directors():
    director_counts = df.groupby("director")["show_id"].count().reset_index()

    top_directors = director_counts.sort_values("show_id", ascending=False)[
        :10
    ].sort_values(by="show_id", ascending=True)
    top_directors = top_directors.rename(columns={"show_id": "directed_movies"})
    return top_directors


def get_type_count():
    type_count = df["type"].value_counts()
    return type_count


def get_top_actors():
    df_actors = pd.DataFrame()
    df_actors["actors"] = df["cast"].str.split(", ")
    actor_counts = df_actors.explode("actors").value_counts().head(10).reset_index()
    return actor_counts


def get_country_count():
    df_countries = pd.DataFrame()
    df_countries["countries"] = df["country"].str.split(", ")
    conutries_counts = df_countries.explode("countries").value_counts().reset_index()
    return conutries_counts


def get_saga():
    patterns = {}
    for i, p1 in enumerate(df["title"]):
        for j, p2 in enumerate(df["title"]):
            if i != j and p1 in p2:
                match = p1
                if match not in patterns or len(match) > len(patterns[match]):
                    patterns[match] = re.escape(match)
    df_title = df["title"].copy().reset_index()
    df_title["saga"] = None
    for saga, patron in patterns.items():
        df_title["saga"][df_title["title"].str.contains(patron)] = saga
    saga_dict = df_title["saga"].value_counts().head(30)
    return saga_dict


def get_data_wordcloud():
    all_descriptions = " ".join(df["description"])

    stop_words = set(stopwords.words("english"))
    words = all_descriptions.lower().split()
    words = [w for w in words if w not in stop_words]

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


def get_data_hist_release_year():
    return df


def get_data_pie_rating():
    rating_counts = df["rating"].value_counts()
    return rating_counts


def get_histogram_duration_min():
    df["duration_min"] = df["duration"].apply(
        lambda x: int(x.split()[0]) if "min" in x else None
    )
    return df.dropna(subset=["duration_min"])


def get_histogram_duration_seasons():
    df["duration_season"] = df["duration"].apply(
        lambda x: int(x.split()[0]) if "Season" in x else None
    )
    return df.dropna(subset=["duration_season"])


def get_data_bar_top_10():
    category_counts = (
        df["listed_in"].value_counts().head(10).sort_values(ascending=True)
    )
    return category_counts


def get_bar_chart_top_categories():
    categories = (
        df["listed_in"]
        .str.split(", ")
        .explode()
        .value_counts()
        .nlargest(10)
        .sort_values(ascending=True)
    )
    return categories
