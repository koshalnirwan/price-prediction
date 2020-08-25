import streamlit as st
import pickle
import numpy as np

st.text('@author: koshal ')
#st.title("*PROPERTY PRICE PREDICTION MODEL*")
html = """
<div style='background-color:tomato;padding:10px'>
<h2 style='color:white;text-align:center;'><b>PROPERTY PRICE PREDICTION MODEL</b> </h2>
</div>
"""
st.markdown(html, unsafe_allow_html=True)
st.subheader('')
st.subheader('*Select Location*')

html2 = """ 
<h3 style="color:grey"><b><i>'Property Price Prediction Model is a web application \
developed using Machine Learning. It is based on Linear Regression Algorithm \
of Supervised Learning. The Model is trained on more than "10000" records'
</h3>"""

st.sidebar.header('ABOUT')
st.sidebar.markdown(html2, unsafe_allow_html=True)

#@st.cache
pickle1 = open('model.pickle','rb')
regressor = pickle.load(pickle1)

#@st.cache
pickle2 = open('dicti.pickle','rb')
dicti = pickle.load(pickle2)

#@st.cache
pickle3 = open('X1.pickle','rb')
X1 = pickle.load(pickle3)

a = st.selectbox('', dicti)

st.subheader('*Provide Area in Sq. Ft.*')
b = st.number_input('  ', value=400, min_value=300, max_value=10000 )

st.subheader('*Enter no. of bathrooms*')
c = st.number_input('',value=1, min_value=1, max_value=20)

st.subheader('*Enter no. of bedrooms*')
d = st.number_input(' ',value=1, min_value=1, max_value=20)

def predict_price(location,sqft,bath,bhk):
    loc_index = np.where(X1.columns == location)[0]
    
    x = np.zeros(len(X1.columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    st.text_input('', f"The Price is almost  {'{:.2f}'.format(abs(regressor.predict([x])[0]))}  {'Lakh Rupees'}")

but = st.button('PREDICT')         
if but:
    predict_price(a,b,c,d)
         
