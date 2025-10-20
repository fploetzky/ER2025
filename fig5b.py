"""
This file generates Fig. 5b
"""
from simulations import opinion_simulation
from plotter import plot_data

# user parameters
SHOW_FILE_ONLY_DO_NOT_PRINT = True

# file parameters
CONF_VALUE_FILE = 'Fig5b/conf0.csv'
INFLUENCE_FILE = 'Fig5b/influence.csv'
INITIAL_OPINIONS = 'Fig5b/t0.csv'
RESULT_OPINION_PROGRESSION = 'Fig5b/opinion_progression.csv'
RESULT_CONF_PROGRESSION = 'Fig5b/conf_progression.csv'
IMG_PATH = 'Fig5b/opinion_progression.svg'

# model parameters
TAU = 50
ALPHA = .3
RHO = .2

opinion_simulation(
    confidence_values_file=CONF_VALUE_FILE,
    initial_opinion_value_file=INITIAL_OPINIONS,
    influence_values_file=INFLUENCE_FILE,
    result_opinion_progression=RESULT_OPINION_PROGRESSION,
    result_conf_progression=RESULT_CONF_PROGRESSION,
    time=TAU,
    alpha=ALPHA,
    rho=RHO,
    use_refinement=True,
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