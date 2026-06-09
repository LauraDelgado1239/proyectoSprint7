# Anuncios de Venta de Coches en EE. UU.

Aplicación web interactiva para explorar el conjunto de datos de anuncios de venta de coches usados en Estados Unidos.

## Descripción

La aplicación permite al usuario visualizar dos aspectos del conjunto de datos mediante casillas de verificación:

- **Histograma del odómetro**: muestra la distribución del kilometraje de los vehículos anunciados.
- **Gráfico de dispersión (odómetro vs precio)**: permite explorar la relación entre el kilometraje y el precio de venta de los vehículos.

El análisis exploratorio de datos completo se encuentra en el notebook `notebooks/EDA.ipynb`.

## Tecnologías utilizadas

- Python
- Pandas
- Plotly
- Streamlit

## Cómo ejecutar la aplicación

1. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

2. Ejecuta la aplicación:
   ```
   streamlit run app.py
   ```

3. Abre el navegador en `http://localhost:8501`
