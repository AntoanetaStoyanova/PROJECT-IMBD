import streamlit as st
import requests

st.title("Prédiction de note IMDB de film")

# Entrée des données du film
features = {
    'num_critic_for_reviews': st.number_input("Nombre de critiques pour avis", min_value=0, format='%d'),
    'director_fb_likes': st.number_input("Likes Facebook du réalisateur", min_value=0, format='%d'),
    'cast_total_fb_likes': st.number_input("Likes Facebook du casting total", min_value=0, format='%d'),
    'gross': st.number_input("Recettes brutes", min_value=0, format='%d'),
    'num_user_for_reviews': st.number_input("Nombre d'avis d'utilisateurs", min_value=0, format='%d'),
    'budget': st.number_input("Budget", min_value=0, format='%d'),
    'duration': st.number_input("Durée (en minutes)", min_value=0, format='%d'),
    'title_year': st.number_input("Année de sortie", min_value=1900, max_value=2024, format='%d'),
    'movie_fb_likes': st.number_input("Likes Facebook du film", min_value=0, format='%d')
}

if st.button("Prédire"):
    # Envoyer la requête à l'API Flask
    response = requests.post('http://localhost:5000/predict', json=features)
    
    if response.status_code == 200:
        prediction = response.json()['prediction']
        st.write(f"La prédiction de note IMDB est : {prediction}")
    else:
        st.write("Une erreur est survenue lors de la prédiction.")

