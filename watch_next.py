# This program reads a movies.txt file and provides a recommendation of a movie to watch based on the previous watched
# movie - Planet Hulk

# import spacy
import spacy

# specifying the model we want to use
nlp = spacy.load('en_core_web_md')


# next_movie function takes in the description as a parameter
# it opens and reads the movies.txt file
# empty movie_list is created to store the movie list
def next_movie(description):
    movies = open("movies.txt", "r")
    movie_list = []

    # for loop splits movies at : and appends the data with movie name and description into movie_list
    for movie in movies:
        movie_list.append(movie.split(':'))

    # variables created for the number of objects in movie list, a similar list and model_sentence
    # model_sentence calls the nlp function as previously defined takes the description as an argument
    movie_count = len(movie_list)
    similarity_list = []
    model_sentence = nlp(description)

    # for loop runs for each movie in the txt file
    # similar movie information is appended into the similarity list based on the movie description and the recently watched movie
    # the maximum similarity is called by using max(similarity_list)
    # the index of the movie with the maximum similarity is created and stored as  a variable
    # information is returned
    for movie in range(0, movie_count):
        similarity_list.append(nlp(movie_list[movie][1]).similarity(model_sentence))

    max_similarity = max(similarity_list)
    max_similarity_index = similarity_list.index(max_similarity)

    return movie_list[max_similarity_index][0]

# description of movie
planet_hulk_description = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""


# next_movie function is called
print("Based on the previous movie that you have seen, the next movie for you to watch is: " + next_movie(planet_hulk_description))