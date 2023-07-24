import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image

model= pickle.load(open('egb.pkl','rb'))

def run():
    menu = ['Home','Bankruptcy Prediction App']
    choice= st.sidebar.selectbox('Menu',menu)
    if choice== 'Home':
      st.title("Corporate Bankruptcy")
      st.header('What is Bankruptcy?')
      st.write('Bankruptcy is the inability of a person or a buusiness to pay their debt.')
      st.write('It involves the sale of property and some other arrangement to pay as mush as possible of the ,oney of a person or business entity owe.')
      st.write('Bankruptcy is a legal proceeding involving a person or business that is unable to repay their outstanding debts.')
      st.write(' The bankruptcy process begins with a petition filed by the debtor, which is most common, or on behalf of creditors,which is less common.')
      st.write('All of the debtors assets are measured and evaluated, and the assets may be used to repay a portion of outstanding debt.')
      st.subheader('About the Machine Learning Model and Developer')
      st.markdown('''### Model Algorithm : Random Forest Classifier''')
      st.markdown('''### Model Accuracy: 94.5746%''')
      st.markdown('''## Model Developed by Karan Singh Thakur, Ridhhi Aggarwal''')
      st.markdown('''### contact: kthakur1_be20@thapar.edu, raggarwal1_be20@thapar.edu''')
      
    elif choice== 'Bankruptcy Prediction App':
      st.title("Corporate Bankruptcy prediction Model")
      st.subheader("This model will predict if a company would Bankrupt in future or not")
      #Company Name:
      comp_name= st.text_input('Company Name')
    # [(cash + short-term securities + receivables - short-term liabilities) / (operating expenses - depreciation)] 365
      attr5= st.number_input(' [(cash + short-term securities + receivables - short-term liabilities) / (operating expenses - depreciation)] 365')
    #(gross profit + depreciation) / sales
      attr13= st.number_input('(gross profit + depreciation) / sales')
    #(inventory * 365) / sales
      attr20= st.number_input('(inventory * 365) / sales')
    #profit on operating activities / total assets
      attr22= st.number_input('profit on operating activities / total assets')
    #gross profit (in 3 years) / total assets
      attr24=st.number_input('gross profit (in 3 years) / total assets')
    #profit on operating activities / financial expenses
      attr27= st.number_input('profit on operating activities / financial expenses')
    #logarithm of total assets
      attr29= st.number_input('logarithm of total assets')
    #operating expenses / total liabilities
      attr34= st.number_input('operating expenses / total liabilities')
    #(current assets - inventory - receivables) / short-term liabilities
      attr40= st.number_input('(current assets - inventory - receivables) / short-term liabilities')
    #(receivables * 365) / sales
      attr44= st.number_input('(receivables * 365) / sales')
    #(current assets - inventory) / short-term liabilities
      attr46= st.number_input('(current assets - inventory) / short-term liabilities')
    #total costs /total sales
      attr58= st.number_input('total costs /total sales')
    #''Attr5', 'Attr13', 'Attr20', 'Attr22', 'Attr24', 'Attr27', 'Attr29',
       #'Attr34', 'Attr40', 'Attr44', 'Attr46', 'Attr58
      features= [[attr5,attr13,attr20,attr22,attr24,attr27,
                attr29,attr34,attr40,attr44,attr46,attr58 ]]
      print(features)
      ans = y = model.predict(features)
      if st.button("Predict"):
        if ans == 0:
          st.warning("Your Company " + comp_name + ' is in low risk for bankruptcy.')
        else:
          st.success("Your Company " + comp_name + ' is in high risk for bankruptcy.')

if __name__ == "__main__":
  run()
