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

    if response.status_code == 200:
        data = response.json()

        st.subheader(f"Cuaca di {data['name']}")

        suhu = data["main"]["temp"]
        kelembapan = data["main"]["humidity"]
        angin = data["wind"]["speed"]
        cuaca = data["weather"][0]["description"]
        ikon = data["weather"][0]["icon"]

        icon_url = f"http://openweathermap.org/img/wn/{ikon}@2x.png"

        st.image(icon_url)
        st.write(f"🌡️ Suhu: **{suhu} °C**")
        st.write(f"💧 Kelembapan: **{kelembapan} %**")
        st.write(f"🌬️ Kecepatan Angin: **{angin} m/s**")
        st.write(f"🌥️ Kondisi: **{cuaca.capitalize()}**")

    else:
        st.error("Kota tidak ditemukan atau terjadi kesalahan API.")

st.markdown("---")
st.caption("Weather App © 2025 | Data: OpenWeatherMap")

