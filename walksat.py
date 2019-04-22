import random
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import time



##formato nas expressões 1 2 3 4 5 0 onde cada Números positivos denotam as variáveis ​​correspondentes.
# Números negativos indicam as negações das variáveis ​​correspondentes. Formando assim as expressões.
#0 é o final da expressão


#Função que ler o arquivo das clausulas. JUnto com os parametros para o WalkSat
def parse(filename):
    clauses = []
    count = 0
    for line in open(filename):

        if line[0] == 'c':
            continue
        if line[0] == 'p':
            n_vars = int(line.split()[2])
            lit_clause = [[] for _ in range(n_vars * 2 + 1)]
            continue

        clause = []
        for literal in line[:-2].split():
            literal = int(literal)
            clause.append(literal)
            lit_clause[literal].append(count)
        clauses.append(clause)
        count += 1
    return clauses, n_vars, lit_clause

#Escolhendo um simbolo aleatoriamente de acordo com o numero enviado no parametro
def get_random_interpretation(n_vars):
    return [i if random.random() < 0.5 else -i for i in range(n_vars + 1)]


##vendo as clausulas que existem apos o sorteio
def get_true_sat_lit(clauses, interpretation):
    true_sat_lit = [0 for _ in clauses]
    for index, clause in enumerate(clauses):
        for lit in clause:
            if interpretation[abs(lit)] == lit:
                true_sat_lit[index] += 1
    fig, ax = plt.subplots()
    ax.plot(true_sat_lit, label="Corretos")
    ax.legend()
    plt.show()
    return true_sat_lit


def update_tsl(literal_to_flip, true_sat_lit, lit_clause):
    for clause_index in lit_clause[literal_to_flip]:
        true_sat_lit[clause_index] += 1
    for clause_index in lit_clause[-literal_to_flip]:
        true_sat_lit[clause_index] -= 1



##contando valors errados
def compute_broken(clause, true_sat_lit, lit_clause, omega=0.4):
    break_min = sys.maxsize
    best_literals = []
    for literal in clause:

        break_score = 0

        for clause_index in lit_clause[-literal]:
            if true_sat_lit[clause_index] == 1:
                break_score += 1

        if break_score < break_min:
            break_min = break_score
            best_literals = [literal]
        elif break_score == break_min:
            best_literals.append(literal)


    if break_min != 0 and random.random() < omega:
        best_literals = clause

    return random.choice(best_literals)


def run_sat(clauses, n_vars, lit_clause, max_flips_proportion=4): 
    max_flips = n_vars * max_flips_proportion
    clauses_unsatisfied = []
    count_mistakes = 0
    y_graf_wrong = []
    while 1:
        interpretation = get_random_interpretation(n_vars)
        true_sat_lit = get_true_sat_lit(clauses, interpretation)
        for _ in range(max_flips):
            ##percorrendo todas as vezes que é para porucrar clausula, se a clausula de interpretação estiver 
            ##nao preenche o vetor
            unsatisfied_clauses_index = [index for index, true_lit in enumerate(true_sat_lit) if
                                         not true_lit]
            
            #caso a lista de clasulas seja vazia, ele retorna a solução mais outras variaveis para gerar o grafico
            if not unsatisfied_clauses_index:
                return interpretation,clauses_unsatisfied,y_graf_wrong

            ##se nao for satisfeito ele escolhe outra clausula aleatoriamente nao satisfeita
            clause_index = random.choice(unsatisfied_clauses_index)
            unsatisfied_clause = clauses[clause_index]
            
            ##variaveis para geração de grafico
            clauses_unsatisfied.append(str(unsatisfied_clause))
            y_graf_wrong.append(count_mistakes)
            count_mistakes = count_mistakes + 1 ##conta como erro
            ##computando erros e acertos

            lit_to_flip = compute_broken(unsatisfied_clause, true_sat_lit, lit_clause)
            ##atualiazndo o tamanho nova pesquisa
            update_tsl(lit_to_flip, true_sat_lit, lit_clause)
            interpretation[abs(lit_to_flip)] *= -1

            ##caso não tenha uma solução ele ficará num looping eterno procurando um clausula
  

def main():
    ##lendo as variaveis do arquivo 'clausulas, 
    clauses, n_vars, lit_clause = parse(sys.argv[1])
    
    ##Gerando graficos para comparação
    m = len(clauses)
    print("M", m)
    print("N", n_vars)
    m_list = [10, 20, 180,50,50]
    n_list = [10,34, 50, 400,500]
    list_time = [1.8050298690795898, 1.8818731307983398,  2.1404731273651123, 2.201709270477295, 2.752943754196167]
    list_time_dpll = [0, 0, 0.0029845237731933594,0.0039861202239990234, 0.042881011962890625]
    fig, ax = plt.subplots()
    ax.plot(n_list, m_list, label="M/N")
    fig.suptitle('Razão M/N de acordo com o testes feitos')
    ##Gerando graficos para comparação



    ##Calculando tempo de execução
    inicio = time.time()
    solution,clauses_unsatisfied,y_graf_wrong  = run_sat(clauses, n_vars, lit_clause)
    fim = time.time()
    print("Tempo de execução", fim - inicio)
    ##Calculando tempo de execução
    
    
    ##Gerando graficos para comparação
    fig, ax = plt.subplots( figsize=(15, 10))
    ax.plot(clauses_unsatisfiedd, y_graf_erro, label="Clausulas não encontradas .")
    ax.legend()
    plt.show()
    plt.plot( n_list, list_time_dpll,linewidth=2.0 , label = "DPLL")
    plt.plot(n_list,list_time , linewidth=2.0 , label = "WalkSat")
    plt.legend()
    plt.show()
    ##Gerando graficos para comparação





    ##Pritando se foi satisfeito ou nao 
    print ('s SATISFIABLE')
    print ('v ' + ' '.join(map(str, solution[1:])) + ' 0')


if __name__ == '__main__':
    main()