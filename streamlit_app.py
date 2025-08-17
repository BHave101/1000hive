import streamlit as st 
import pathlib 

from st_social_media_links import SocialMediaIcons

# load the logo 

logo_path = "assets/comb.gif" 
st.logo(logo_path, size="large")


# Load CSS from "assets" file

def load_css(file_path): 
    with open(file_path) as f: 
        st.html(f"<style>{f.read()}</style>")

#Load the external CSS 
css_path = pathlib.Path("assets/styles.css")
load_css(css_path)



# BACKGROUND SETUP 
#-----


# Top navbar

with st.container(horizontal=True, horizontal_alignment="center"):
    if st.button("Notre projet"): 
        st.switch_page("views/about_you.py")
    if st.button("Votre impact"): 
        st.switch_page("views/your_action.py")
    if st.button("Participez"): 
        st.switch_page("views/take_action.py")

        
# --- PAGE SETUP --- 
about_page = st.Page(
    page="views/about_you.py", 
    title="Notre projet",
    icon=":material/emoji_nature:",
    default=True, # use the page as a default main page
)
    

project_page_1 = st.Page(
    page="views/your_action.py", 
    title="Votre impact", 
    icon=":material/hive:",
    )

project_page_2 = st.Page(
    page="views/take_action.py", 
    title="Participez", 
    icon=":material/call_to_action:",
    )


_='''
project_page_2 = st.Page(
    page="views/my_page.py", 
    title="Page_title", 
    icon=":material/hive:",
    )
'''



# --- NAVIGATION BAR LEFT
#pg = st.navigation(pages=[about_page, project_page_1,project_page_2])

# --- RUN NAVIGATION
#pg.run()


# --- NAVIGATION BAR
navigation_bar = st.navigation(pages=[about_page, project_page_1,project_page_2] )


# --- RUN NAVIGATION
navigation_bar.run()


# Social Network Buttons 

social_media_links = ["https://www.facebook.com", 
                     "https://www.instagram.com", 
                     "https://www.youtube.com"
                     
                     ]

social_media_icon = SocialMediaIcons(social_media_links)

social_media_icon.render()

with st.container():
    st.write("---") 
# contact number 
with st.container(horizontal=True, horizontal_alignment="center", border=False): 
    st.button(":material/call: +261 32 00 000 00 - :material/mail: 1000hive@mail.com")
    #st.markdown("<p style='text-align: center;'>:material/call: +261 32 00 000 00 :material/mail: 1000hive@mail.com.</p>", unsafe_allow_html=True)



# --- SHARED ON ALL PAGES 

#st.logo(":material/hive:")
#st.sidebar.text("THiS TeXt is Here")