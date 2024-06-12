# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:05:43 2024

@author: hp
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved model

#diabetes_model= pickle.load(open('C:/Users/hp/OneDrive/Desktop/Multiple_Disease_Prediction_System/diabetes_model.sav','rb'))

#heart_disease_model= pickle.load(open('C:/Users/hp/OneDrive/Desktop/Multiple_Disease_Prediction_System/heartdisease_model.sav','rb'))

#parkinsons_model= pickle.load(open('C:/Users/hp/OneDrive/Desktop/Multiple_Disease_Prediction_System/parkinsons_model.sav','rb'))

#breast_cancer_model= pickle.load(open('C:/Users/hp/OneDrive/Desktop/Multiple_Disease_Prediction_System/breast_cancer_model.sav','rb'))

diabetes_model=pickle.load(open('diabetes_model.sav','rb'))

heart_disease_model=pickle.load(open('heartdisease_model.sav','rb'))

parkinsons_model= pickle.load(open('parkinsons_model.sav','rb'))

breast_cancer_model= pickle.load(open('breast_cancer_model.sav','rb'))



# sidebar for navigate

with st.sidebar:
    
    selected=option_menu('Multiple Disease Prediction System',
                         
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Breast Cancer Prediction',
                          'Parkinsons Prediction'
                          ],
                         
                         icons=['activity','heart','person-standing-dress','person'],
                         
                         default_index=0)
    
