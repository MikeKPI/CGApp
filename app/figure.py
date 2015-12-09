import math


def create_figure(h=10, r_vert=2, r_hor=2, r_in=1, r_out=2):
    h2 = h / 2
    return  [
        {
            'O': (-h2, 0),
            'r': r_hor,
            'sangle': math.pi / 2,
            'fangle': math.pi * 3 / 2
        },
        {
            'O': (h2, 0),
            'r': r_hor,
            'sangle': math.pi * 3 / 2,
            'fangle': math.pi * 5 / 2
        },
        {
            'O': (0, h2),
            'r': r_vert,
            'sangle': 0,
            'fangle': math.pi * 2
        },
        {
            'O': (0, -h2),
            'r': r_vert,
            'sangle': 0,
            'fangle': math.pi * 2
        },
        {
            'O': (0, 0),
            'r': r_in,
            'sangle': 0,
            'fangle': math.pi * 2
        },
        {
            'O': (0, 0),
            'r': r_out,
            'sangle': 0,
            'fangle': math.pi * 2
        }
    ]
