import requests
from Request.Response import Response
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')

class ImdbRequest:

    _id_url = "https://imdb-api.com/en/API/Search/" + API_KEY + "/"
    _content_url = "https://imdb-api.com/en/API/Title/" + API_KEY + "/"


    @classmethod
    def get_movie_info(cls, movie_name):

        try :
            get_id= requests.get(cls._id_url + movie_name)
            get_id.raise_for_status()
        except requests.exceptions.HTTPError:
            return 'HTTPError'
        
        else : 
            return Response(get_id.status_code, get_id.json())

    @classmethod
    def get_movie_id(cls, movie_info):
        try :
                get_id= requests.get(cls._content_url + movie_info.content["results"][0]["id"] + "/Trailer")
                get_id.raise_for_status()

        except requests.exceptions.HTTPError:
            return 'HTTPError'

        except TypeError:
            return 'NoneType Error'

        except IndexError:
            return 'IndexError'

        else :
            return Response(get_id.status_code, get_id.json())
    

