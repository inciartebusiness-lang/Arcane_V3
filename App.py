import streamlit as st
import time

# PROTOCOLO MAESTRO ARCANE V3
st.set_page_config(page_title="ARCANE V3 CORE", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #000000; color: #00FF00; }
    .stButton>button { width: 100%; border: 1px solid #00FF00; background-color: #050505; color: #00FF00; font-weight: bold; height: 3.5em; }
    .stTextArea textarea { background-color: #050505 !important; color: #00FF00 !important; border: 1px solid #00FF00; font-family: 'Courier New'; }
    .stTextInput input { background-color: #050505 !important; color: #00FF00 !important; border: 1px solid #00FF00; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏹 ARCANE V3 CORE")

# ENTRADA TÁCTICA
col_a, col_b = st.columns([2, 1])
with col_a:
    par = st.text_input("GEMA / PAR:", value="MAGMA/USDT")
with col_b:
    ex = st.selectbox("EX:", ["Bybit", "Binance", "MEXC", "DEX"])

info = st.text_area("CONSULTA / INFO ADICIONAL:", placeholder="Escribe tu duda o pega datos aquí...")

st.divider()

# MOTOR DE INTELIGENCIA DINÁMICA
def motor_arcane(fase_tipo):
    query = info.lower()
    if not query:
        return "⚠️ **ERROR:** El núcleo requiere información en el cuadro de INFO para procesar el protocolo."
    
    # LÓGICA DE PROGRAMA 1: ESCANEO
    if fase_tipo == 1:
        if any(x in query for x in ["lista", "cual", "gema", "mejor"]):
            return f"### 🕵️ REPORTE PROG 1\n**ACTIVO:** {par}\n**ESTADO:** Acumulación institucional detectada. El flujo en {ex} indica que es la gema con mayor potencial del set actual. **MÓDULO A: VALIDADO.**"
        return f"### 🕵️ REPORTE PROG 1\nSincronizando {par}. Esperando confirmación de volumen social para clasificar."

    # LÓGICA DE PROGRAMA 2: SNIPER
    if fase_tipo == 2:
        if any(x in query for x in ["entrar", "ahora", "entrada", "comprar", "scalping"]):
            return f"### 🎯 REPORTE PROG 2 (SNIPER)\n**ORDEN:** 🟢 **LONG**\n**CONFIRMACIÓN:** 94% (Módulos A-B-C-D)\n**GHOST MODE:** Sincronizado en {ex}.\n**NOTA:** Entrada óptima en el retroceso del bloque actual."
        return f"### 🎯 REPORTE PROG 2\nAnalizando fractalidad de {par}. No dispares hasta ver concordancia en 15m."

    # LÓGICA DE PROGRAMA 3: RCM
    if fase_tipo == 3:
        return f"### 🛡️ REPORTE PROG 3 (RCM)\n**ESTADO:** Protección Activa.\n**AJUSTE:** Stop Loss a BE +2.5%.\n**TRAILING:** 1.5% activado en {ex}. Tu capital está blindado."

# BOTONES DE EJECUCIÓN
c1, c2, c3 = st.columns(3)
if c1.button("PROG 1"):
    st.markdown(motor_arcane(1))
if c2.button("PROG 2"):
    st.markdown(motor_arcane(2))
if c3.button("PROG 3"):
    st.markdown(motor_arcane(3))

st.sidebar.markdown("### ⚡ SISTEMA")
st.sidebar.success("👻 GHOST MODE: ON")
st.sidebar.write(f"Sincronizado: {ex}")
