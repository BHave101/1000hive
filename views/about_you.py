import streamlit as st 
import time 

with st.container(): 
    st.title("Votre projet")

    with st.container(border=True): 
        st.write(""" Nous croyons qu’un simple geste peut avoir un impact immense. 
    Accueillir une ruche chez soi, c’est offrir un foyer à des milliers d'abeilles et redonner vie à la biodiversité urbaine. 
    Plutôt qu’un apiculteur possédant des milliers de ruches, nous rêvons d’inspirer des milliers de personnes à en adopter seulement deux.
    """)

#with st.container() : 
col1, col2, col3 = st.columns(3, border=True)


with col1 : 
    st.header("Votre ruche")
    st.write("""Une ruche dans votre jardin, sur votre balcon ou votre toit. 
Nous installons et entretenons tout pour que vous profitiez de pleinement de l’expérience. """)

with col2 : 
    st.header("Votre miel")
    st.write(""" Un miel unique, produit par vos abeilles, à votre adresse.
Mis en pot, prêt à être partagé avec vos proches.""" )

with col3 : 
    st.header("Votre impact")
    st.write("""Chaque jour, vos abeilles pollinisent les fleurs et jardins
 de votre quartier, aidant la nature à reprendre sa place en ville.
""")
    

with st.container(): 
    #empty_col1, 
    st.write("Voir nos offres")
    if st.button("Nos offres"): 
        st.switch_page("views/your_action.py")