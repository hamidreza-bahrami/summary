import streamlit as st
from newspaper import Article
import time
import nltk 
nltk.download('punkt')

def show_page():
    st.write("<h1 style='text-align: center; color: blue;'>مدل خلاصه ساز مقاله</h1>", unsafe_allow_html=True)
    st.write("<h2 style='text-align: center; color: gray;'>!لینک مقاله رو بده، خلاصه‌شو تحویل بگیر</h2>", unsafe_allow_html=True)
    st.write("<h4 style='text-align: center; color: gray;'>Robo-Ai.ir طراحی شده توسط</h4>", unsafe_allow_html=True)
    st.link_button("Robo-Ai بازگشت به", "https://robo-ai.ir")

    url = st.text_input('.لینک مقاله را وارد کنید')
    button = st.button('خلاصه کن')
    if button :
        with st.chat_message("assistant"):
            with st.spinner('''درحال بررسی، لطفا صبور باشید'''):
                time.sleep(3)
                st.success(u'\u2713''در حال خلاصه سازی')
                article = Article(url)
                article.download()
                article.parse()
                article.nlp()
                container = st.container(border=True)
                container.write("<h4 style='text-align: right; color: gray;'>عنوان مقاله</h4>", unsafe_allow_html=True)
                container.write(article.title)       
                container.write("<h4 style='text-align: right; color: gray;'>تاریخ انتشار مقاله</h4>", unsafe_allow_html=True)
                container.write(article.publish_date)
                container.write("<h4 style='text-align: right; color: gray;'>خلاصه مقاله</h4>", unsafe_allow_html=True)
                container.write(article.summary)
                text = article.summary
                st.download_button('دانلود خلاصه مقاله', text)

                
show_page()