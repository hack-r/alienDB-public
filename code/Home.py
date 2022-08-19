from datetime import date
from datetime import timedelta
from datetime import datetime
from matplotlib.backends.backend_agg import RendererAgg
from matplotlib.figure import Figure
from pandas import json_normalize
from PIL import Image
from st_aggrid import AgGrid, GridOptionsBuilder
from st_aggrid.shared import GridUpdateMode
from streamlit_player import st_player

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import seaborn as sns
import streamlit as st
import urllib.request
import xmltodict


st.set_page_config(
    layout="centered", page_icon="👽",page_title="AlienDB"
)

st.title("👽 AlienDB.org")
st.image("Media/images/logo.png")
st.markdown(
    """AlienDB is a hub for ET data analytics, machine learning (ML), and exo-AI. More data, visualizations, and Machine Learning are coming soon, so keep checking back.
    
You can navigate this site using the expandable menu on the top left. ↖️
    """ # I hate the word 'hub'... think of a synonym.
)

st.write("")
st.write("")

st.markdown("""
Change Log:
- Appended [People](https://aliendb.org/People) table with UCB SETI researchers
- Added [Radio Signals & Fast Radio Bursts](https://aliendb.org/Radio_Signals_and_FRBs) stub/intro (more soon!)
- Added [Videos](https://aliendb.org/Videos) page
- [Reports](https://aliendb.org/Reports) table: appended "Credibility" column; added 'Oumuamua
""")

st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    padding-left:40px;
}
</style>
''', unsafe_allow_html=True)


# CSS to inject contained in a string
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """

# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)

st.write("")

# Give people someting to look at
st.image('Media/images/navy_pyramid_confirmed_uap_nightvision.png')

st.header("UAP Timeline Plot")
st.image('Media/images/timeline_plot_events_1940_present.png')

# Ear candy
st_player("https://soundcloud.com/ramtagrecordings/ytcracker-on-my-starship?in=ramtagrecordings/sets/ytcracker-space-mission")

# Contact
st.write('(c) 2022 AlienDB.org')

# Remove junk
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

