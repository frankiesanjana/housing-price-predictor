# The code in this file is adapted from CI's WP02 "Churnometer"

import streamlit as st


class MultiPage: 
    """
    Class to generate multiple Streamlit pages
    using an object-oriented approach
    """
    def __init__(self, app_name) -> None:
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon=":house_buildings:")
    
    def add_page(self, title, func) -> None:
        # adds a new page to the list of pages
        self.pages.append({"title": title, "function": func })

    def run(self):
        """
        Sets title of application, creates sidebar
        with radio button for page selection, and
        runs the function associated with the
        """
        st.title(self.app_name)
        page = st.sidebar.radio('Menu', self.pages, format_func=lambda page: page['title'])
        page['function']() 

