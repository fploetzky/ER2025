"""
This file generates Fig. 7b (the case study's opinion progression).
"""
from simulations import opinion_simulation
from plotter import plot_data

# user parameters
SHOW_FILE_ONLY_DO_NOT_PRINT = True

# file parameters
CONF_FILE = 'Fig7b/conf0.csv'
INFLUENCE_FILE = 'Fig7b/influence.csv'
INITIAL_OPINIONS = 'Fig7b/t0.csv'
RESULT_OPINION_PROGRESSION = 'Fig7b/opinion_progression.csv'
RESULT_CONF_PROGRESSION = 'Fig7b/conf_progression.csv'
IMG_PATH = 'Fig7b/opinion_progression.svg'

# model parameters
TAU = 20
ALPHA = .3
RHO = .2

opinion_simulation(
    initial_opinion_value_file=INITIAL_OPINIONS,
    influence_values_file=INFLUENCE_FILE,
    confidence_values_file=CONF_FILE,
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
    colors=['b', 'r'],
    first_n_agents_only=2, # Choose only DEMs and GOP for this purpose
    show_graph=SHOW_FILE_ONLY_DO_NOT_PRINT
)