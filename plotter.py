"""
Generate the plots based on the opinion dynamics csv files
"""
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
from random import shuffle, seed

def plot_data(
        data_path: str,
        img_path: str,
        use_refinement=True,
        auto_colors=True,
        colors=None,
        show_graph=True,
        color_seed = 543534,
        first_n_agents_only=None
    ):

    def directions(x, y):
        assert x.shape == y.shape
        u = np.zeros(x.shape)
        v = np.zeros(x.shape)
        for i in range(x.shape[0] - 1):
            u[i] = x[i + 1] - x[i]
            v[i] = y[i + 1] - y[i]
        u[-1] = u[-2]
        v[-1] = v[-2]
        return u, v

    def rotate(x, y, phi):
        v = np.array([x, y])
        R = np.array([
            [np.cos(phi), -np.sin(phi)],
            [np.sin(phi), np.cos(phi)]
        ])
        return R @ v

    def plotArrows(x, y, color='0'):
        u, v = directions(x, y)
        plt.quiver(x, y, u, v, scale_units='xy', angles='xy', scale=1, width=.004,
                   headlength=4, headwidth=4, color=color)

    def getColors(numcolors, s=color_seed):
        seed(s)
        base_colors = mcolors.BASE_COLORS
        del base_colors['w']
        if numcolors > 7:
            base_colors = mcolors.XKCD_COLORS
        colors = [*base_colors.values()]
        shuffle(colors)

        return colors[0:numcolors]

    def drawMultiple(V, colors, use_ref=use_refinement):
        Y = np.arange(0, V.shape[1], 1)
        if use_ref:
            Y = np.arange(-V.shape[1], 0, 1)
        for column in range(V.shape[0]):
            plotArrows(V[column], Y, colors[column])

    datapath = data_path
    data = np.transpose(np.atleast_2d(np.genfromtxt(datapath, delimiter=',', dtype='float64')))
    imgpath = img_path

    MAX_T = data.shape[1]
    NUM_COLUMNS = data.shape[0]
    if first_n_agents_only is not None:
        V = data[0:first_n_agents_only, :]
    else:
        V = data

    if auto_colors:
        colors = getColors(NUM_COLUMNS)
    #else:
    #    colors = colors
    assert colors is not None
    drawMultiple(V, colors)

    y_start = 0
    y_end = MAX_T

    if use_refinement:
        y_start = -MAX_T
        y_end = 0

    plt.axis([-1, 1, y_end, y_start])
    plt.xlabel('Opinion $o_i^c(t)$')
    plt.ylabel('Time $t$')
    plt.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
    if show_graph:
        plt.show()
    else:
        plt.savefig(imgpath)

