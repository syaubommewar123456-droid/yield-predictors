import streamlit as st
import pandas as pd
import pickle
# Load the trained pipeline (make sure you save it beforehand)
pipeline = pickle.load(open('pipeline.pkl','rb'))

# Assuming your predict_crop_yield function
def predict_crop_yield(pipeline, area, item, year, average_rain_fall_mm_per_year, pesticides_tonnes, avg_temp):
    input_data = pd.DataFrame({
        'Area': [area],
        'Item': [item],
        'Year': [year],
        'average_rain_fall_mm_per_year': [average_rain_fall_mm_per_year],
        'pesticides_tonnes': [pesticides_tonnes],
        'avg_temp': [avg_temp]
    })
    prediction = pipeline.predict(input_data)
    return prediction[0]

# Streamlit app
def main():
    st.title("🌾 Crop Yield Prediction App")
    st.write("Predict crop yield based on environmental and agricultural factors.")

    # Input fields
    area = st.text_input('Area', 'Albania')
    item = st.text_input('Crop Item', 'Maize')
    year = st.number_input('Year', min_value=1900, max_value=2100, value=2025)
    average_rain_fall_mm_per_year = st.number_input('Average Rainfall (mm/year)', value=1500.0)
    pesticides_tonnes = st.number_input('Pesticides (tonnes)', value=130.0)
    avg_temp = st.number_input('Average Temperature (°C)', value=17.5)

    if st.button('Predict Crop Yield'):
        predicted_yield = predict_crop_yield(
            pipeline,
            area,
            item,
            year,
            average_rain_fall_mm_per_year,
            pesticides_tonnes,
            avg_temp
        )
        st.success(f"🌾 Predicted Crop Yield: **{predicted_yield:.2f} hg/ha**")

if __name__ == "__main__":
    main()
