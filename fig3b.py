"""
This file generates Fig. 3b
"""
from simulations import opinion_simulation
from plotter import plot_data

# user parameters
SHOW_FILE_ONLY_DO_NOT_PRINT = True

# file parameters
INFLUENCE_FILE = 'Fig3b/influence.csv'
INITIAL_OPINIONS = 'Fig3b/t0.csv'
RESULT_OPINION_PROGRESSION = 'Fig3b/opinion_progression.csv'
RESULT_CONF_PROGRESSION = 'Fig3b/conf_progression.csv'
IMG_PATH = 'Fig3b/opinion_progression.svg'

# model parameters
TAU = 40
ALPHA = .1
RHO = .2

opinion_simulation(
    initial_opinion_value_file=INITIAL_OPINIONS,
    influence_values_file=INFLUENCE_FILE,
    confidence_values_file=None,
    result_opinion_progression=RESULT_OPINION_PROGRESSION,
    result_conf_progression=RESULT_CONF_PROGRESSION,
    time=TAU,
    alpha=ALPHA,
    rho=RHO,
    use_refinement=False,
    show_average=True,
    avg_groups=[ [0,1,2,3,4,5,6,7,8,9] ]
)

plot_data(
    RESULT_OPINION_PROGRESSION,
    IMG_PATH,
    use_refinement=False,
    auto_colors=False,
    colors= 10 * ['0.7'] + ['b', 'r'],
    show_graph=SHOW_FILE_ONLY_DO_NOT_PRINT
)