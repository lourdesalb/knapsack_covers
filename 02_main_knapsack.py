import My_project.knapsack_model as km
import My_project.utils_solving_model as usm
import pandas as pd
from tqdm import tqdm
# data_folder = 'Data/n00050/R01000/'
data_folder = 'Data/n00100/R01000/'
# data_folder = 'Data/n10000/R01000/'
# data_folder = 'Data/n01000/R01000/'
# data_folder = 'Data/n05000/R01000/'
# data_folder = 'Data/n02000/R01000/'
number_of_instances = 25

# instance = 0
metrics = pd.DataFrame(index=range(number_of_instances), columns=['nodes', 'time', 'gap', 'objval'])
for instance in tqdm(range(number_of_instances)):
#for instance in tqdm([10]):
    # for instance in range(5):
    if instance in range(10):
        string_instance = '0' + str(instance)
    else:
        string_instance = str(instance)
    data_knapsack_instance = pd.read_csv(data_folder + 's0' + string_instance + '.kp', header=None)

    number_of_items = int(data_knapsack_instance.loc[0, 0])
    budget = int(data_knapsack_instance.loc[1, 0])
    cost_items = []
    weight_items = []
    list_items = list(range(number_of_items))

    for item in list_items:
        cost_and_weight = data_knapsack_instance.loc[2 + item, 0].split(sep=' ')
        cost_items.append(int(cost_and_weight[0]))
        weight_items.append(int(cost_and_weight[1]))
    aa = 0
    knapsack_model = km.knapsack_model(number_of_items=number_of_items,
                                       budget=budget,
                                       weight_items=weight_items,
                                       cost_items=cost_items,
                                       list_items=list_items)

    knapsack_model = usm.solve_model(model=knapsack_model)

    # knapsack_model.getVars()
    # usm.extract_decision_variables(knapsack_model)

    metrics.loc[instance, 'nodes'] = knapsack_model.NodeCount
    metrics.loc[instance, 'time'] = knapsack_model.RunTime
    metrics.loc[instance, 'gap'] = knapsack_model.MIPGap
    metrics.loc[instance, 'objval'] = knapsack_model.ObjVal
    

metrics.to_csv('metrics_knapsack.csv', sep=';')
aa = 0

aa = 0
