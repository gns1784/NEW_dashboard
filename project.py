import streamlit as st
import pandas as pd
import plotly.express as px

# 데이터 로드
titanic = pd.read_csv("./data/titanic.csv")

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

# 본문에 글 쓰기
st.write("# Titanic Dataset Analysis")
st.write("""
This analysis allows you to filter the Titanic dataset by gender and age range, 
and visualize the age distribution of the selected group of passengers.
Use the sidebar to select the gender and age range you are interested in.
""")

# 데이터 표시
st.write("### Filtered Titanic Data")
st.write(filtered_data)

# 데이터 시각화
st.write(f"### Age Distribution for {sex.capitalize()} Passengers Aged {age_bins[0]} to {age_bins[1]}")

# Plotly를 사용한 히스토그램 생성
fig = px.histogram(filtered_data, x='Age', nbins=10, title='Age Distribution',
                   labels={'Age': 'Age'}, template='plotly_white')
fig.update_layout(yaxis_title='Number of Passengers', xaxis_title='Age')

# Plotly 그래프를 Streamlit에 표시
st.plotly_chart(fig)
