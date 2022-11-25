import streamlit as st
from Request.Imdb_Request import ImdbRequest
from Request.Response import Response



st.markdown("# **Do I Watch this Movie ?**")
st.markdown("## **THE** reference when you want to know more about a movie!")


title = st.text_input(
    label="Movie Name",
    placeholder="Enter the name of the movie",
    label_visibility="hidden",
)

with st.spinner('Nous recherchons votre film, ne bougez pas...'):
  
    if len(title) > 0 and not title.isspace():
        my_movie_info = ImdbRequest.get_movie_info(title)

        if my_movie_info != 'HTTPError':

            my_movie_id = ImdbRequest.get_movie_id(my_movie_info)

            if  isinstance(my_movie_id,Response):
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
            else :
                st.error("Oups we didn't find your movie")
