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
                           ['Diabetes Prediction'],
                           
                           icons = ['activity'],
                           
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


