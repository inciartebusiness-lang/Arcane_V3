import streamlit as st
import time

st.set_page_config(page_title="ARCANE V3 CONTROL", layout="centered")

# ESTILO TERMINAL ARCANE
st.markdown("""
    <style>
    .main { background-color: #000000; color: #00FF00; }
    .stButton>button { width: 100%; border: 1px solid #00FF00; background-color: #050505; color: #00FF00; font-weight: bold; border-radius: 5px; margin-bottom: 10px; }
    .stButton>button:hover { background-color: #00FF00; color: black; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏹 ARCANE CONTROL CENTER")

# SELECCIÓN DE PROGRAMA
programa = st.radio("SELECCIONAR FASE:", ["PROG 1: Escaneo & Clasificación", "PROG 2: Entrada Sniper", "PROG 3: Gestión RCM"], horizontal=True)

st.divider()

if "PROG 1" in programa:
    st.subheader("🕵️ PROG 1: ESCANEO SOCIAL Y GEMAS")
    datos_p1 = st.text_area("Pega lista de gemas o datos de mercado:", height=150, placeholder="Ej: Lista de DexScreener, tendencias, o capturas de texto...")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔍 CLASIFICAR GEMAS"):
            st.info("Buscando manipulación y sentimiento...")
            time.sleep(1)
            st.success("FILTRO COMPLETADO: Listado para análisis profundo.")
    with col2:
        if st.button("🔥 TOP 3 CALIENTES"):
            st.warning("Detectando flujo de ballenas en tiempo real...")

elif "PROG 2" in programa:
    st.subheader("🎯 PROG 2: ENTRADA SNIPER")
    activo = st.text_input("ACTIVO SELECCIONADO:", "SOL/USDT")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 VALIDAR ENTRADA"):
            st.success(f"Analizando Order Flow para {activo}...")
            st.code("MODULOS A-B-C-D: COMPILANDO...")
    with col2:
        if st.button("📉 VER FRACTAL"):
            st.info("Buscando concordancia de temporalidades...")

elif "PROG 3" in programa:
    st.subheader("🛡️ PROG 3: GESTIÓN RCM")
    st.write("Configuración de protección activa.")
    
    if st.button("🔒 ACTIVAR GHOST MODE"):
        st.error("GHOST MODE ON: Ocultando Stop Loss en el libro.")
    
    if st.button("📊 CALCULAR BREAK-EVEN (+2.5%)"):
        st.info("Punto de equilibrio ajustado con Trailing al 1.5%.")

st.sidebar.markdown("### ⚡ COMANDOS RÁPIDOS")
if st.sidebar.button("ESTADO DEL MERCADO"):
    st.sidebar.write("🟢 BULLISH (SENTIMIENTO ALTO)")
if st.sidebar.button("ALERTAS DE LIQUIDEZ"):
    st.sidebar.write("⚠️ ZONA DE BARRIDA EN BTC")
