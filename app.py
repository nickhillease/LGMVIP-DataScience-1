import streamlit as st
import joblib
#loading the model
model_filename=r'decTree.joblib'
saved_model=joblib.load(model_filename)


st.title('Iris Flowers Classification ')
sepal_length = st.number_input('Enter Sepal Length:')
sepal_width = st.number_input('Enter Sepal Width:')
petal_length = st.number_input('Enter Petal Length:')
petal_width = st.number_input('Enter Petal Width:')

# Sepal length,Sepal Width,Petal Length,Petal Width
if st.button('Predict'):
     features=np.array([sepal_length, sepal_width, petal_length, petal_width])
     prediction=saved_model.predict(features)

     if prediction==0:
          st.write('The given flower is Iris Setosa')
     elif prediction==1:
          st.write("The given flower is Iris Versicolor")
     elif prediction==2:
          st.write('The given flower is Iris Virginica')
     else:
          st.write('Invalid Prediction')
     
     
