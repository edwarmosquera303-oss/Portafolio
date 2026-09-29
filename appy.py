import os
import streamlit as st
from PIL import Image

# Configuración de la página en modo ancho para aprovechar mejor las columnas
st.set_page_config(layout="wide")
st.title("Laboratorio Edwards Mosquera")

with st.sidebar:
    st.subheader("Acerca de las Prácticas")
    parrafo = (
        "Este espacio recopila una serie de herramientas interactivas, "
        "modelos de Machine Learning, análisis de datos y sistemas IoT "
        "diseñados para comprender de forma práctica los conceptos clave de la IA."
    )
    st.write(parrafo)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")

# Lista ordenada de las 11 prácticas con sus imágenes, títulos, descripciones y enlaces
practicas = [
    {
        "img": "img1",
        "titulo": "¿Qué fruta es más parecida?",
        "desc": "**Similaridad Vectorial mediante Distancia Euclídea Directa.** Esta práctica enseña a medir la semejanza entre objetos del mundo real transformando sus características (peso, diámetro y dulzor) en vectores dentro de un espacio 3D.",
        "url": ""
    },
    {
        "img": "img2",
        "titulo": "Descenso de Gradiente Interactivo",
        "desc": "Una herramienta visual para comprender el algoritmo de optimización central del aprendizaje automático. Muestra cómo los parámetros afectan la convergencia hacia el mínimo de una función de costo en 3D.",
        "url": ""
    },
    {
        "img": "img3",
        "titulo": "Detector de Anomalías: Lógica + Big-O",
        "desc": "Un benchmark visual que compara dos enfoques para detectar anomalías (umbrales lógicos vs. vectorización con NumPy), destacando la importancia de la complejidad computacional (Big-O).",
        "url": ""
    },
    {
        "img": "img4",
        "titulo": "Estructura y Preparación de Datos",
        "desc": "**Módulo 5 (IoT):** Una interfaz para configurar y explorar un dataset sintético de sensores IoT enfocado en lidiar con valores faltantes y valores atípicos (outliers).",
        "url": ""
    },
    {
        "img": "img5",
        "titulo": "Nivel de Ríos y Quebradas",
        "desc": "**CORNARE:** Un panel de control (dashboard) para el monitoreo en tiempo real de datos hidrológicos y ubicación geográfica para la gestión de recursos naturales.",
        "url": ""
    },
    {
        "img": "img6",
        "titulo": "Regresión: Conceptos Clave",
        "desc": "**(Vivienda):** Herramienta interactiva para ajustar modelos de regresión lineal (simple y múltiple) sobre datos reales de vivienda en California, explorando el error (MSE).",
        "url": ""
    },
    {
        "img": "img7",
        "titulo": "Series de Tiempo - Sensor IoT",
        "desc": "Aplicación interactiva para descomponer y analizar series temporales simuladas (temperatura), ajustando componentes como tendencia, estacionalidad y ruido.",
        "url": ""
    },
    {
        "img": "img8",
        "titulo": "Calidad del Aire - CORNARE",
        "desc": "**(MARCO):** Interfaz que permite cargar modelos predictivos (`.pkl`) para realizar pronósticos de calidad del aire (PM2.5 y PM10) en una región específica.",
        "url": ""
    },
    {
        "img": "img9",
        "titulo": "Predictor de Sensación Térmica",
        "desc": "Aplicación que conecta con una base de datos en tiempo real (InfluxDB) para obtener datos IoT y entrenar un modelo de regresión lineal que predice la sensación térmica.",
        "url": ""
    },
    {
        "img": "img10",
        "titulo": "¿Lloverá mañana?",
        "desc": "**Regresión Logística Interactiva:** Herramienta para explorar clasificación binaria, visualizando la función sigmoide y el umbral de clasificación para predecir lluvia.",
        "url": ""
    },
    {
        "img": "img11",
        "titulo": "Explora KNN en Suelos",
        "desc": "**(AGROSAVIA):** Caso de estudio avanzado que aplica el algoritmo K-NN a datos abiertos reales para clasificar la fertilidad del suelo (baja, media, alta).",
        "url": ""
    }
]

# Organizar en filas de 3 columnas de manera limpia y estructurada
for i in range(0, len(practicas), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(practicas):
            p = practicas[i + j]
            with cols[j]:
                # Contenedor con borde para cada tarjeta
                with st.container(border=True):
                    st.subheader(p["titulo"])
                    
                    # Detección automática de la extensión de la imagen (.jpg, .png, .webp)
                    encontrada = False
                    for ext in ['.jpg', '.png', '.webp']:
                        ruta = p["img"] + ext
                        if os.path.exists(ruta):
                            try:
                                st.image(Image.open(ruta), use_container_width=True)
                                encontrada = True
                                break
                            except Exception:
                                pass
                    if not encontrada:
                        st.warning(f"Imagen '{p['img']}.*' no encontrada.")
                    
                    st.write(p["desc"])
                    st.write(f"Acceso: [Enlace]({p['url']})")
