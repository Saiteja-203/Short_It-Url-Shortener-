import streamlit as st
import pyshorteners as pys
import pyperclip
shortener=pys.Shortener()
def copying():
    pyperclip.copy(shortened.replace(custom_tag,'tinyurl.com'))
st.markdown("<h1 style='text-align:center;'>SHORT IT</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;'>A URL SHORTENER</h2>", unsafe_allow_html=True)

form=st.form('URL')

url=form.text_input('URL Here.....')

custom_tag=form.text_input('Custom Tag here...')

s_btn=form.form_submit_button('Shorten..')

if s_btn:
    shortened=shortener.tinyurl.short(url)
    shortened=shortened.replace('tinyurl.com',custom_tag)
    st.markdown('<br>',unsafe_allow_html=True)
    st.markdown('<h3>Shorted Url</h3>',unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align:center'>{shortened}</h5>", unsafe_allow_html=True)
    st.button('Copy',on_click=copying)

