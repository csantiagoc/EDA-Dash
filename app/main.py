import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import plotly.express as px
from wordcloud import WordCloud
import graph_descriptions
import dash_bootstrap_components as dbc


from service_layer import (
    get_top_directors,
    get_type_count,
    get_top_actors,
    get_country_count,
    get_saga,
    get_data_wordcloud,
    get_data_hist_release_year,
    get_data_pie_rating,
    get_histogram_duration_min,
    get_histogram_duration_seasons,
    get_data_bar_top_10,
    get_bar_chart_top_categories,
)


def top_dictors_graph():
    data = get_top_directors()
    top_directors = px.bar(data, x="directed_movies", y="director", orientation="h")
    top_directors.update_layout(
        xaxis_title="Director",
        yaxis_title="Directed movies",
    )
    return top_directors


def type_graph():
    data = get_type_count()
    type_graph = px.pie(names=data.index, values=data.values)
    return type_graph


def top_actors_graph():
    data = get_top_actors()
    actors_graph = px.bar(data, x="actors", y="count")

    return actors_graph


def country_count_graph():
    data = get_country_count()
    country_graph = px.scatter_geo(
        data,
        locations="countries",
        locationmode="country names",
        color="count",
        hover_name="countries",
        projection="natural earth",
        scope="world",
    )
    country_graph.update_layout(coloraxis=dict(colorscale="Bluered", cmin=0, cmax=200))
    return country_graph


def title_graph():
    data = get_saga()
    title_graph = px.bar(x=data.index, y=data.values)
    title_graph.update_layout(
        xaxis_title="Name of the saga",
        yaxis_title="Number of movies that are part of the saga",
    )
    return title_graph


def description_wordcloud():
    data = get_data_wordcloud()
    wc = WordCloud(
        width=800, height=400, background_color="white", max_words=200
    ).generate_from_frequencies(data)
    fig = px.imshow(wc)
    fig.update_layout(title_text="Wordcloud de descripciones de películas")
    return fig


def hist_release_year_graph():
    data = get_data_hist_release_year()
    fig = px.histogram(data, x="release_year", nbins=50)
    return fig


def pie_rating_graph():
    data = get_data_pie_rating()
    fig = px.pie(data, values=data.values, names=data.index)
    return fig


def histogram_duration_min_graph():
    data = get_histogram_duration_min()
    fig = px.histogram(data, x="duration_min", nbins=50)
    return fig


def histogram_duration_season_graph():
    data = get_histogram_duration_seasons()
    fig = px.histogram(data, x="duration_season")
    return fig


def bar_top_10_graph():
    data = get_data_bar_top_10()
    fig = px.bar(data, x=data.values, y=data.index, orientation="h")
    return fig


def bar_chart_top_categories_graph():
    data = get_bar_chart_top_categories()
    fig = px.bar(data, x=data.values, y=data.index, orientation="h")
    return fig


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


app.layout = dbc.Container(
    children=[
        html.H1(children="Disney plus data set"),
        html.P(graph_descriptions.INTRODUCTION_TEXT),
        html.Div(
            children=[
                html.H2(children="Top 10 directors"),
                html.P(graph_descriptions.DIRECTOR_TEXT),
                dcc.Graph(id="top-directors", figure=top_dictors_graph()),
            ]
        ),
        html.Div(
            children=[
                html.H2(children="Show type"),
                html.P(graph_descriptions.TYPE_TEXT),
                dcc.Graph(id="show-type", figure=type_graph()),
            ]
        ),
        html.Div(
            children=[
                html.H2(children="Top 10 actors"),
                html.P(graph_descriptions.CAST_TEXT),
                dcc.Graph(id="top-actors", figure=top_actors_graph()),
            ]
        ),
        html.Div(
            children=[
                html.H2(children="Shows per country"),
                html.P(graph_descriptions.COUNTRY_TEXT),
                dcc.Graph(id="country", figure=country_count_graph()),
            ]
        ),
        html.Div(
            children=[
                html.H2(children="Sagas identified in movie titles"),
                html.P(graph_descriptions.TITLE_TEXT),
                dcc.Graph(id="sagas", figure=title_graph()),
            ]
        ),
        html.Div(
            children=[
                html.H2(children="Wordcloud of most frequent words in the description"),
                html.P(graph_descriptions.DESCRIPTION_TEXT),
                dcc.Graph(id="wordcloud", figure=description_wordcloud()),
            ]
        ),
        html.Div(
            children=[
                html.H2(children="Histogram release year"),
                html.P(graph_descriptions.RELEASE_YEAR_TEXT),
                dcc.Graph(id="histo-release-year", figure=hist_release_year_graph()),
            ]
        ),
        html.Div(
            children=[
                html.H2(children="Rating"),
                html.P(graph_descriptions.RATING_TEXT),
                dcc.Graph(id="pie-rating", figure=pie_rating_graph()),
            ]
        ),
        html.Div(
            children=[
                html.H2(children="Duration in minutes"),
                html.P(graph_descriptions.DURATION_TEXT),
                dcc.Graph(id="hist-duration", figure=histogram_duration_min_graph()),
            ]
        ),
        html.Div(
            children=[
                html.H2(children="Duration in seasons"),
                dcc.Graph(
                    id="hist-duration-season", figure=histogram_duration_season_graph()
                ),
            ]
        ),
        html.Div(
            children=[
                html.H2(children="Group of categories"),
                html.P(graph_descriptions.LISTED_IN_TEXT),
                dcc.Graph(id="cat-top-10-mixed", figure=bar_top_10_graph()),
            ]
        ),
        html.Div(
            children=[
                html.H2(children="Categories"),
                dcc.Graph(id="cat-top-10", figure=bar_chart_top_categories_graph()),
            ]
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
