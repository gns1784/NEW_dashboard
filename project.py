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

# 연령대를 구간으로 나누기
age_groups = pd.cut(filtered_data['Age'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80])
age_distribution = filtered_data.groupby(age_groups).size().reset_index(name='Count')

# Plotly를 사용한 바 그래프 생성
fig = px.bar(age_distribution, x='Age', y='Count', title='Age Distribution',
             labels={'Age': 'Age Group', 'Count': 'Number of Passengers'}, template='plotly_white')
fig.update_layout(yaxis_title='Number of Passengers', xaxis_title='Age Group')

# Plotly 그래프를 Streamlit에 표시
st.plotly_chart(fig)
