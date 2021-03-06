from pulp import *
import data_30


bom = {}
materials = {}
madeable_parts = {}
madeable_dict = {}


def get_madeable_parts():
    for level, bill in bom.iteritems():
        tmp = level.split(".")
        depth = len(tmp)
        if depth > 1:
            tmp_level = ".".join(tmp[0:depth - 1])
            if tmp_level in bom:
                part = bom[tmp_level][0][0]
                made_key = part + '_m'
                if made_key not in madeable_parts:
                    madeable_parts[made_key] = {}
                madeable_parts[made_key][level] = bill
                madeable_dict[tmp_level] = made_key


def replace_madeable_parts(madeable_parts):
    for level, bill in bom.iteritems():
        parts = bill[0]
        for part in bill[0]:
            if part + '_m' in madeable_parts:
                parts.append(part + '_m')
        bill[0] = parts


def main():
    global madeable_parts
    global madeable_dict
    madeable_parts = {}
    madeable_dict = {}
    get_madeable_parts()
    replace_madeable_parts(madeable_parts)
    madeable_vars_dict = {}
    madeable_level_vars_dict = {}
    part_level_vars_dict = {}

    part_level_dict = {}

    for part,formula in madeable_parts.iteritems():
        madeable_vars_dict[part] = LpVariable(part, lowBound=0, cat=LpInteger)
        madeable_level_vars_dict[part] = []

    for part, quantity in materials.iteritems():
        part_level_vars_dict[part] = []

    prob = LpProblem("Dong bo san pham", LpMaximize)

    objective = LpVariable("objective", lowBound=0, cat=LpInteger)

    # objective
    prob += objective

    # equality constraints
    for level, bill in bom.iteritems():
        parts = bill[0]
        quantity = bill[1]
        lp_vars = []
        i = 0
        for part in parts:
            # lp_var = LpVariable(part + '_' + level,
            #                     lowBound=0,
            #                     cat=LpInteger if isinstance(quantity, int) else LpContinuous)
            part_level_dict[level+'_'+str(i)] = part + '_' + level

            lp_var = LpVariable(level+'_'+str(i),
                                lowBound=0,
                                cat=LpInteger if isinstance(quantity, int) else LpContinuous)
            i += 1

            if "_m" not in part:
                part_level_vars_dict[part].append(lp_var)
            else:
                madeable_level_vars_dict[part].append(lp_var)

            lp_vars.append(lp_var)

        if len(level.split(".")) == 1:
            prob += lpSum(lp_vars) - quantity * objective == 0
        else:
            tmp = level.split(".")
            tmp_level = ".".join(tmp[0:len(tmp) - 1])
            if tmp_level in madeable_dict:
                tmp_part = madeable_dict[tmp_level]
                prob += lpSum(lp_vars) - quantity * madeable_vars_dict[tmp_part] == 0
            else:
                prob += lpSum(lp_vars) - quantity * objective == 0

    # inequality constraints
    for part, vars in part_level_vars_dict.iteritems():
        if len(vars) > 0:
            prob += lpSum(vars) - materials[part] <= 0

    for part, vars in madeable_level_vars_dict.iteritems():
        prob += lpSum(vars) - madeable_vars_dict[part] == 0

    # LpSolverDefault.msg = 1
    prob.solve()
    tmp ={}
    for var in prob.variables():
        if var.name in part_level_dict:
            if part_level_dict[var.name] in tmp:
                if var.varValue > 0:
                    tmp[part_level_dict[var.name]] = var.varValue
            else:
                tmp[part_level_dict[var.name]] = var.varValue
            # print "%s=%d" % (part_level_dict[var.name], var.varValue)
        else:
            # print "%s=%d" % (var.name, var.varValue)
            tmp[var.name] = var.varValue

    result = {}
    result['objective'] = tmp['objective']
    result['bom'] = {}
    for key, value in tmp.iteritems():
        if '_' in key:
            levels = key.split('_')
            name = key.split('_')[0]
            if len(levels) ==2 and levels[1] != 'm':
                required = bom[levels[1]][1]
                if levels[1] not in result['bom']:
                    result['bom'][levels[1]] = {
                        name:value
                    }

                else:
                    result['bom'][levels[1]][name] = value

            elif len(levels) ==2 and levels[1] == 'm':
                if levels[1] not in result:
                    result[levels[1]] = {
                        name: value
                    }

                else:
                    result[levels[1]][name] = value
            elif len(levels) == 3:
                name = key.split('_')[0] +'_'+ key.split('_')[1]
                if levels[2] not in result['bom']:
                    result['bom'][levels[2]] = {
                        name:value
                    }
                else:
                    result['bom'][levels[2]][name]= value
    return result

if __name__ == '__main__':
    main()