import streamlit as st

# ==============================
# STOICHIA - Stoichiometry App
# ==============================

st.set_page_config(
    page_title="Stoichia",
    page_icon="⚗️",
    layout="centered"
)

st.title("Stoichia")
st.subheader("Kalkulator Stoikiometri Sederhana")
st.write(
    "Aplikasi ini membantu perhitungan dasar stoikiometri "
    "untuk mahasiswa kimia dan sains."
)

menu = st.sidebar.selectbox(
    "Pilih Menu",
    [
        "Hitung Mol",
        "Hitung Massa",
        "Mol ke Massa",
        "Stoikiometri Reaksi"
    ]
)

# ------------------------------
# HITUNG MOL
# ------------------------------
if menu == "Hitung Mol":
    st.header("Perhitungan Mol")

    massa = st.number_input("Massa zat (gram)", min_value=0.0)
    mr = st.number_input("Mr (massa molekul relatif)", min_value=0.0)

    if st.button("Hitung Mol"):
        if mr == 0:
            st.error("Mr tidak boleh nol.")
        else:
            mol = massa / mr
            st.success(f"Jumlah mol = {mol:.4f} mol")

# ------------------------------
# HITUNG MASSA
# ------------------------------
elif menu == "Hitung Massa":
    st.header("Perhitungan Massa")

    mol = st.number_input("Jumlah mol (mol)", min_value=0.0)
    mr = st.number_input("Mr (massa molekul relatif)", min_value=0.0)

    if st.button("Hitung Massa"):
        massa = mol * mr
        st.success(f"Massa zat = {massa:.4f} gram")

# ------------------------------
# MOL KE MASSA
# ------------------------------
elif menu == "Mol ke Massa":
    st.header("Konversi Mol ke Massa")

    mol = st.number_input("Jumlah mol (mol)", min_value=0.0)
    mr = st.number_input("Mr zat", min_value=0.0)

    if st.button("Konversi"):
        massa = mol * mr
        st.success(f"Hasil konversi = {massa:.4f} gram")

# ------------------------------
# STOIKIOMETRI REAKSI
# ------------------------------
elif menu == "Stoikiometri Reaksi":
    st.header("Stoikiometri Reaksi Sederhana")

    st.write(
        "Perhitungan berdasarkan perbandingan koefisien reaksi."
    )

    mol_diketahui = st.number_input("Mol zat diketahui (mol)", min_value=0.0)
    koef_diketahui = st.number_input("Koefisien zat diketahui", min_value=1)
    koef_ditanya = st.number_input("Koefisien zat ditanya", min_value=1)

    if st.button("Hitung Mol Zat Ditanya"):
        mol_ditanya = (koef_ditanya / koef_diketahui) * mol_diketahui
        st.success(f"Mol zat ditanya = {mol_ditanya:.4f} mol")

st.markdown("---")
st.caption("Stoichia © 2025 | Kalkulator Stoikiometri Mahasiswa")
