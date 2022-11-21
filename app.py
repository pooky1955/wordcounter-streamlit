#!/usr/bin/python3
import streamlit as st
import sys
import re
import clipboard as c


st.write("# Word Counter Excluding Quotations and Citations!")
input_text = st.text_input("Enter your text to count without words and quotes")
quotes_patt = re.compile('\"[^\"]*\"')
parent_patt = re.compile('\([^)]*\)')
without_quotations = quotes_patt.sub('',input_text)
cleaned_text = parent_patt.sub('',without_quotations)

words = len(cleaned_text.split())
st.write(f"Words: {words}")
st.write(f"Resulting text:\n{cleaned_text}")
