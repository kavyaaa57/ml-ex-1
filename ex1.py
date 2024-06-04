import streamlit as st
import numpy as np
import pandas as pd

def load_data():
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        return data
    return None

def learn(concepts, target):
    specific_h = concepts[0].copy()
    general_h = [["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    
    for i, h in enumerate(concepts):
        if target[i] == "Yes":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    specific_h[x] = '?'
                    general_h[x][x] = '?'
        if target[i] == "No":
            for x in range(len(specific_h)):
                if h[x] != specific_h[x]:
                    general_h[x][x] = specific_h[x]
                else:
                    general_h[x][x] = '?'
    
    indices = [i for i, val in enumerate(general_h) if val == ['?', '?', '?', '?', '?', '?']]
    for i in indices:
        general_h.remove(['?', '?', '?', '?', '?', '?'])
    
    return specific_h, general_h

st.title('Candidate Elimination Algorithm')

data = load_data()

if data is not None:
    st.write("Dataset:")
    st.write(data)
    
    concepts = np.array(data.iloc[:, 0:-1])
    target = np.array(data.iloc[:, -1])
    
    s_final, g_final = learn(concepts, target)
    
    st.write("\nFinal Specific Hypothesis:", s_final)
    st.write("\nFinal General Hypothesis:", g_final)

    st.write("Specific Hypothesis:")
    st.write(s_final)
    
    st.write("General Hypothesis:")
    st.write(g_final)
else:
    st.write("Please upload a CSV file.")
