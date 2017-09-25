from pulp import *

def get_variables(bom,materials,lp_vars):
    for part, num in materials.iteritems():
        for level, bill in bom.iteritems():
            if part in bill[0]:
                lp_var = LpVariable(name=part + '_' + level,
                                    lowBound=0,
                                    upBound=num,
                                    cat=LpInteger if isinstance(bill[1], int) else LpContinuous)
                lp_vars.append(lp_var)


def get_objective(lp_vars,objective):
    # objective will be finding maximize of produced products, a number called K
    for var in lp_vars:
        objective.append(0)
    objective.append(1)  # coef for K


def get_inequality_constraints(materials,lp_vars,A_ineq,B_ineq):
    for part, num in materials.iteritems():
        row = []
        for var in lp_vars:
            row.append(1 if part == var.name.split('_') else 0)

        row.append(0)  # coef for K

        A_ineq.append(row)
        B_ineq.append(num)


def get_equality_constraints(bom,lp_vars,A_eq,B_eq):
    for level, bill in bom.iteritems():
        row = []
        coef = bill[1]
        options = bill[0]

        for var in lp_vars:
            if var.name.split('_')[0] in options and var.name.split('_')[1] == level:
                row.append(1)
            else:
                row.append(0)

        # print type(coef)
        # coef = float(coef)
        row.append(-coef)  # coef for K
        A_eq.append(row)
        B_eq.append(0)


def calculator(bom,materials,lp_vars,A_eq,B_eq,A_ineq,B_ineq,objective,materials_dict):
    prob = LpProblem("Dong bo san pham", LpMaximize)
    get_variables(bom,materials,lp_vars)
    get_objective(lp_vars,objective)
    get_equality_constraints(bom,lp_vars,A_eq,B_eq)
    get_inequality_constraints(materials,lp_vars,A_ineq,B_ineq)

    lp_vars.append(LpVariable('K', 0, cat=LpInteger))
    num_of_vars = len(lp_vars)

    # objective
    prob += lpSum([objective[i] * lp_vars[i] for i in xrange(num_of_vars)])

    # equality constraints
    for i in xrange(len(A_eq)):
        prob += lpSum([A_eq[i][j] * lp_vars[j] for j in xrange(num_of_vars)]) == B_eq[i]

    # inequality constraints
    for i in xrange(len(A_ineq)):
        prob += lpSum([A_ineq[i][j] * lp_vars[j] for j in xrange(num_of_vars)]) <= B_ineq[i]

    prob.solve()

    # Solution
    # materials_dict = {}
    for v in prob.variables():
        materials_dict[v.name] = v.varValue

    return value(prob.objective)
    # print "objective=", value(prob.objective)
    # print materials_dict