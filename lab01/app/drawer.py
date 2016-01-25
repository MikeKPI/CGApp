import math


def draw_bow(O, r, start_angle=0, finish_angle=2*math.pi, prec=128):
    PREC = 100
    angle = math.fabs(finish_angle - start_angle) / prec
    yield from ((round(math.cos(angle*i + start_angle) * r + O[0], PREC),
                 round(math.sin(angle*i + start_angle) * r + O[1], PREC))
                for i in range(prec+1))

def default_figure(h=100, r_vert=20, r_hor=20, r_in=10, r_out=20):
    h2 = h / 2
    from .figure import create_figure

    for bow in create_figure(h, r_vert, r_hor, r_in, r_out):
        yield draw_bow(O=bow['O'], r=bow['r'],
                       start_angle=bow['sangle'],
                       finish_angle=bow['fangle'])

    yield ((h2, r_hor), (r_vert, h2))
    yield ((h2, -r_hor), (r_vert, -h2))
    yield ((-h2, -r_hor), (-r_vert, -h2))
    yield ((-h2, r_hor), (-r_vert, h2))
    yield ((h2, 0), (0, h2-r_vert))
    yield ((-h2, 0), (0, h2-r_vert))
    yield ((h2, 0), (0, -h2+r_vert))
    yield ((-h2, 0), (0, -h2+r_vert))

if __name__ == '__main__':
    for i in draw_bow((0, 0), 100, prec=5):
        print(i)
