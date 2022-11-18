import requests
from Request.Response import Response
from Request import constant

class ImdbRequest:
    
    _id_url = "https://imdb-api.com/en/API/Search/"+ constant.API_KEY +'/'
    _content_url = "https://imdb-api.com/en/API/Title/"+ constant.API_KEY +'/'


    @classmethod
    def get_info(cls,movie_name):

        if not isinstance(movie_name,type(None)):

            get_id = requests.get(cls._id_url+movie_name).json()
            
            if  not isinstance(get_id['results'],type(None)) and not not get_id['results'] :
                id = get_id['results'][0]['id']
                response = requests.get(cls._content_url+id)

                if response.status_code != 200:
                    raise Exception('We encountered a problem calling IMDB API')
                else :
                    return Response(response.status_code,response.json())
            else :
                return 404
        
        
