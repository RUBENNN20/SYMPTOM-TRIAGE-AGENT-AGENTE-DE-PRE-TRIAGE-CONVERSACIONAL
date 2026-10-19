import streamlit as st
import json
import os

st.set_page_config(
    page_title="Agente de Pre-Triaje Clínico",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Agente de Pre-Triaje Clínico con Utilidad y Aprendizaje")
st.markdown("""
Esta plataforma aloja el sistema multi-escenario de pre-triaje conversacional basado en utilidad y aprendizaje (Fases 2 y 3).
""")

# Pestañas para organizar la interfaz
tab1, tab2, tab3 = st.tabs(["📊 Resultados Fase 3", "🧪 Casos de Prueba Sugeridos", "ℹ️ Instrucciones de Uso"])

with tab1:
    st.header("Resultados Oficiales de Evaluación (Fase 3)")
    
    # Intentar cargar el resumen si existe
    resumen_path = "fase3_resultados/resumen.json"
    if os.path.exists(resumen_path):
        with open(resumen_path, "r", encoding="utf-8") as f:
            resumen = json.load(f)
        st.success("✅ Resultados cargados correctamente desde el servidor.")
    
    # Mostrar la tabla en Markdown si existe
    tabla_path = "fase3_resultados/tabla_resultados.md"
    if os.path.exists(tabla_path):
        with open(tabla_path, "r", encoding="utf-8") as f:
            tabla_md = f.read()
        st.markdown(tabla_md)
    else:
        st.warning("⚠️ No se encontró el archivo de la tabla de resultados. Asegúrate de haber ejecutado las pruebas.")

with tab2:
    st.header("Casos de Prueba Sugeridos para Evaluación")
    st.markdown("""
    Puedes validar el comportamiento del agente evaluando los siguientes escenarios descritos en la arquitectura:
    * **Caso Normal (E1):** Pacientes típicos con parámetros estándar de ruido y cooperación.
    * **Caso Límite (E2):** Casos de frontera (niveles 2, 3 y 4 con solapamiento sintomático alto).
    * **Caso de Pacientes Graves (E3):** Filtrado exclusivo de niveles de urgencia alta (1 y 2).
    * **Caso de Falla en Entradas (E6):** Resiliencia ante entradas inválidas o texto libre anómalo.
    """)

with tab3:
    st.header("Instrucciones de Uso")
    st.markdown("""
    1. **Navegación:** Utiliza las pestañas superiores para alternar entre el panel de métricas de desempeño (M1 a M8) y los escenarios evaluados.
    2. **Verificación de Logs:** Todos los episodios y decisiones del agente quedan registrados de forma auditable en formato JSONL dentro del repositorio.
    3. **Despliegue:** Sistema montado en la nube bajo los requerimientos de la asignatura de arquitectura de software y sistemas inteligentes.
    """)