# Diabetes prediction page
if (selected== 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction using ML')
    
    #getting the input data from the user
    #columns for input fields
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.number_input('Number of Pregnancies',format="%.3f")
        
    with col2:
        Glucose=st.number_input('Glucose Level',format="%.3f")
        
    with col3:
        BloodPressure=st.number_input('Blood Pressure Value',format="%.3f")
        
    with col1:
        SkinThickness=st.number_input('Skin Thickness Value',format="%.3f")
        
    with col2:
        Insulin=st.number_input('Insulin Level',format="%.3f")
        
    with col3:
       BMI=st.number_input('BMI Value',format="%.3f")
       
    with col1:
       DiabetesPedigreeFunction=st.number_input('Diabetes Pedigree Function Value',format="%.3f")
       
    with col2:
       Age=st.number_input('Age of the person',format="%.3f")
    
    #code for prediction
    diab_diagnosis=''
    
    #creating a button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
        
        if(diab_prediction[0]==1):
            diab_diagnosis='The person is Diabetic'
        else:
            diab_diagnosis='The person is not Diabetic'
    
    st.success(diab_diagnosis)
    
    
# Heart Disease prediction page
if (selected== 'Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction using ML')
    
    #getting the input data from the user
    #columns for input fields
    col1,col2,col3=st.columns(3)
    
    with col1:
        age=st.number_input('Age',format="%.3f")
        
    with col2:
        sex=st.number_input('Sex',format="%.3f")
        
    with col3:
        cp=st.number_input('Chest Pain Type',format="%.3f")
        
    with col1:
        trestbps=st.number_input('Resting Blood Pressure',format="%.3f")
        
    with col2:
        chol=st.number_input('Serum Cholestoral in mg/dl',format="%.3f")
        
    with col3:
       fbs=st.number_input('Fasting Blood Sugar > 120 mg/dl',format="%.3f")
       
    with col1:
       restecg	=st.number_input('Resting Electrocardiographic Results',format="%.3f")
       
    with col2:
       thalach=st.number_input('Maximum Heart Rate achieved',format="%.3f")
       
    with col3:
          exang=st.number_input('Exercise induced angina',format="%.3f")
    
    with col1:
         oldpeak=st.number_input('ST depression induced by exercise relative to rest',format="%.3f")
     
    with col2:
         slope=st.number_input('The slope of the peak exercise ST segment',format="%.3f")
        
    with col3:
          ca=st.number_input('number of major vessels (0-3) colored by flourosopy',format="%.3f")
    
    with col1:
        thal=st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect',format="%.3f")
       
       

    #code for prediction
    heart_diagnosis=''
    
    #creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction=heart_disease_model.predict([[age,sex,cp,trestbps,chol,fbs, restecg,thalach,exang, oldpeak,slope,ca,thal]])
        
        if(heart_prediction[0]==1):
            heart_diagnosis='The person has Heart Disease'
        else:
            heart_diagnosis='The person does not have a Heart Disease'
    
    st.success(heart_diagnosis)
    
    
# Parkinsons prediction page
if (selected== 'Parkinsons Prediction'):
    
    #page title
    st.title('Parkinsons Prediction using ML')
    
    #getting the input data from the user
    #columns for input fields
    col1,col2,col3=st.columns(3)
    
    with col1:
        Fo=st.number_input('MDVP_Fo(Hz)',format="%.6f")
        
    with col2:
        Fhi=st.number_input('MDVP_Fhi(Hz)',format="%.6f")
        
    with col3:
        Flo=st.number_input('MDVP_Flo(Hz)',format="%.6f")
        
    with col1:
        Jitterperc=st.number_input('MDVP_Jitter(%)',format="%.6f")
        
    with col2:
        JitterAbs=st.number_input('MDVP_Jitter(Abs)',format="%.6f")
        
    with col3:
      RAP=st.number_input('MDVP_RAP',format="%.6f")
       
    with col1:
       PPQ	=st.number_input('MDVP_PPQ',format="%.6f")
       
    with col2:
       DDP=st.number_input('Jitter_DDP',format="%.6f")
       
    with col3:
          Shimmer=st.number_input('MDVP_Shimmer',format="%.6f")
    
    with col1:
         Shimmerdb=st.number_input('MDVP_Shimmer(dB)',format="%.6f")
     
    with col2:
         ShimmerAPQ3=st.number_input('Shimmer_APQ3',format="%.6f")
        
    with col3:
          ShimmerAPQ5=st.number_input('Shimmer_APQ5',format="%.6f")
    
    with col1:
        APQ=st.number_input('MDVP_APQ',format="%.6f")
       
    with col2:
         DDA=st.number_input('Shimmer_DDA',format="%.6f")
         
    with col3:
         NHR=st.number_input('NHR',format="%.6f")
        
    with col1:
        HNR=st.number_input('HNR',format="%.6f")
       
    with col2:
         RPDE=st.number_input('RPDE',format="%.6f")
        
    with col3:
         DFA=st.number_input('DFA',format="%.6f")
        
    with col1:
         spread1=st.number_input('spread1',format="%.6f")
        
    with col2:
         spread2=st.number_input('spread2',format="%.6f")
        
    with col3:
         D2=st.number_input('D2',format="%.6f")
        
    with col1:
         PPE=st.number_input('PPE',format="%.6f")
        
        

    #code for prediction
    parkinsons_diagnosis=''
    
    #creating a button for Prediction
    if st.button('Parkinsons Test Result'):
        parkinsons_prediction=parkinsons_model.predict([[Fo,Fhi,Flo,Jitterperc,JitterAbs,RAP,PPQ,DDP,Shimmer,Shimmerdb,ShimmerAPQ3,ShimmerAPQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        
        if(parkinsons_prediction[0]==1):
            parkinsons_diagnosis='The person has Parkinsons Disease'
        else:
            parkinsons_diagnosis='The person does not have a Parkinsons Disease'
    
    st.success(parkinsons_diagnosis)
    
    
# Breast Cancer prediction page
if (selected== 'Breast Cancer Prediction'):
    
    #page title
    st.title('Breast Cancer Prediction using ML')
    
    #getting the input data from the user
    #columns for input fields
    col1,col2,col3=st.columns(3)
    
    with col1:
        mean_radius=st.number_input('mean radius',format="%.6f")
        
    with col2:
        mean_texture=st.number_input('mean texture',format="%.6f")
        
    with col3:
        mean_perimeter=st.number_input('mean perimeter',format="%.6f")
        
    with col1:
        mean_area=st.number_input('mean area',format="%.6f")
        
    with col2:
        mean_smoothness=st.number_input('mean smoothness',format="%.6f")
        
    with col3:
         mean_compactness=st.number_input('mean compactness',format="%.6f")
       
    with col1:
        mean_concavity=st.number_input('mean concavity',format="%.6f")
       
    with col2:
         mean_concave_points=st.number_input('mean concave points',format="%.6f")
       
    with col3:
          mean_symmetry=st.number_input('mean symmetry',format="%.6f")
    
    with col1:
         mean_fractal_dimension=st.number_input('mean fractal dimension',format="%.6f")
     
    with col2:
         radius_error=st.number_input('radius error',format="%.6f")
        
    with col3:
         texture_error=st.number_input('texture error',format="%.6f")
    
    with col1:
         perimeter_error=st.number_input('perimeter error',format="%.6f")
       
    with col2:
         area_error=st.number_input('area error',format="%.6f")
         
    with col3:
         smoothness_error=st.number_input('smoothness error',format="%.6f")
        
    with col1:
         compactness_error=st.number_input('compactness error',format="%.6f")
       
    with col2:
         concavity_error=st.number_input('concavity error',format="%.6f")
        
    with col3:
         concave_points_error=st.number_input('concave points error',format="%.6f")
        
    with col1:
         symmetry_error=st.number_input('symmetry error',format="%.6f")
        
    with col2:
         fractal_dimension_error=st.number_input('fractal dimension error',format="%.6f")
        
    with col3:
         worst_radius=st.number_input('worst radius',format="%.6f")
        
    with col1:
         worst_texture=st.number_input('worst texture',format="%.6f")
         
    with col2:
         worst_perimeter=st.number_input('worst perimeter',format="%.6f")
         
    with col3:
        worst_area=st.number_input('worst area',format="%.6f")
        
    with col1:
        worst_smoothness=st.number_input('worst smoothness',format="%.6f")
        
    with col2:
         worst_compactness=st.number_input('worst compactness',format="%.6f")
       
    with col3:
         worst_concavity=st.number_input('worst concavity',format="%.6f")
       
    with col1:
         worst_concave_points=st.number_input('worst concave points',format="%.6f")
       
    with col2:
         worst_symmetry=st.number_input('worst symmetry',format="%.6f")
       
    with col3:
        worst_fractal_dimension=st.number_input('worst fractal dimension',format="%.6f")
       
        
        

    #code for prediction
    breast_cancer_diagnosis=''
    
    #creating a button for Prediction
    if st.button('Breast Cancer Test Result'):
        breast_cancer_prediction=breast_cancer_model.predict([[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,perimeter_error,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,symmetry_error,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension]])
        
        if(breast_cancer_prediction[0]==1):
            breast_cancer_diagnosis='The Breast cancer is Benign'
        else:
            breast_cancer_diagnosis='The Breast cancer is Malignant'
    
    st.success(breast_cancer_diagnosis)