#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 19:56:06 2018

@author: jacobpelletier
"""
import fresh_tomatoes
import media

deathofstalin = media.Movie('The Death of Stalin', 'Dark comedy about events following'
                     ' the death of stalin.',
                     'https://upload.wikimedia.org/wikipedia/en/8/86/The_Death_of_Stalin.png',
                     'https://www.youtube.com/watch?v=XzO4VIK-sVM',
                     )

theevildead2 = media.Movie('The Evil Dead 2', 'Classic 80s horror/comedy film'
                           ' about demonic possession.',
                           'https://upload.wikimedia.org/wikipedia/en/6/6d/Evil_Dead_II_poster.jpg',
                           'https://www.youtube.com/watch?v=6lM3NPeEG24',
                           )

burnafterreading = media.Movie('Burn After Reading', 'Black comedy about idiocy',
                               'https://upload.wikimedia.org/wikipedia/en/4/42/Burn_After_Reading.png',
                               'https://www.youtube.com/watch?v=SVCHSiRWjJM',
                               )

kungfuhustle = media.Movie('Kung Fu Hustle', 'Chinese Martial arts and gangster'
                           ' comedy film.', 
                           'https://upload.wikimedia.org/wikipedia/en/0/00/KungFuHustleHKposter.jpg',
                           'https://www.youtube.com/watch?v=-m3IB7N_PRk',
                           )

movies = [deathofstalin, theevildead2, burnafterreading, kungfuhustle]
fresh_tomatoes.open_movies_page(movies)
