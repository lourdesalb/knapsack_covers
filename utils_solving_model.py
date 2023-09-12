def solve_model(model):
    model.optimize()
    return model


def extract_decision_variables(model):
    xi = [var.x for var in model.getVars()]

    return xi
