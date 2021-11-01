import streamlit as st


class MultiPage:
    def __init__(self) -> None:
        """Constructor class to generate a list which will
        store all the applications as an instance variable"""

        self.pages = []

    def add_page(self, title, func) -> None:
        self.pages.append({
            "title": title,
            "function": func
        })

    def run(self):
        page = st.sidebar.radio("Browse", self.pages,
                                format_func=lambda app: app['title'])
        page['function']()
