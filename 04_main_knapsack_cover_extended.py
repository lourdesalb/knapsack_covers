# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 15:07:47 2023

@author: Lourdes
"""

import My_project.knapsack_model as km
import My_project.knapsack_cover_model as kcm
import My_project.utils_solving_model as usm
import My_project.knapsack_cover_extended_model as un

import numpy as np
import pandas as pd
from itertools import combinations
from tqdm import tqdm

data_folder = 'Data/n00100/R01000/'
number_of_instances = 25

# instance = 4
metrics = pd.DataFrame(index=range(number_of_instances), columns=[
                       'nodes', 'time', 'gap', 'objval'])
for instance in range(number_of_instances):
#for instance in [10]:

    if instance in range(10):
        string_instance = '0' + str(instance)
    else:
        string_instance = str(instance)
    data_knapsack_instance = pd.read_csv(
        data_folder + 's0' + string_instance + '.kp', header=None)

    number_of_items = int(data_knapsack_instance.loc[0, 0])
    budget = int(data_knapsack_instance.loc[1, 0])
    cost_items = []
    weight_items = []
    list_items = list(range(number_of_items))

    for item in list_items:
        cost_and_weight = data_knapsack_instance.loc[2 +
            item, 0].split(sep=' ')
        cost_items.append(int(cost_and_weight[0]))
        weight_items.append(int(cost_and_weight[1]))
    aa = 0

    covers = []  # lista covers (lista de listas)
    # creacion de los covers
    for item in range(40):
        cover = [item]
        # cost_items_in_cover = [cost_items[item]]
        cost_items_in_cover = [weight_items[item]]
        item_to_include = item + 1
        while sum(cost_items_in_cover) <= budget:
            cover.append(item_to_include)
            cost_items_in_cover.append(weight_items[item_to_include])
            item_to_include += 1
        covers.append(cover)

    todos = list(range(100))
    new_covers = []
    for c in covers:
        new_covers.append(c+[j for j in list(set(todos)-set(c))
                          if all([weight_items[j] >= weight_items[i] for i in c])])

    knapsack_cover_model = un.knapsack_cover_model2(number_of_items=number_of_items,
                                                    budget=budget,
                                                    weight_items=weight_items,
                                                    cost_items=cost_items,
                                                    list_items=list_items,
                                                    new_covers=new_covers, covers=covers)

    knapsack_cover_model = usm.solve_model(model=knapsack_cover_model)
    metrics.loc[instance, 'nodes'] = knapsack_cover_model.NodeCount
    metrics.loc[instance, 'time'] = knapsack_cover_model.RunTime
    metrics.loc[instance, 'gap'] = knapsack_cover_model.MIPGap
    metrics.loc[instance, 'objval'] = knapsack_cover_model.ObjVal
    metrics.to_csv('metrics_knapsack_cover_extended.csv', sep=';')
    aa = 0
     
  #  print(new_covers)
  #  print("--------------------------------------------------")
  #  print(covers)