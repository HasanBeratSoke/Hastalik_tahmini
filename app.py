import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import pickle




pickle_in = open('knn.pkl', 'rb')
classifier = pickle.load(pickle_in)


st.title('Diabetes Prediction')
name = st.text_input("İsim:")
pregnancy = st.number_input("Hamile kalma sayısı:", min_value=0)
glucose = st.number_input("Plazma Glikoz Konsantrasyonu:")
bp =  st.number_input("Diyastolik kan basıncı (mm Hg):")
skin = st.number_input("Triceps cilt kıvrım kalınlığı (mm):")
insulin = st.number_input("2 saatlik serum insülini (mu U/ml):")
bmi = st.number_input("Vücut kitle indeksi (kg cinsinden ağırlık/(m cinsinden yükseklik)^2):")
dpf = st.number_input("Diyabet Soyağacı İşlevi:")
age = st.number_input("Yaşss:")
submit = st.button('Tahmin')
if submit:
    prediction = classifier.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
    if prediction == 0:
        st.write('Tebrikler',name,'Diabet hastası değilsiniz.')
    else:
        st.write(name," diabet hastalığı olma ihtimaliniz yüksek, lütfen en yalın zamanda bir doktara gözükünüz.")