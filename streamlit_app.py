import streamlit as st
import requests

# ==============================
# WEATHER FORECAST APP
# ==============================

API_KEY = "ISI_API_KEY_KAMU"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

st.set_page_config(
    page_title="Weather App",
    page_icon="🌤️",
    layout="centered"
)

st.title("Aplikasi Ramalan Cuaca")
st.write("Menampilkan informasi cuaca terkini berdasarkan kota.")

kota = st.text_input("Masukkan nama kota", "Jakarta")

if st.button("Cek Cuaca"):
    params = {
        "q": kota,
        "appid": API_KEY,
        "units": "metric",
        "lang": "id"
    }

    response = requests.get(BASE_URL, params=params)

    if response.stat
