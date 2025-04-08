# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 16:54:55 2025
@author: parit
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction'],
        icons=['activity', 'heart-pulse-fill'],
        default_index=0
    )

# ----------------------- Diabetes Prediction Page ----------------------- #
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    # Input Fields
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''

    if st.button('Diabetes Test Result'):
        try:
            input_data = [[
                int(Pregnancies), float(Glucose), float(BloodPressure), float(SkinThickness),
                float(Insulin), float(BMI), float(DiabetesPedigreeFunction), int(Age)
            ]]

            diab_prediction = diabetes_model.predict(input_data)

            if diab_prediction[0] == 1:
                diab_diagnosis = '✅ The person **is diabetic**.'
            else:
                diab_diagnosis = '✅ The person **is not diabetic**.'

        except ValueError:
            st.error("⚠️ Please enter **valid numeric values** in all fields.")
        except Exception as e:
            st.error(f"🚨 An error occurred: {e}")

        st.success(diab_diagnosis)

# ----------------------- Heart Disease Prediction Page ----------------------- #
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex (1 = Male, 0 = Female)')

    with col3:
        cp = st.text_input('Chest Pain Type (0–3)')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholesterol (mg/dl)')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)')

    with col1:
        restecg = st.text_input('Resting ECG Results (0–2)')

    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina (1 = Yes, 0 = No)')

    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise')

    with col2:
        slope = st.text_input('Slope of the Peak Exercise ST Segment')

    with col3:
        ca = st.text_input('Major Vessels Colored by Flourosopy (0–3)')

    with col1:
        thal = st.text_input('Thal (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)')

    heart_diagnosis = ''

    if st.button('Heart Disease Result'):
        try:
            input_data = [[
                int(age), int(sex), int(cp), float(trestbps), float(chol),
                int(fbs), int(restecg), int(thalach), int(exang),
                float(oldpeak), int(slope), int(ca), int(thal)
            ]]

            heart_prediction = heart_disease_model.predict(input_data)

            if heart_prediction[0] == 1:
                heart_diagnosis = '❤️ The person **has heart disease**.'
            else:
                heart_diagnosis = '💓 The person **does not have heart disease**.'

        except ValueError:
            st.error("⚠️ Please enter **valid numeric values** in all fields.")
        except Exception as e:
            st.error(f"🚨 An error occurred: {e}")

        st.success(heart_diagnosis)
