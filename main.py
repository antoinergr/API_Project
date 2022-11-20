import streamlit as st
from Request.Imdb_Request import ImdbRequest


st.markdown("# **Welcome to** Do I Watch this Movie ?")
st.write("## **THE** reference when you want to know more about a movie!")

title = st.text_input(
    label="Movie Name",
    placeholder="Enter the name of the movie",
    label_visibility="hidden",
)

my_movie_info = ImdbRequest.get_movie_info(title)

if my_movie_info != 'HTTPError':

    my_movie_id = ImdbRequest.get_movie_id(my_movie_info)

    if my_movie_id not in ['HTTPError','Unavailable']:
        st.image(my_movie_id.get_poster())
        st.markdown('## Types')
        st.markdown('### ' + my_movie_id.get_genres())
        st.markdown('## Plot')
        st.markdown('### ' + my_movie_id.get_plot())

        st.markdown("## Rating ")
        st.markdown("### " + str(my_movie_id.get_rating()) + "/10")

        st.markdown("## Top Actors")
        actors, images = my_movie_id.get_top_actors()
        st.image(images, width=230, caption=actors)
    else:
        st.markdown("## Enter the movie name or check the name you just entered")
