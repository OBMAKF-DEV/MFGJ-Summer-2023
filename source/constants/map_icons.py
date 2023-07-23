from enum import Enum


class MapIcons:
    items = dict()
    items['X'] = 'player_icon'
    items['+'] = 'container'
    items['#'] = 'wall'
    items['-'] = 'floor'


TILE_DATA = {
    'floor': {'passable': True, 'interactable': False, 'format': 'jpg'},
    'wall': {'passable': False, 'interactable': False, 'format': 'jpg'},
    'container': {'passable': False, 'interactable': True, 'format': 'png'},
}
