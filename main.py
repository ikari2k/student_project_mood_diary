import streamlit as st
import glob
from pathlib import Path
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px

analyzer = SentimentIntensityAnalyzer()

list_of_files_sorted = sorted(glob.glob("diary/*.txt"))

positive_scores =[]
negative_scores =[]
dates = []

for file in list_of_files_sorted:
    with open(file,"r") as file:
        day = file.read()
    single_date = Path(file.name).stem
    dates.append(single_date)
    scores = analyzer.polarity_scores(day)
    positive_scores.append(scores["pos"])
    negative_scores.append(scores["neg"])


st.title("Positive score trend")
figure = px.line(x=dates, y=positive_scores, labels={"x": "Date","y":"Positive score"})
st.plotly_chart(figure)

st.title("Negative score trend")
figure2 = px.line(x=dates, y=negative_scores, labels={"x": "Date","y":"Negative score"})
st.plotly_chart(figure2)