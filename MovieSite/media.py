#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 12:54:06 2018

@author: jacobpelletier
"""

class Movie():

    def __init__(self, title, storyline, poster_url, trailer_youtube_url):
        """initializes the instance of a movie with the variables
        title, storyline, poster_url, trailer_youtube_url"""
        self.title = title
        self.storyline = storyline
        self.poster_url = poster_url
        self.trailer_youtube_url = trailer_youtube_url

