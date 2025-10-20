"""
Module for the actual opinion dynamics simulations.
"""
import numpy as np
import math
import copy

# Test Configuration
PRINT_INTERMEDIATE = False
SHOW_AVERAGE = False
AVG_GROUPS = False
#AVG_GROUPS = [ [0,1,2,3,4,5,6,7,8,9] ]

# Default Model Parameters
TIME = 30 # number of iterations
ALPHA = 0.6 # strength of alignment
RHO = 0.4 # strength of reinforcement
# Whether opinions should be inferred -- set to true if not all initial opinions are known
USE_REFINEMENT = True

def opinion_simulation(
        initial_opinion_value_file: str,
        influence_values_file: str,
        confidence_values_file: str = None,
        result_opinion_progression: str = '',
        result_conf_progression: str = '',
        time: int = TIME,
        alpha: float = ALPHA,
        rho: float = RHO,
        use_refinement: bool = USE_REFINEMENT,
        show_average: bool = SHOW_AVERAGE,
        avg_groups=None,
    ):

    def read_tables(op_value_file, inf_value_file, conf_value_file=None):
        filepath = inf_value_file
        influence = np.atleast_2d(np.genfromtxt(filepath, delimiter=',', dtype='float64')).tolist()

        filepath = op_value_file
        t0 = np.atleast_1d(np.genfromtxt(filepath, dtype='float64')).tolist()

        conf0 = []
        if conf_value_file is not None: #USE_REFINEMENT:
            filepath = conf_value_file
            conf0 = np.atleast_1d(np.genfromtxt(filepath, dtype='float64')).tolist()
        else:
            conf0 = np.zeros(len(t0)).tolist()

        return influence, t0, conf0

    def write_tables(results, conf_results, res_file, c_ref_file=None):
        results = np.asarray(results)

        filepath = res_file
        np.savetxt(filepath, results, delimiter=',', fmt='%1.4f')

        if c_ref_file is not None:
            filepath = c_ref_file
            np.savetxt(filepath, conf_results, delimiter=',', fmt='%1.4f')

    def apply(val1, val2, weight, l_alpha=alpha, l_rho=rho):
        return l_alpha * alignment(val1, val2, weight) + l_rho * reinforcement(val1, val2, weight)

    def alignment(val1, val2, weight):
        return weight * math.tanh(val2 - val1)

    def reinforcement(val1, val2, weight):
        return max(weight, 0) * (val1 + val2) / 2

    def limit(val):
        return max(min(val, 1), -1)

    def append_avg(current, append, groups):
        if not append:
            return current
        cp = np.asarray(current)
        if groups:
            for group in groups:
                l = []
                for i in group:
                    l.append(current[i])
                cp = np.append(cp, np.average(l))
        else:
            cp = np.append(cp, np.average(current))
        return cp.tolist()

    influence, currentT, currentConf = read_tables(
        initial_opinion_value_file, influence_values_file, confidence_values_file)
    length = len(currentT)
    results = [append_avg(currentT, show_average, avg_groups)]
    conf_results = [currentConf]

    for t in range(0, time):
        nextT = copy.deepcopy(currentT)
        nextConf = copy.deepcopy(currentConf)
        for node_id in range(0, length):
            inf = influence[node_id]
            val = float(currentT[node_id])

            conf = currentConf[node_id]
            nconf = 1
            cgain = 0
            if use_refinement:
                nconf_top = 0
                nconf_bottom = 0
                for i in range(0, length):
                    weight = influence[i][node_id]
                    nconf_top += currentConf[i] * abs(weight)
                    nconf_bottom += abs(weight)
                if nconf_bottom != 0:
                    nconf = nconf_top / nconf_bottom
                cgain = (1 - conf) * nconf * nconf_top * (alpha + rho) / 2
                nextConf[node_id] += cgain

            for i in range(0, length):
                weight = influence[i][node_id]
                if use_refinement:
                    weight = weight * currentConf[i] / (nconf or 1)
                nextT[node_id] += (1 - conf) * apply(val, currentT[i], weight)

            nextT[node_id] = limit(nextT[node_id])

        currentT = nextT
        currentConf = nextConf
        results.append(append_avg(currentT, show_average, avg_groups))
        conf_results.append(currentConf)

        write_tables(results, conf_results, result_opinion_progression, result_conf_progression)