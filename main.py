
import streamlit as st
from Request.ImdbRequest import ImdbRequest


st.markdown("# **Welcome to** Do I Watch this Movie ?")
st.write("## **THE** reference when you want to know more about a movie!")

title = st.text_input(label = 'Movie Name',placeholder='Enter the name of the movie',label_visibility='hidden')

my_movie_info = ImdbRequest.get_info(title)

if my_movie_info != 404:
    st.image(my_movie_info.get_poster())
    st.markdown(my_movie_info.get_genres())
    st.markdown(my_movie_info.get_plot())

    st.markdown('## Rating ')
    st.markdown('### '+ str(my_movie_info.get_rating()) +'/10')

    st.markdown('## Top Actors')
    actors ,images = my_movie_info.get_top_actors()
    st.image(images,width = 230,caption=actors)
else :
    st.markdown('## Ouuuups it seems that your movie is unaivalable')





