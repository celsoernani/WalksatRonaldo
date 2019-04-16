# Resolver problema SAT com DPLL

import sys, random
import time


# Lê o arquivo
def parse(filename):
    clauses = []
    for line in open(filename):
        if line.startswith('c'): continue
        if line.startswith('p'):
            nvars, nclauses = line.split()[2:4]
            continue
        clause = [int(x) for x in line[:-2].split()]
        clauses.append(clause)
    return clauses, int(nvars)

# Escolhe um literal e adiciona ele puro as clausulás
def bcp(formula, unit):
    modified = []
    for clause in formula:
        if unit in clause: continue
        if -unit in clause:
            c = [x for x in clause if x != -unit]
            if len(c) == 0: return -1
            modified.append(c)
        else:
            modified.append(clause)
    return modified


def get_counter(formula):
    counter = {}
    for clause in formula:
        for literal in clause:
            if literal in counter:
                counter[literal] += 1
            else:
                counter[literal] = 1
    return counter

# Verifica se existe algum literal puro
def pure_literal(formula):
    counter = get_counter(formula)
    assignment = []
    pures = [] 
    for literal, times in counter.items():
        if -literal not in counter: pures.append(literal)
    for pure in pures:
        formula = bcp(formula, pure)
    assignment += pures
    return formula, assignment

# Propagação do literal selecionada
def unit_propagation(formula):
    assignment = []
    unit_clauses = [c for c in formula if len(c) == 1]
    while len(unit_clauses) > 0:
        unit = unit_clauses[0]
        formula = bcp(formula, unit[0])
        assignment += [unit[0]]
        if formula == -1:
            return -1, []
        if not formula:
            return formula, assignment
        unit_clauses = [c for c in formula if len(c) == 1]
    return formula, assignment

# Seleciona uma variável para ser analisáda
def variable_selection(formula):
    counter = get_counter(formula)
    return random.choice(list(counter.keys()))

# "Força bruta" faz as verificações consecutivas em busca da solução
def backtracking(formula, assignment):
    formula, pure_assignment = pure_literal(formula)
    formula, unit_assignment = unit_propagation(formula)
    assignment = assignment + pure_assignment + unit_assignment
    if formula == - 1:
        return []
    if not formula:
        return assignment

    variable = variable_selection(formula)
    solution = backtracking(bcp(formula, variable), assignment + [variable])
    if not solution:
        count_main = count_main + 1
        solution = backtracking(bcp(formula, -variable), assignment + [-variable])
    return solution

def main():
    clauses, nvars = parse(sys.argv[1])
    print(clauses)
    count_main = 0



    inicio = time.time()
    solution = backtracking(clauses, [])
    fim = time.time()
    print("Tempo de execução", fim - inicio)


    solution = backtracking(clauses, [])
    print(count_main)
    
    if solution:
        solution += [x for x in range(1, nvars + 1) if x not in solution and -x not in solution]
        solution.sort(key=lambda x: abs(x))
        print('s SATISFIABLE')
        print('v ' + ' '.join([str(x) for x in solution]) + ' 0')
    else:
        print('s UNSATISFIABLE')


if __name__ == '__main__':
    main()