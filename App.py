import streamlit as st

# CONFIGURACIÓN ARCANE MOBILE-READY
st.set_page_config(page_title="ARCANE V3", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #000000; color: #00FF00; }
    .stButton>button { width: 100%; background-color: #00FF00; color: black; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏹 ARCANE TACTICAL V3")

tab1, tab2 = st.tabs(["ANÁLISIS", "RIESGO RCM"])

with tab1:
    activo = st.text_input("ACTIVO", "BTC/USDT")
    datos = st.text_area("DATOS DEL MERCADO", placeholder="Pega aquí...")
    if st.button("EJECUTAR SNIPER"):
        st.success(f"ANALIZANDO {activo}...")
        st.info("SISTEMA ARCANE: CONECTADO")

with tab2:
    st.subheader("PARÁMETROS RCM")
    st.write("✅ PROTECCIÓN BE: +2.5%")
    st.write("✅ TRAILING: +1.5%")
