import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the Streamlit app
st.title("Attendance Forecasting for Modules - Starting October 2024")

# Load the forecasted data
@st.cache_data  # Cache data to avoid reloading on each interaction
def load_data():
    # Load forecast data from CSV (ensure the file path is correct)
    return pd.read_csv("attendance_forecast_per_module.csv")

# Load the data
df_forecast = load_data()

# Sidebar: Select a module to view its forecast
module = st.sidebar.selectbox("Select Module", df_forecast['module'].unique())

# Filter the data for the selected module
df_selected_module = df_forecast[df_forecast['module'] == module]

# Display the dataframe in the Streamlit app
st.subheader(f"Forecasted Attendance for {module}")
st.write(df_selected_module)

# Plotting the forecasted data
st.subheader(f"Attendance Forecast Plot for {module}")

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(df_selected_module['ds'], df_selected_module['yhat'], label=f'Forecasted Attendance for {module}', color='blue')
plt.xlabel('Date')
plt.ylabel('Attendance')
plt.title(f'Forecasted Attendance for {module} from October 2024')
plt.legend()
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(plt)

# Optionally, let users download the forecast data
st.subheader("Download Forecast Data")
st.download_button(
    label="Download Forecast CSV",
    data=df_forecast.to_csv().encode('utf-8'),
    file_name='attendance_forecast_per_module.csv',
    mime='text/csv'
)
