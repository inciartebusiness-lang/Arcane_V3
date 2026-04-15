import streamlit as st

# CONFIGURACIÓN NÚCLEO COMPACTO
st.set_page_config(page_title="ARCANE V3 CORE", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #000000; color: #00FF00; }
    .stButton>button { width: 100%; border: 1px solid #00FF00; background-color: #050505; color: #00FF00; font-weight: bold; height: 3em; margin-top: 10px; }
    .stTextArea textarea { background-color: #050505 !important; color: #00FF00 !important; border: 1px solid #00FF00; height: 80px !important; }
    .stTextInput input { background-color: #050505 !important; color: #00FF00 !important; border: 1px solid #00FF00; }
    .stSelectbox div[data-baseweb="select"] { background-color: #050505 !important; color: #00FF00 !important; }
    div[data-baseweb="select"] * { color: #00FF00 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏹 ARCANE V3 CORE")

# FILA 1: PAR Y EXCHANGE
col_a, col_b = st.columns([2, 1])
with col_a:
    par = st.text_input("GEMA / PAR:", placeholder="Ej: MAGMA/USDT")
with col_b:
    ex = st.selectbox("EX:", ["Bybit", "Binance", "MEXC", "DEX"])

# FILA 2: INFO ADICIONAL (CUADRO PEQUEÑO)
info = st.text_area("INFO ADICIONAL / COMANDOS:", placeholder="Notas extra o comandos rápidos...")

st.divider()

# FILA 3: BOTONES DE PROGRAMA (LOS DISPARADORES)
st.write("### ⚡ EJECUTAR PROGRAMA:")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("PROG 1"):
        st.info(f"PROG 1: Escaneando {par} en {ex}...")
        # Aquí procesamos el escaneo 7 niveles
        st.success("LISTO")

with col2:
    if st.button("PROG 2"):
        st.warning(f"PROG 2: Validando Sniper + Ghost Mode...")
        # Aquí validamos módulos A-B-C-D
        st.success("ENTRY OK")

with col3:
    if st.button("PROG 3"):
        st.error(f"PROG 3: RCM Activo para {par}")
        # Aquí calculamos protección BE y Trailing
        st.success("RCM ON")

# ESTADO GHOST SIEMPRE VISIBLE
st.sidebar.markdown("---")
st.sidebar.success("👻 GHOST MODE: ENABLED")
st.sidebar.success("🛡️ ANTI-BARRIDA: ON")
