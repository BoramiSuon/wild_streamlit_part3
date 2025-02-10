import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Données utilisateurs
lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()
authentication_status = st.session_state.get("authentication_status", None)
if authentication_status:
    with st.sidebar:
        st.title("📌 Navigation")
        selection = option_menu(
            menu_title=None,
            options=["Accueil", "Les photos de mon chat"],
            default_index=0,
            styles={
                "container": {"padding": "10px", "background-color": "#f0f2f6"},
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "5px",
                    "padding": "10px",
                    "border-radius": "5px",
                    "color": "black",  
                },
                "nav-link-selected": {
                    "background-color": "#ffcc00",  
                    "color": "black",  
                    "font-weight": "bold",
                },
            }
        )
    def accueil():
        st.title("MOUAHAH TU ES RENTRE DANS LE MORDOR DES CHATS TROP TROP CUTE”")
        st.image("https://media.tenor.com/cVdLW-0baz0AAAAM/cats-chat.gif", use_container_width=True)

    if selection == "Accueil":
        accueil()
    elif selection == "Les photos de mon chat":
        st.title("🐱 Les photos de mon chat")
        cols = st.columns(3)
        images = [
            "https://www.photofunky.net/output/image/c/4/d/f/c4dfd3/photofunky.gif",
            "https://i.pinimg.com/originals/b1/e3/51/b1e3512516c438ff0a9c01eae1944b02.gif",
            "https://static.mmzstatic.com/wp-content/uploads/2014/03/myope-chat.gif"
        ]
        for i, col in enumerate(cols):
            col.image(images[i], use_container_width=True)  

    authenticator.logout("Déconnexion", "sidebar")

elif authentication_status is False:
    st.error("L'username ou le password est incorrect")
elif authentication_status is None:
    st.warning("Les champs username et mot de passe doivent être remplis")
