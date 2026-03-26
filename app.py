# import streamlit as st 
# import pickle
# import pandas as pd

# def recommend(movie):
#     movie_index = movies[movies['original_title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
#     recommended_movies= []
#     for i in movies_list:
#         recommended_movies.append(movies.iloc[i[0]].original_title)

#     return recommended_movies


# movies_dict = pickle.load(open('movies_dict.pkl','rb'))
# movies  = pd.DataFrame(movies_dict)

# similarity=  pickle.load(open('similarity.pkl','rb'))
# st.title('Movie Recommender System')


# options= st.selectbox(
#     'choose a movie',movies['original_title'].values
# )

# if st.button('recommend'):
#     recommendations = recommend(options)
#     for i in recommendations:
#         st.write(i)

# import streamlit as st 
# import pickle
# import pandas as pd
# import requests

# def fetch_poster(movie_id):
#   """
#   Fetches the poster URL for a given movie ID from The Movie Database (TMDB).

#   Args:
#     movie_id (int): The unique ID of the movie on TMDB.

#   Returns:
#     str: The URL of the movie poster, or an empty string if not found.
#   """
#   api_key = "d35be676b682a821d70142b9f230e622"
  
#   url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
  
#   try:
#     response = requests.get(url)
#     response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
    
#     data = response.json()
    
#     if 'poster_path' in data and data['poster_path']:
#       return f"https://image.tmdb.org/t/p/w500/{data['poster_path']}"
#     else:
#       return ""
      
#   except requests.exceptions.RequestException as e:
#     print(f"Error fetching data: {e}")
#     return ""
#   except KeyError:
#     print(f"KeyError: 'poster_path' not found for movie ID {movie_id}")
#     return ""

# def recommend(movie):
#   """
#   Finds the 5 most similar movies based on a given movie title and returns 
#   a list of recommended movie names and a list of their posters.
#   """
#   index = movies[movies['original_title'] == movie].index[0]
#   distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
  
#   recommended_movie_names = []
#   recommended_movie_posters = []
#   for i in distances[1:6]:
#       movie_id = movies.iloc[i[0]].movie_id
#       recommended_movie_posters.append(fetch_poster(movie_id))
#       recommended_movie_names.append(movies.iloc[i[0]].original_title)

#   return recommended_movie_names, recommended_movie_posters

# # --- Load Data and Setup Streamlit UI ---
# movies = pickle.load(open('movies_dict.pkl','rb'))
# movies = pd.DataFrame(movies)

# similarity = pickle.load(open('similarity.pkl','rb'))

# st.header('Movie Recommender System')

# movie_list = movies['original_title'].values
# selected_movie = st.selectbox(
#     "Type or select a movie from the dropdown",
#     movie_list
# )

# if st.button('Show Recommendation'):
#     recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    
#     # Use st.columns instead of the deprecated st.beta_columns
#     col1, col2, col3, col4, col5 = st.columns(5)
    
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0])
#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1])
#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2])
#     with col4:
#         st.text(recommended_movie_names[3])
#         st.image(recommended_movie_posters[3])
#     with col5:
#         st.text(recommended_movie_names[4])
#         st.image(recommended_movie_posters[4])


import pickle
import streamlit as st
import requests

API_KEY = "d35be676b682a821d70142b9f230e622"

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # will raise error if response != 200
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

# def fetch_poster(movie_id):
#     api_key = "d35be676b682a821d70142b9f230e622"  # your key
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
#     response = requests.get(url, timeout=10)
#     data = response.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path

# def fetch_poster(movie_id):
#     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
#     data = requests.get(url)
#     data = data.json()
#     poster_path = data['poster_path']
#     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#     return full_path
# import pickle
# import streamlit as st
# import requests

# API_KEY = "56ab7d19d5351ad7f66c6ade3aed8add"  # your new TMDB API key

# def fetch_poster(movie_id):
#     url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
#     response = requests.get(url, timeout=10)
#     response.raise_for_status()  # will raise error if response != 200
#     data = response.json()
#     poster_path = data.get('poster_path')
#     if poster_path:
#         full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
#         return full_path
#     return None  # return None if no poster found

# def recommend(movie):
#     index = movies[movies['original_title'] == movie].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_movie_names = []
#     recommended_movie_posters = []
#     for i in distances[1:6]:
#         # fetch the movie poster
#         movie_id = movies.iloc[i[0]].id   # ✅ keep 'id' since that’s your column
#         recommended_movie_posters.append(fetch_poster(movie_id))
#         recommended_movie_names.append(movies.iloc[i[0]].original_title)

#     return recommended_movie_names, recommended_movie_posters


# st.header('Movie Recommender System')
# movies = pickle.load(open('movies.pkl', 'rb'))
# similarity = pickle.load(open('similarity.pkl', 'rb'))

# movie_list = movies['original_title'].values
# selected_movie = st.selectbox(
#     "Type or select a movie from the dropdown",
#     movie_list
# )

# if st.button('Show Recommendation'):
#     recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#         st.text(recommended_movie_names[0])
#         st.image(recommended_movie_posters[0])
#     with col2:
#         st.text(recommended_movie_names[1])
#         st.image(recommended_movie_posters[1])
#     with col3:
#         st.text(recommended_movie_names[2])
#         st.image(recommended_movie_posters[2])
#     with col4:
#         st.text(recommended_movie_names[3])
#         st.image(recommended_movie_posters[3])
#     with col5:
#         st.text(recommended_movie_names[4])
#         st.image(recommended_movie_posters[4])

import pickle
import streamlit as st
import requests, time

API_KEY = "56ab7d19d5351ad7f66c6ade3aed8add"  # your TMDB API key
FALLBACK_POSTER = "https://via.placeholder.com/500x750?text=No+Poster"

def safe_request(url, retries=3, delay=2):
    """Retry request a few times before failing."""
    for i in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException:
            if i < retries - 1:
                time.sleep(delay)
            else:
                return None

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = safe_request(url)
    if not response:  # if request failed completely
        return FALLBACK_POSTER

    data = response.json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    return FALLBACK_POSTER

def recommend(movie):
    index = movies[movies['original_title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].id  # ✅ correct column
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].original_title)
    return recommended_movie_names, recommended_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movie_list = movies['original_title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(recommended_movie_names[idx])
            st.image(recommended_movie_posters[idx])
