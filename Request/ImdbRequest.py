import requests
import Request
from Request import constant

class ImdbRequest:
    
    _id_url = "https://imdb-api.com/en/API/Search/"+ constant.API_KEY +'/'
    _content_url = "https://imdb-api.com/en/API/Title/"+ constant.API_KEY +'/'


    @classmethod
    def get_info(cls,movie_name):
        print(movie_name)
        if movie_name != None:

            id = requests.get(cls._id_url+movie_name).json()['results'][0]['id']
            response = requests.get(cls._content_url+id)
            if response.status_code != 200:
                raise Exception('We encountered a problem calling IMDB API')
            else :
                return Request.Response(response.status_code,response.json())
        

    def get_poster(clc,movie_info):

        poster = movie_info.content['image']

        return poster
    

    def get_genres(clc,movie_info):

        genres = movie_info.content['genres']

        return genres

    
    def get_plot(clc,movie_info):

        plot = movie_info.content['plot']

        return plot

    
    def get_rating(clc,movie_info):

        rating = movie_info.content['imDbRating']

        return rating

    
    def get_topActors(clc,movie_info):

        topImages= []
        topActors =[]

        for actor in movie_info.content['starList']:
            topActors.append(actor['name'])

        for images in movie_info.content['actorList']:
            if images['name'] in topActors:
                topImages.append(images['image'])
                topActors = movie_info.content['image']

        return topActors, topImages
        
