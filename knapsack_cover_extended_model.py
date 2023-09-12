# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 16:13:51 2023

@author: Lourdes
"""

import gurobipy as gp
from gurobipy import GRB


def knapsack_cover_model2(number_of_items,
                         budget,
                         weight_items,
                         cost_items,
                         list_items,
                         new_covers,covers):
    model = gp.Model('knapsack')
    model.setParam('Cuts', 0)
    # model.setParam('BQPCuts', 0)
    # model.setParam('CliqueCuts', 0)
    # model.setParam('CoverCuts', 0)
    # model.setParam('FlowCoverCuts', 0)
    # model.setParam('FlowPathCuts', 0)
    # model.setParam('GUBCoverCuts', 0)
    # model.setParam('ImpliedCuts', 0)
    # model.setParam('InfProofCuts', 0)
    # model.setParam('Heuristics', 0)
    model.setParam('Presolve', 0)
    model.setParam('TimeLimit', 60)
    # model.Params.LogToConsole = 0  # Do not show details of the optimization problem

    # Decision variables

    xi = model.addVars(number_of_items, vtype=GRB.BINARY, name='binaries')

    # Constraints

    constraint_1 = model.addConstr(gp.quicksum(weight_items[item] * xi[item] for item in list_items) <= budget)
    i= 0
    for cover in covers:
        constraint_cover = model.addConstr(gp.quicksum(xi[item] for item in new_covers[i]) <= (len(cover) - 1))
        i+=1

    # Objective function

    objective = model.setObjective(gp.quicksum(cost_items[item] * xi[item] for item in list_items), sense=GRB.MAXIMIZE)

    return model
