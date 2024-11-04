import pandas as pd
import altair as alt

alt.renderers.set_embed_options(actions=False)

def get_plot(df):
    chart = alt.Chart(df).mark_line().encode(
        x='x',
        y='y'
    ).properties(
        width='container'
    )
    return chart