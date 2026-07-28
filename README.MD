# 🤖 NovaShop Colombia - Asistente Virtual J.A.R.V.I.S.

Aplicación web desarrollada con **Streamlit** y la API de **Groq Cloud** (`llama-3.3-70b-versatile`), diseñada para resolver dudas de soporte, envíos y métodos de pago de la tienda NovaShop Colombia basándose en un manual de clientes (PDF).

---

## 🌐 Probar la Aplicación en Vivo

Puedes interactuar con J.A.R.V.I.S. en tiempo real desde cualquier dispositivo ingresando al siguiente enlace:

👉 **[Acceder a J.A.R.V.I.S. NovaShop](https://zhize3bs3k3vg9usbyzsgt.streamlit.app)**

---

## 🚀 Características

* **Inferencia Ultrarrápida en la Nube:** Respuestas en tiempo real impulsadas por **Groq Cloud API** y el modelo **Llama 3.3 70B Versatile**.
* **RAG / Lectura de Contexto:** Lee dinámicamente `manual_soporte_clientes.pdf` usando `pypdf` para dar respuestas precisas basadas en las políticas reales de la tienda.
* **Disponibilidad 24/7:** Desplegada públicamente en Streamlit Community Cloud sin depender de servidores ni entornos locales.
* **Interfaz Fluida:** Desarrollada en Streamlit con gestión de historial de conversación por sesión de usuario.

---

## 📄 Tecnologías Utilizadas

* **Python 3.10+**
* **Streamlit** (Interfaz Web)
* **Groq SDK** (Procesamiento de LLM)
* **PyPDF** (Extracción de texto desde PDF)
