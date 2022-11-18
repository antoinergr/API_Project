class Response:
    def __init__(self, status_code, content):
        self.status_code = status_code
        self.content = content


    def get_poster(self):

        poster = self.content['image']

        return poster
    

    def get_genres(self):

        genres = self.content['genres']

        return genres

    
    def get_plot(self):

        plot = self.content['plot']

        return plot

    
    def get_rating(self):

        rating = self.content['imDbRating']

        return rating

    
    def get_top_actors(self):

        topImages= []
        topActors =[]

        for actor in self.content['starList']:
            topActors.append(actor['name'])

        for images in self.content['actorList']:
            if images['name'] in topActors:
                topImages.append(images['image'])


        return topActors, topImages