import os
import streamlit as st
import ollama
from pypdf import PdfReader

# ---------------------------------------------------------
# 1. Configuración de la página
# ---------------------------------------------------------
st.set_page_config(
    page_title="J.A.R.V.I.S. - NovaShop Colombia",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# 2. Carga del Manual de Soporte (PDF)
# ---------------------------------------------------------
@st.cache_data
def cargar_manual(ruta_pdf):
    if not os.path.exists(ruta_pdf):
        return None
    try:
        reader = PdfReader(ruta_pdf)
        texto = ""
        for page in reader.pages:
            contenido = page.extract_text()
            if contenido:
                texto += contenido + "\n"
        return texto
    except Exception:
        return None

PDF_NOMBRE = "manual_soporte_clientes.pdf"
texto_manual = cargar_manual(PDF_NOMBRE)

# ---------------------------------------------------------
# 3. Barra Lateral (Sidebar Informativa)
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=100)
    st.title("🤖 J.A.R.V.I.S.")
    st.markdown("**Estado:** 🟢 Conectado (Ollama Local)")
    st.markdown("**Modelo:** `llama3.2`")
    st.markdown("---")
    st.markdown("### 🛍️ NovaShop Colombia")
    st.write("Asistente inteligente de atención al cliente optimizado para soporte en tiempo real.")
    
    if st.button("🗑️ Limpiar Conversación"):
        st.session_state.messages = []
        st.rerun()

# ---------------------------------------------------------
# 4. Encabezado Principal
# ---------------------------------------------------------
st.title("🤖 J.A.R.V.I.S. - NovaShop Colombia")
st.subheader("Asistente Virtual de Soporte y Atención al Cliente")
st.markdown(
    "¡Hola! Soy J.A.R.V.I.S. Puedo ayudarte con dudas sobre métodos de pago "
    "(PSE, Nequi, Tarjetas), políticas de envío, devoluciones y soporte general de NovaShop Colombia."
)
st.markdown("---")

# ---------------------------------------------------------
# 5. Prompt de Sistema
# ---------------------------------------------------------
SYSTEM_PROMPT = f"""
Eres J.A.R.V.I.S., el asistente virtual oficial de atención al cliente de NovaShop Colombia.
Tu objetivo es responder las consultas de los clientes con un tono amable, profesional y conciso.

INFORMACIÓN DE CONTEXTO DEL MANUAL DE SOPORTE:
\"\"\"
{texto_manual if texto_manual else "No hay información adicional disponible."}
\"\"\"

REGLAS DE RESPUESTA:
1. Responde basándote prioritariamente en la información del manual cargado.
2. Si la información no está en el manual, responde educadamente que no dispones de ese dato específico y ofrece canalizar con soporte humano.
3. Sé directo, claro y amable.
"""

# ---------------------------------------------------------
# 6. Historial de Chat e Interacción
# ---------------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! Bienvenido a NovaShop Colombia. ¿En qué puedo ayudarte hoy sobre tu compra o soporte?"}
    ]

# Mostrar chat
for message in st.session_state.messages:
    avatar = "🤖" if message["role"] == "assistant" else "👤"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# Entrada de usuario
if prompt := st.chat_input("Escribe tu consulta aquí..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # Preparar mensajes para Ollama
    mensajes_ollama = [{"role": "system", "content": SYSTEM_PROMPT}]
    for msg in st.session_state.messages:
        mensajes_ollama.append({"role": msg["role"], "content": msg["content"]})

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("J.A.R.V.I.S. está pensando..."):
            try:
                response = ollama.chat(
                    model="llama3.2",
                    messages=mensajes_ollama
                )
                bot_response = response["message"]["content"]
                st.markdown(bot_response)
                st.session_state.messages.append({"role": "assistant", "content": bot_response})
            except Exception as e:
                st.error("Error al conectar con el servidor local de Ollama.")
                st.info("Por favor verifica que la aplicación de Ollama esté abierta en tu equipo.")