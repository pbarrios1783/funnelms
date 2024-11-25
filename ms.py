import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configurar página de Streamlit
st.set_page_config(page_title="Funnel de Lead Generation", layout="wide")

# Crear el DataFrame inicial
data = {
    "Etapa": [
        "Visitantes al Perfil/Sitio Web",
        "Interacciones Iniciales",
        "Sesiones Informativas Agendadas",
        "Sesiones Pagadas Confirmadas",
        "Clientes Recurrentes"
    ],
    "Objetivo Semanal": [100, 20, 10, 5, 3],
    "Progreso Real": [0, 0, 0, 0, 0],
}
df = pd.DataFrame(data)

# Título de la app
st.title("Funnel de Lead Generation")

# Dividir la página en tres columnas
col1, col2, col3 = st.columns(3)

# Columna 1: Formulario para actualizar progreso
with col1:
    st.header("Actualizar Progreso Diario")
    for i, row in df.iterrows():
        progreso = st.number_input(
            f"{row['Etapa']}", 
            min_value=0, 
            value=row['Progreso Real'], 
            step=1, 
            key=row['Etapa']
        )
        df.at[i, "Progreso Real"] = progreso
    if st.button("Guardar Progreso", key="guardar"):
        df.to_csv("funnel_progreso_psicologo.csv", index=False)
        st.success("Progreso guardado con éxito.")

# Columna 2: Mostrar tabla del funnel
with col2:
    st.header("Estado Actual del Funnel")
    st.dataframe(df)

# Columna 3: Visualización del funnel
with col3:
    st.header("Visualización del Funnel")
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.barh(df["Etapa"], df["Progreso Real"], color='#FB6F92', label='Progreso Real')
    ax.barh(df["Etapa"], df["Objetivo Semanal"], color='#FFC2D1', alpha=0.5, label='Objetivo Semanal')
    ax.set_xlabel("Cantidad")
    ax.set_ylabel("Etapa")
    ax.set_title("Funnel de Actividades")
    ax.legend()
    st.pyplot(fig)
