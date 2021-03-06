# -*- coding: utf-8 -*-

import re

def check_file(text):
    '''
    Check that the input file have the right format
    '''

    patterns = ['Organizador', 'Elo medio', 'Fecha', '', 'Clasificación Final', '', 'Rank']
    cErrors = 0

    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')
    print("CHECKEAR FORMATO:")
    print('...')

    for i in range(7):
        if not (re.search(patterns[i], text[i+2])):
            cErrors = cErrors+1
            print("pattern: ", patterns[i])
            print("file: ", text[i+2])

    if (cErrors != 0):
        print('Errores encontrados en el formato: ', cErrors)
        print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')

    else:
        print('Formato de archivo OK!')
        print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')

def menu(p, p_r):
    print("el rating para "+ p.name +" en la base es "+ str(p_r.rating))
    print("pero en el torneo esta ingresado con "+str(p.rating))
    print("Presione 1 para conservar el valor de la base, 0 en el otro caso")
    inp = input("")
    if int(inp):
        p.set_rating(p_r.rating)

def check_players_rating(players_list, rating_list):
    '''
    Check if players from the tournament with rating are in the rating list
    And if the rating matches
    '''

    print('..................................................')
    print("Chequendo los jugadores en la base...")
    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')

    cErrors = 0

    for player in players_list:
        if (player.rating != 0):
            p = [_player for _player in rating_list if (_player.name == player.name)]
            try:
                p = p[0]
                if (player.rating != p.rating):
                    print("el rating de "+player.name+" no coincide con la base")
                    menu(player, p)
                    
                player.refresh_data_r(p.id, p.n_games, p.k)
            except IndexError:
                print("el jugador "+player.name+" no se encuentra en la base")
                cErrors = cErrors + 1
    
    return(cErrors)
