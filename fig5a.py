"""
This file generates Fig. 5a
"""
from simulations import opinion_simulation
from plotter import plot_data

# user parameters
SHOW_FILE_ONLY_DO_NOT_PRINT = True

# file parameters
INFLUENCE_FILE = 'Fig5a/influence.csv'
INITIAL_OPINIONS = 'Fig5a/t0.csv'
RESULT_OPINION_PROGRESSION = 'Fig5a/opinion_progression.csv'
RESULT_CONF_PROGRESSION = 'Fig5a/conf_progression.csv'
IMG_PATH = 'Fig5a/opinion_progression.svg'

# model parameters
TAU = 50
ALPHA = .3
RHO = .2

opinion_simulation(
    initial_opinion_value_file=INITIAL_OPINIONS,
    influence_values_file=INFLUENCE_FILE,
    result_opinion_progression=RESULT_OPINION_PROGRESSION,
    result_conf_progression=RESULT_CONF_PROGRESSION,
    time=TAU,
    alpha=ALPHA,
    rho=RHO,
    use_refinement=False,
    show_average=False,
)

plot_data(
    RESULT_OPINION_PROGRESSION,
    IMG_PATH,
    use_refinement=False,
    auto_colors=False,
    colors= ['b', 'r', 'g'],
    show_graph=SHOW_FILE_ONLY_DO_NOT_PRINT
)