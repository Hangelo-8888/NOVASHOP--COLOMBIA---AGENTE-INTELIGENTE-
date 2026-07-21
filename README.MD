# 🤖 NovaShop Colombia - Asistente Virtual J.A.R.V.I.S.

Aplicación web desarrollada con **Streamlit** y un Modelo de Lenguaje de Gran Escala (LLM) **local mediante Ollama** (`llama3.2`), diseñada para resolver dudas de soporte, envíos y métodos de pago de la tienda NovaShop Colombia basándose en un manual de clientes (PDF).

## 🚀 Características
- **Modelos Local:** Sin dependencia de API Keys ni servicios de pago (Usa Ollama + Llama 3.2).
- **RAG / Lectura de Contexto:** Lee dinámicamente `manual_soporte_clientes.pdf` usando `pypdf`.
- **Interfaz Fluida:** Desarrollada en Streamlit con gestión de historial de chat.

## 🛠️ Requisitos Previos
1. Instalar [Ollama](https://ollama.com/) en tu equipo.
2. Ejecutar en terminal para descargar el modelo:
   ```bash
   ollama run llama3.2
