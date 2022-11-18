
import streamlit as st
import json
import Request


#f = open("./data.json")
#my_movie_info = json.load(f)

st.markdown("# **Welcome to** Do I Watch this Movie ?")
st.write("## **THE** reference when you want to know more about a movie!")

title = st.text_input(label = 'Movie Name',placeholder='Enter the name of the movie',label_visibility='hidden')

my_movie_info = Request.ImdbRequest.get_info(title)

st.image(my_movie_info.get_poster())
st.markdown(my_movie_info.get_genres())
st.markdown(my_movie_info.get_plot())

st.markdown('## Rating ')
st.markdown('### '+ str(my_movie_info.get_rating()) +'/10')

st.markdown('## Top Actors')
actors ,images = my_movie_info.get_topActors()
st.image(images,width = 230,caption=actors)





