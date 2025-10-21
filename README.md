## ER'25: Shaping Your World – Conceptualizing Viewpoint Dynamics in Event-Centric Knowledge Graphs

This repository contains the code used in the evaluation of the opinion dynamics approach in our ER'25 paper.

In general, the requirements to execute the code are low; you need a Python installation with numpy and  matplotlib installed (all requirements can be installed via pip using the ```requirements.txt```).
To ease the execution, each figure in the paper is mapped to a corresponding script (where the necessary data, i.e., initial opinions, influence network, and confidences, can be found in the corresponding folders). 
The file ````simulations.py```` contains the actual opinion dynamics code that implements the formulas explained in the paper.
The ```plotter.py``` file contains the matplotlib code for the actual plotting.

The paper in question is this one:

```bibtex
@article{affeldt_etal_opinion_dynamics,
    author={Affeldt, Till
        and Pl{\"o}tzky, Florian
        and Balke, Wolf-Tilo},
    editor={Bork, Dominik
        and Lukyanenko, Roman
        and Sadiq, Shazia
        and Bellatreche, Ladjel
        and Pastor, Oscar},
    title={Shaping Your World -- Conceptualizing Viewpoint Dynamics in Event-Centric Knowledge Graphs},
    booktitle={Conceptual Modeling},
    year={2026},
    publisher={Springer Nature Switzerland},
    address={Cham},
    pages={283--301},
    isbn={978-3-032-08623-5},
    doi={10.1007/978-3-032-08623-5_15}
}
```
