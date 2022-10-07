import streamlit as st

#st.title('🎈 streamlit-option-menu')

import streamlit as st
from streamlit_option_menu import option_menu

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu('Main Menu', ['Home', 'Upload', 'Tasks', 'Settings'], 
        icons=['house', 'cloud-upload', 'list-task', 'gear'], menu_icon='cast', default_index=1)
    st.write('**You are here:**', selected)
    
# 2. horizontal menu
selected2 = option_menu(None, ['Home', 'Upload', 'Tasks', 'Settings'], 
    icons=['house', 'cloud-upload', 'list-task', 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
st.write('**You are here:**', selected2)

# 3. CSS style definitions
#selected3 = option_menu(None, ['Home', 'Upload',  'Tasks', 'Settings'], 
#    icons=['house', 'cloud-upload', "list-task", 'gear'], 
#    menu_icon="cast", default_index=0, orientation="horizontal",
#    styles={
#        "container": {"padding": "0!important", "background-color": "#fafafa"},
#        "icon": {"color": "orange", "font-size": "25px"}, 
#        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#        "nav-link-selected": {"background-color": "green"},
#    }
#)
