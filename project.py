import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the dashboard
st.title('mini-project Streamlit Dashboard')

titanic = pd.read_csv("./data/titanic.csv")
st.write(titanic)
