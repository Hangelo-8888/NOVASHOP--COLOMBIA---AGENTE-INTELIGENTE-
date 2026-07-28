# 🤖 NovaShop Colombia - Asistente Virtual J.A.R.V.I.S.

Aplicación web desarrollada con **Streamlit** y la API de **Groq Cloud** (`llama-3.3-70b-versatile`), diseñada para resolver dudas de soporte, envíos y métodos de pago de la tienda NovaShop Colombia basándose en un manual de clientes (PDF).

## 🚀 Características

* **Inferencia Ultrarrápida en la Nube:** Respuestas en tiempo real impulsadas por **Groq Cloud API** y el modelo **Llama 3.3 70B Versatile**.
* **RAG / Lectura de Contexto:** Lee dinámicamente `manual_soporte_clientes.pdf` usando `pypdf` para dar respuestas precisas basadas en las políticas reales de la tienda.
* **Despliegue 24/7:** Disponible de forma pública en Streamlit Community Cloud sin requerir servidores locales ni túneles (Ngrok).
* **Interfaz Fluida:** Desarrollada en Streamlit con gestión de historial de conversación por sesión de usuario.

---

## 🛠️ Requisitos Previos

1. Tener **Python 3.10+** instalado.
2. Contar con una API Key de **[Groq Cloud](https://console.groq.com/)**.

---

## 💻 Instalación y Configuración Local

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/TU_USUARIO/TU_REPOSITORIO.git](https://github.com/TU_USUARIO/TU_REPOSITORIO.git)
   cd TU_REPOSITORIO
