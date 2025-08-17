import streamlit as st 

st.title("Your action")


with st.container(): 
    st.write("""
      Participez à votre echelle et soyez récompensés pour vos actions.      
 """)


offer_col1, offer_col2 = st.columns(2, border=False)

with offer_col1 :  
   with st.expander("ADOPTER UNE RUCHE"): 
        st.write("""
---
---
---
---
---
---
---
---
---""")

with offer_col2 : 
    with st.expander("PARRAINER UNE RUCHE"): 
        st.write("""
---
---
---
---
---
---
---
---
---""")
    
    
