import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Title of the dashboard
st.title('mini-project Streamlit Dashboard')

titanic = pd.read_csv("./data/titanic.csv")
st.write(titanic)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
titanic = pd.read_csv("./data/titanic.csv")
st.write(titanic)

# 사이드바 설정
st.sidebar.header('User Input Parameters')
sex = st.sidebar.selectbox('Select Gender', ('All', 'male', 'female'))
age_bins = st.sidebar.slider('Age Range', 0, 80, (0, 80))

# 필터링 데이터
if sex != 'All':
    filtered_data = titanic[titanic['Sex'] == sex]
else:
    filtered_data = titanic

filtered_data = filtered_data[(filtered_data['Age'] >= age_bins[0]) & (filtered_data['Age'] <= age_bins[1])]

# 데이터 시각화
st.header(f'Titanic Data - {sex.capitalize()} Passengers Aged {age_bins[0]} to {age_bins[1]}')

fig, ax = plt.subplots()
ax.hist(filtered_data['Age'], bins=10, edgecolor='black')
ax.set_title('Age Distribution')
ax.set_xlabel('Age')
ax.set_ylabel('Number of Passengers')
st.pyplot(fig)