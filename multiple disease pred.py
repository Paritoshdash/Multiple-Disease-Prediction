# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 16:54:55 2025

@author: parit
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav' , 'rb'))

heart_model = pickle.load(open('heart_disease_model.sav' , 'rb'))




# sidebar for navigate

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           
                           icons = ['activity','heart-pulse-fill','person'],
                           
                           default_index = 0)
    

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    #page site
    st.title('Diabetes Prediction using ML')
    
    # getting the input data from user
    #coulmns for input fields
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

    
    
    #code for prediction
    diab_dignosis = ''
    
    #creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0]==1):
            diab_dignosis = 'The Person Is Diabetic'
        else:
            diab_dignosis = 'The Person Is Not Diabetic'
    
    st.success(diab_dignosis)


# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    #page site
    st.title('Heart Disease Prediction using ML')
    
    
    # getting the input data from user
    #coulmns for input fields
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    
    
    #code for prediction
    heart_dignosis = ''
    
    #creating a button for prediction
    
    if st.button('Heart Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (heart_prediction[0]==1):
            heart_dignosis = 'The person is having heart disease'
        else:
            heart_dignosis = 'The person does not have any heart disease'
    
    st.success(heart_dignosis)

# Parkinsons Prediction Page 
if (selected == 'Parkinsons Prediction'):
    
    #page site
    st.title('Parkinsons Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col1:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col2:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col3:
        RAP = st.text_input('MDVP:RAP')

    with col1:
        PPQ = st.text_input('MDVP:PPQ')

    with col2:
        DDP = st.text_input('Jitter:DDP')

    with col3:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col1:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col2:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col3:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col1:
        APQ = st.text_input('MDVP:APQ')

    with col2:
        DDA = st.text_input('Shimmer:DDA')

    with col3:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col1:
        spread1 = st.text_input('spread1')

    with col2:
        spread2 = st.text_input('spread2')

    with col3:
        D2 = st.text_input('D2')

    with col1:
        PPE = st.text_input('PPE')

    #code for prediction
    Parkinsons_dignosis = ''
    
    #creating a button for prediction
    
    if st.button('Heart Test Result'):
        Parkinsons_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (Parkinsons_prediction[0]==1):
            Parkinsons_dignosis = 'The person is having heart disease'
        else:
            Parkinsons_dignosis = 'The person does not have any heart disease'
    
    st.success(Parkinsons_dignosis)
    
