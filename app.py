import os
import requests
import streamlit as st
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

# Servidor de Ollama
OLLAMA_HOST = st.secrets.get("OLLAMA_HOST", "http://localhost:11434")

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
# 3. Barra Lateral (Sidebar)
# ---------------------------------------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=90)
    st.title("🤖 J.A.R.V.I.S.")
    st.markdown("**Estado:** 🟢 Conectado (Ollama)")
    st.markdown("**Modelo:** `llama3.2`")
    st.markdown("---")
    
    st.markdown("### 💡 Preguntas de Prueba")
    st.caption("Prueba copiando estas consultas:")
    st.markdown("""
    - *¿Cuáles son los métodos de pago aceptados?*
    - *¿Cuánto tarda en llegar un envío?*
    - *¿Cuál es la política de devoluciones?*
    """)
    st.markdown("---")
    
    if st.button("🗑️ Limpiar Conversación"):
        st.session_state.messages = []
        st.rerun()

# ---------------------------------------------------------
# 4. Encabezado Principal
# ---------------------------------------------------------
st.title("🤖 J.A.R.V.I.S. - NovaShop Colombia")
st.subheader("Asistente Virtual de Soporte y Atención al Cliente")
st.markdown("¡Hola! Soy J.A.R.V.I.S. Puedo ayudarte con dudas sobre métodos de pago, envíos y soporte general.")
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

# Historial de Chat
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! Bienvenido a NovaShop Colombia. ¿En qué puedo ayudarte hoy?"}
    ]

for message in st.session_state.messages:
    avatar = "🤖" if message["role"] == "assistant" else "👤"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# ---------------------------------------------------------
# 6. Petición HTTP a Ollama
# ---------------------------------------------------------
if prompt := st.chat_input("Escribe tu consulta aquí..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    mensajes_ollama = [{"role": "system", "content": SYSTEM_PROMPT}]
    for msg in st.session_state.messages:
        mensajes_ollama.append({"role": msg["role"], "content": msg["content"]})

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("J.A.R.V.I.S. está pensando..."):
            try:
                # Se llama directamente a la API HTTP de Ollama
                url = f"{OLLAMA_HOST.rstrip('/')}/api/chat"
                payload = {
                    "model": "llama3.2",
                    "messages": mensajes_ollama,
                    "stream": False
                }
                
                response = requests.post(url, json=payload, timeout=60)
                
                if response.status_code == 200:
                    bot_response = response.json()["message"]["content"]
                    st.markdown(bot_response)
                    st.session_state.messages.append({"role": "assistant", "content": bot_response})
                else:
                    st.error(f"Error en el servidor de Ollama (Código {response.status_code})")
                    
            except Exception as e:
                st.error("No se pudo conectar con el servidor de Ollama.")
                st.info("Si estás ejecutando en la nube, verifica que la URL en Secrets (OLLAMA_HOST) esté activa.")
