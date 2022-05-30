import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

st.write("""
# Title
Hello
""")


df = pd.DataFrame(np.random.randn(200,3),
        columns=['a','b','c'])

c = alt.Chart(df).mark_circle().encode(
        x='a',y='b',size='c',tooltip=['a','b','c'])

st.altair_chart(c, use_container_width=True)


slid = st.slider("slide",0.0,1.0,.5)

x = np.arange(100)
source = pd.DataFrame({
    'x':x,
    'f(x)':np.sin(x/5)*slid 
    })

d = alt.Chart(source).mark_line().encode(
        x='x',
        y='f(x)'
        )
st.altair_chart(d,use_container_width=True)
