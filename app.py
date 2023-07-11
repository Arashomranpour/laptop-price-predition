import streamlit as st
import pickle
import pandas as pd
import numpy as np
pipe=pickle.load(open("pipe1.pkl","rb"))
df=pickle.load(open("df.pkl","rb"))
# print(df.columns)


st.title("Laptop price prediction")

company=st.selectbox("Brand",df["Company"].unique())
type=st.selectbox("Type",df["TypeName"].unique())
Inches=st.selectbox("Inches",sorted(df["Inches"].unique()))
Resolution=st.selectbox("Resolution",df["Resolution"].unique())
ram=st.selectbox("Ram",sorted(df["Ram"].unique()))
weight=st.selectbox("Weight",df["Weight"].unique())
ts=st.selectbox("TouchScreen",["No", "Yes"])
ips=st.selectbox("Ips",["No", "Yes"])
Cpu=st.selectbox("Cpu",df["Cpu brand"].unique())
HDD=st.selectbox("HDD",sorted(df["HDD"].unique()))
SSD=st.selectbox("SSD",sorted(df["SDD"].unique()))
Gpu=st.selectbox("Gpu",df["gpu brand"].unique())
os=st.selectbox("os",df["os"].unique())


if st.button("Predict Price",type="secondary"):
    # query
    if ts=="Yes":
        ts=1
    else: ts=0
    
    if ips=="Yes":
        ips=1
    else: ips=0
    query=np.array([company,type,Inches,Resolution,ram,weight,ts,ips,Cpu,HDD,SSD,Gpu,os])
    query=query.reshape(1,len(query))
    st.title("Prediction : "+str(int(np.exp(pipe.predict(query)[0]))))