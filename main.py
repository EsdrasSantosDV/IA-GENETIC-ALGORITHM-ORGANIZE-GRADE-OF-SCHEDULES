import tkinter
from tkinter import *
from tkinter import ttk
import os
import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random as rd
from scipy.optimize import dual_annealing
from matplotlib.figure import Figure
import math
import random
import pandas as pd
from copy import deepcopy
DAYS = 5  # Dias da semana
PERIODS = 4  # Períodos por dia
CLASS = 6  # Número de turmas
SUBJECTS = 33  # Número de disciplinas

subject_names = {
    -1: "JANELA",
    1: "Algoritmos",
    2: "Algoritmos",
    3: "Algoritmos",
    4: "Algoritmos",
    5: "Algoritmos",
    6: "Algoritmos",
    7: "Algoritmos",
    8: "Algoritmos",
    9: "F. Web Design",
    10: "F. Web Design",
    11: "Matemática",
    12: "Matemática",
    13: "Matemática",
    14: "Matemática",
    15: "Matemática",
    16: "Matemática",
    17: "Extensão 1",
    18: "Arquitetura",
    19: "Arquitetura",
    20: "Arquitetura",
    21: "Lógica",
    22: "Lógica",
    23: "Lógica",
    24: "E.D.",
    25: "E.D.",
    26: "E.D.",
    27: "E.D.",
    28: "E.D.",
    29: "E.D.",
    30: "Mod. B.D.",
    31: "Mod. B.D.",
    32: "S.O.",
    33: "S.O.",
    34: "S.O.",
    35: "S.O.",
    36: "Extensão 2",
    37: "Script Web",
    38: "Script Web",
    39: "P.O.O.",
    40: "P.O.O.",
    41: "P.O.O.",
    42: "P.O.O.",
    43: "P.O.O.",
    44: "P.O.O.",
    45: "Extensão 3",
    46: "P.O.",
    47: "P.O.",
    48: "P.O.",
    49: "P.O.",
    50: "P.O.",
    51: "B.D.",
    52: "B.D.",
    53: "B.D.",
    54: "B.D.",
    55: "B.D.",
    56: "B.D.",
    57: "Interface",
    58: "Interface",
    59: "P.D.M.",
    60: "P.D.M.",
    61: "P.D.M.",
    62: "P.D.M.",
    63: "P.D.M.",
    64: "P.D.M.",
    65: "P.D.M.",
    66: "P.D.M.",
    67: "D.A.W.1",
    68: "D.A.W.1",
    69: "D.A.W.1",
    70: "D.A.W.1",
    71: "Esof",
    72: "Esof",
    73: "Esof",
    74: "Esof",
    75: "Extensão 4",
    76: "Redes",
    77: "Redes",
    78: "Redes",
    79: "Redes",
    80: "LabEsof",
    81: "LabEsof",
    82: "LabEsof",
    83: "LabEsof",
    84: "LabEsof",
    85: "LabEsof",
    86: "P.P.",
    87: "P.P.",
    88: "Extensão 5",
    89: "D.A.W.2",
    90: "D.A.W.2",
    91: "D.A.W.2",
    92: "D.A.W.2",
    93: "Probabilidade",
    94: "Probabilidade",
    95: "Ética",
    96: "Ética",
    97: "Implant Servidores",
    98: "Implant Servidores",
    99: "Implant Servidores",
    100: "Implant Servidores",
    101: "GeProj",
    102: "GeProj",
    103: "GeProj",
    104: "GeProj",
    105: "Seg. Info",
    106: "Seg. Info",
    107: "Seg. Info",
    108: "Seg. Info",
    109: "Extensão 6",
    110: "Extensão 6",
    111: "Empreend.",
    112: "Empreend.",
    113: "Ciência de Dados",
    114: "Ciência de Dados",
    115: "Ciência de Dados",
    116: "Ciência de Dados",
    117: "Intel. Comput.",
    118: "Intel. Comput.",
    119: "Intel. Comput.",
    120: "Intel. Comput.",
}

subjects_by_class = {
    1: [
        {"Id": 1, "Professor": "Ernani Borges", "Nome": "Algoritmos"},
        {"Id": 2, "Professor": "Ernani Borges", "Nome": "Algoritmos"},
        {"Id": 3, "Professor": "Ernani Borges", "Nome": "Algoritmos"},
        {"Id": 4, "Professor": "Ernani Borges", "Nome": "Algoritmos"},
        {"Id": 5, "Professor": "Ernani Borges", "Nome": "Algoritmos"},
        {"Id": 6, "Professor": "Ernani Borges", "Nome": "Algoritmos"},
        {"Id": 7, "Professor": "Ernani Borges", "Nome": "Algoritmos"},
        {"Id": 8, "Professor": "Ernani Borges", "Nome": "Algoritmos"},
        {"Id": 9, "Professor": "Marco Maciel", "Nome": "F. Web Design"},
        {"Id": 10, "Professor": "Marco Maciel", "Nome": "F. Web Design"},
        {"Id": 11, "Professor": "Jorge", "Nome": "Matemática"},
        {"Id": 12, "Professor": "Jorge", "Nome": "Matemática"},
        {"Id": 13, "Professor": "Jorge", "Nome": "Matemática"},
        {"Id": 14, "Professor": "Jorge", "Nome": "Matemática"},
        {"Id": 15, "Professor": "Jorge", "Nome": "Matemática"},
        {"Id": 16, "Professor": "Jorge", "Nome": "Matemática"},
        {"Id": 17, "Professor": "Aline", "Nome": "Extensão 1"},
        {"Id": 18, "Professor": "Rogélio", "Nome": "Arquitetura"},
        {"Id": 19, "Professor": "Rogélio", "Nome": "Arquitetura"},
        {"Id": 20, "Professor": "Rogélio", "Nome": "Arquitetura"},
    ],
    2: [
        {"Id": 21, "Professor": "Marcelo Barreiro", "Nome": "Lógica"},
        {"Id": 22, "Professor": "Marcelo Barreiro", "Nome": "Lógica"},
        {"Id": 23, "Professor": "Marcelo Barreiro", "Nome": "Lógica"},
        {"Id": 24, "Professor": "Alexandre", "Nome": "E.D."},
        {"Id": 25, "Professor": "Alexandre", "Nome": "E.D."},
        {"Id": 26, "Professor": "Alexandre", "Nome": "E.D."},
        {"Id": 27, "Professor": "Alexandre", "Nome": "E.D."},
        {"Id": 28, "Professor": "Alexandre", "Nome": "E.D."},
        {"Id": 29, "Professor": "Alexandre", "Nome": "E.D."},
        {"Id": 30, "Professor": "Camilo", "Nome": "Mod. B.D."},
        {"Id": 31, "Professor": "Camilo", "Nome": "Mod. B.D."},
        {"Id": 32, "Professor": "Gustavo Bota", "Nome": "S.O."},
        {"Id": 33, "Professor": "Gustavo Bota", "Nome": "S.O."},
        {"Id": 34, "Professor": "Gustavo Bota", "Nome": "S.O."},
        {"Id": 35, "Professor": "Gustavo Bota", "Nome": "S.O."},
        {"Id": 36, "Professor": "Rogélio", "Nome": "Extensão 2"},
        {"Id": 37, "Professor": "Aline", "Nome": "Script Web"},
        {"Id": 38, "Professor": "Aline", "Nome": "Script Web"},
    ],
    3: [
        {"Id": 39, "Professor": "Eduardo Silvestre", "Nome": "P.O.O."},
        {"Id": 40, "Professor": "Eduardo Silvestre", "Nome": "P.O.O."},
        {"Id": 41, "Professor": "Eduardo Silvestre", "Nome": "P.O.O."},
        {"Id": 42, "Professor": "Eduardo Silvestre", "Nome": "P.O.O."},
        {"Id": 43, "Professor": "Eduardo Silvestre", "Nome": "P.O.O."},
        {"Id": 44, "Professor": "Eduardo Silvestre", "Nome": "P.O.O."},
        {"Id": 45, "Professor": "Camilo", "Nome": "Extensão 3"},
        {"Id": 46, "Professor": "Hugo", "Nome": "P.O."},
        {"Id": 47, "Professor": "Hugo", "Nome": "P.O."},
        {"Id": 48, "Professor": "Hugo", "Nome": "P.O."},
        {"Id": 49, "Professor": "Hugo", "Nome": "P.O."},
        {"Id": 50, "Professor": "Hugo", "Nome": "P.O."},
        {"Id": 51, "Professor": "Rogério Costa", "Nome": "B.D."},
        {"Id": 52, "Professor": "Rogério Costa", "Nome": "B.D."},
        {"Id": 53, "Professor": "Rogério Costa", "Nome": "B.D."},
        {"Id": 54, "Professor": "Rogério Costa", "Nome": "B.D."},
        {"Id": 55, "Professor": "Rogério Costa", "Nome": "B.D."},
        {"Id": 56, "Professor": "Rogério Costa", "Nome": "B.D."},
        {"Id": 57, "Professor": "Lídia", "Nome": "Interface"},
        {"Id": 58, "Professor": "Lídia", "Nome": "Interface"},
    ],
    4: [
        {"Id": 59, "Professor": "Jefferson", "Nome": "P.D.M."},
        {"Id": 60, "Professor": "Jefferson", "Nome": "P.D.M."},
        {"Id": 61, "Professor": "Jefferson", "Nome": "P.D.M."},
        {"Id": 62, "Professor": "Jefferson", "Nome": "P.D.M."},
        {"Id": 63, "Professor": "Jefferson", "Nome": "P.D.M."},
        {"Id": 64, "Professor": "Jefferson", "Nome": "P.D.M."},
        {"Id": 65, "Professor": "Jefferson", "Nome": "P.D.M."},
        {"Id": 66, "Professor": "Jefferson", "Nome": "P.D.M."},
        {"Id": 67, "Professor": "Rafael Godoi", "Nome": "D.A.W.1"},
        {"Id": 68, "Professor": "Rafael Godoi", "Nome": "D.A.W.1"},
        {"Id": 69, "Professor": "Rafael Godoi", "Nome": "D.A.W.1"},
        {"Id": 70, "Professor": "Rafael Godoi", "Nome": "D.A.W.1"},
        {"Id": 71, "Professor": "Mauro", "Nome": "Esof"},
        {"Id": 72, "Professor": "Mauro", "Nome": "Esof"},
        {"Id": 73, "Professor": "Mauro", "Nome": "Esof"},
        {"Id": 74, "Professor": "Mauro", "Nome": "Esof"},
        {"Id": 76, "Professor": "Frederico", "Nome": "Redes"},
        {"Id": 77, "Professor": "Frederico", "Nome": "Redes"},
        {"Id": 78, "Professor": "Frederico", "Nome": "Redes"},
        {"Id": 79, "Professor": "Frederico", "Nome": "Redes"},
    ],
    5: [
        {"Id": 80, "Professor": "Mauro", "Nome": "LabEsof"},
        {"Id": 81, "Professor": "Mauro", "Nome": "LabEsof"},
        {"Id": 82, "Professor": "Mauro", "Nome": "LabEsof"},
        {"Id": 83, "Professor": "Mauro", "Nome": "LabEsof"},
        {"Id": 84, "Professor": "Mauro", "Nome": "LabEsof"},
        {"Id": 85, "Professor": "Mauro", "Nome": "LabEsof"},
        {"Id": 86, "Professor": "Marco Maciel", "Nome": "P.P."},
        {"Id": 87, "Professor": "Marco Maciel", "Nome": "P.P."},
        {"Id": 88, "Professor": "Ademir", "Nome": "Extensão 5"},
        {"Id": 89, "Professor": "Lídia", "Nome": "D.A.W.2"},
        {"Id": 90, "Professor": "Lídia", "Nome": "D.A.W.2"},
        {"Id": 91, "Professor": "Lídia", "Nome": "D.A.W.2"},
        {"Id": 92, "Professor": "Lídia", "Nome": "D.A.W.2"},
        {"Id": 93, "Professor": "Alef", "Nome": "Probabilidade"},
        {"Id": 94, "Professor": "Alef", "Nome": "Probabilidade"},
        {"Id": 95, "Professor": "Ana Lúcia", "Nome": "Ética"},
        {"Id": 96, "Professor": "Ana Lúcia", "Nome": "Ética"},
        {"Id": 97, "Professor": "Gustavo Bota", "Nome": "Implant Servidores"},
        {"Id": 98, "Professor": "Gustavo Bota", "Nome": "Implant Servidores"},
        {"Id": 99, "Professor": "Gustavo Bota", "Nome": "Implant Servidores"},
        {"Id": 100, "Professor": "Gustavo Bota", "Nome": "Implant Servidores"},
    ],
    6: [
        {"Id": 101, "Professor": "Marco Maciel", "Nome": "GeProj"},
        {"Id": 102, "Professor": "Marco Maciel", "Nome": "GeProj"},
        {"Id": 103, "Professor": "Marco Maciel", "Nome": "GeProj"},
        {"Id": 104, "Professor": "Marco Maciel", "Nome": "GeProj"},
        {"Id": 105, "Professor": "Elson", "Nome": "Seg. Info"},
        {"Id": 106, "Professor": "Elson", "Nome": "Seg. Info"},
        {"Id": 107, "Professor": "Elson", "Nome": "Seg. Info"},
        {"Id": 108, "Professor": "Elson", "Nome": "Seg. Info"},
        {"Id": 109, "Professor": "Ademir", "Nome": "Extensão 6"},
        {"Id": 110, "Professor": "Ademir", "Nome": "Extensão 6"},
        {"Id": 111, "Professor": "Ana Lúcia", "Nome": "Empreend."},
        {"Id": 112, "Professor": "Ana Lúcia", "Nome": "Empreend."},
        {"Id": 113, "Professor": "Marcelo Barreiro", "Nome": "Ciência de Dados"},
        {"Id": 114, "Professor": "Marcelo Barreiro", "Nome": "Ciência de Dados"},
        {"Id": 115, "Professor": "Marcelo Barreiro", "Nome": "Ciência de Dados"},
        {"Id": 116, "Professor": "Marcelo Barreiro", "Nome": "Ciência de Dados"},
        {"Id": 117, "Professor": "José Ricardo", "Nome": "Intel. Comput."},
        {"Id": 118, "Professor": "José Ricardo", "Nome": "Intel. Comput."},
        {"Id": 119, "Professor": "José Ricardo", "Nome": "Intel. Comput."},
        {"Id": 120, "Professor": "José Ricardo", "Nome": "Intel. Comput."},
    ],
}



def translate_schedule(schedule):
    translated_schedule = []

    for x in range(CLASS):
        translated_schedule.append([])
        for y in range(PERIODS * DAYS):
            translated_schedule[x].append(schedule[x][y]["Nome"])
    return translated_schedule



def create_individual():
    individual = []

    for i in range(CLASS):
        group = []
        available_subjects = [x for x in range(0, PERIODS * DAYS)]
        chosen_subjects = []
        for _ in range(PERIODS * DAYS):
            subject_chosen = random.choice(available_subjects)
            while subject_chosen in chosen_subjects:
                subject_chosen = random.choice(available_subjects)

            try:
                group.append(subjects_by_class[i + 1][subject_chosen])
            except IndexError:
                group.append({"Id": -1, "Professor": None, "Nome": "JANELA"})
            chosen_subjects.append(subject_chosen)
        individual.append(group)

    return individual



def create_population(population_size):
    return [create_individual() for _ in range(population_size)]


# Função de fitness
def fitness(individual):
    score = 0
    cp=0
    ocr2=0
    ocr3=0
    ocr4=0

    for i in range(0,4):
        for z in range(5):
            v = individual[z][i * 4:4 + (i * 4)]
            comparador = v[0]
            count = 1
            for j in range(1, 4):
                if comparador['Nome'] == v[j]['Nome']:
                    count = count + 1
                else:
                    if count == 2:
                        ocr2 = ocr2 + 1
                    elif count == 3:
                        ocr3 = ocr3 + 1
                    elif count == 4:
                        ocr4 = ocr4 + 1
                    count = 0
                    comparador = v[j]
            if count == 2:
                ocr2 = ocr2 + 1
            elif count == 3:
                ocr3 = ocr3 + 1
            elif count == 4:
                ocr4 = ocr4 + 1


    for i in range(PERIODS * DAYS):
        counter = list()
        for j in range(CLASS):
            counter.append(individual[j][i]['Professor'])
        counter_set = set(counter)
        cp += (len(counter) - len(counter_set))

    return 7900 + 5*ocr2+10*ocr3+15*ocr4-500*cp

def select(population, fitnesses, num_parents):
    total_fitness = sum(fitnesses)
    probs = [f / total_fitness for f in fitnesses]
    parents = []
    for _ in range(num_parents):
        r = random.random()  # Gera um número aleatório entre 0 e 1
        for i, individual in enumerate(population):
            r -= probs[i]
            if r <= 0:
                parents.append(individual)
                break
    return parents


def crossover(parent1, parent2, crossover_rate):
    # Escolher um ponto de cruzamento aleatório
    crossover_point = random.randint(0, CLASS-1)

    should_cross = random.random()
    if should_cross < crossover_rate:
        # Criar os filhos
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]

        return deepcopy(child1), deepcopy(child2)
    else:
        return parent1, parent2

def mutate(individual, mutation_rate):
    individual_copy = deepcopy(individual)
    for i in range(CLASS):
        for _ in range(PERIODS * DAYS):
            if random.random() < mutation_rate:
                j_chosen1 = random.randint(0, (PERIODS * DAYS) - 1)
                j_chosen2 = random.randint(0, (PERIODS * DAYS) - 1)
                individual_copy[i][j_chosen1], individual_copy[i][j_chosen2] = individual_copy[i][j_chosen2], individual_copy[i][j_chosen1]
    return deepcopy(individual)

def replace_population(population, new_individuals):
    # Substitui os indivíduos menos aptos pelos novos indivíduos
    population.sort(key=fitness)
    population[:len(new_individuals)] = deepcopy(new_individuals)

    return deepcopy(population)


def genetic_algorithm(population_size, num_generations,mutation_rate,crossover_rate,eletism):
    population = create_population(population_size)
    populacao_pela_geracao = 0
    geracaoencontrada=0
    max_fitness_scores = []
    plt.figure()
    for gen in range(num_generations):
        # Calcula o fitness de cada indivíduo na população
        fitnesses = [fitness(individual) for individual in population]

        # Seleciona os pais
        parents = select(population, fitnesses, population_size // 2)

        # Gera os filhos por cruzamento
        children = []
        for i in range(0, len(parents), 2):
            child1, child2 = crossover(parents[i], parents[i + 1],crossover_rate)
            children.append(child1)
            children.append(child2)

        # Aplica a mutação nos filhos
        mutated_children = [mutate(child, mutation_rate) for child in children]

        # Implementação do elitismo
        population.sort(key=fitness, reverse=True)  # Ordena a população pelo fitness (de maior para menor)
        elites = deepcopy(population[:eletism])


        if populacao_pela_geracao != max(population, key=fitness):
            populacao_pela_geracao =max(population, key=fitness)
            geracaoencontrada = gen + 1

        # Substitui a população
        population = replace_population(population, mutated_children)

        population.sort(key=fitness, reverse=False)
        population[:eletism] = deepcopy(elites)
        best_individual = max(population, key=fitness)
        max_fitness_scores.append(fitness(best_individual))

        plt.plot(max_fitness_scores)
        plt.pause(0.001)  # Pause for 1 millisecond

    melhor_geracao.config(text=f"Geração em que foi encontrado a melhor geração: {geracaoencontrada}")
    best_individual = max(population, key=fitness)
    plt.show()
    return best_individual

def display_df_in_new_window(df):
    # Cria uma nova janela
    new_window = Toplevel()

    # Cria um Treeview
    tree = ttk.Treeview(new_window)

    # Configura as colunas do Treeview
    tree["columns"] = list(df.columns)
    for col in df.columns:
        tree.heading(col, text=col)

    # Adiciona as linhas do DataFrame ao Treeview
    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    tree.pack()
    new_window.mainloop()



def submit_button_event():
    population_size = int(form_tamanho_da_populacao.get())
    probabilidade_de_cruzamento = float(form_probabilidade_de_cruzamento.get())
    mutacao_probabilidade = float(form_mutacao_probabilidade.get())
    num_generations = int(form_quantidade_geracoes.get())
    if check_var.get():
        tamanho_torneio = int(form_tamanho_torneio.get())
    else:
        tamanho_torneio = None
    tamanho_elitismo = int(form_tamanho_elitismo.get())
    tamanho_elitismo = int(form_tamanho_elitismo.get())
    selection_method = "tournament" if check_var.get() else "roulette"
    print("Tamanho da população:", population_size)
    print("Probabilidade de cruzamento:", probabilidade_de_cruzamento)
    print("Probabilidade de mutação:", mutacao_probabilidade)
    print("Quantidade de gerações:", num_generations)
    print("Tamanho do torneio:", tamanho_torneio)
    print("Tamanho do elitismo:", tamanho_elitismo)
    print("Selection method:", selection_method)
    schedule = genetic_algorithm(population_size, num_generations,mutacao_probabilidade,probabilidade_de_cruzamento,tamanho_elitismo)



    df = pd.DataFrame(translate_schedule(schedule))

    header1 = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta']
    header2 = ['19h00', '19h50', '20h50', '21h40']
    header = [f'{day} - {hour}' for day in header1 for hour in header2]
    df.columns = header
    display_df_in_new_window(df)


def fill_form():
    form_tamanho_da_populacao.delete(0, tkinter.END)
    form_tamanho_da_populacao.insert(0, str(100))
    form_probabilidade_de_cruzamento.delete(0, tkinter.END)
    form_probabilidade_de_cruzamento.insert(0, str(0.85))
    form_mutacao_probabilidade.delete(0, tkinter.END)
    form_mutacao_probabilidade.insert(0, str(0.5))
    form_quantidade_geracoes.delete(0, tkinter.END)
    form_quantidade_geracoes.insert(0, str(100))
    form_tamanho_torneio.delete(0, tkinter.END)
    form_tamanho_torneio.insert(0, str(15))
    form_tamanho_elitismo.delete(0, tkinter.END)
    form_tamanho_elitismo.insert(0, str(10))
def toggle_torneio_visibility():
    if check_var.get():
        label_tamanho_torneio.place(x=100, y=200)
        form_tamanho_torneio.place(x=325, y=200)
    else:
        label_tamanho_torneio.place_forget()
        form_tamanho_torneio.place_forget()

window = Tk()
window.title("IA-TRABALHO-GRUPO-ESDRAS-JOAO-OTAVIO-FELIPE MENDES")
window.geometry('600x600')
window.configure(background="gray")


label_form=tkinter.Label(window,text="Dados das Entradas",background="gray")
label_tamanho_da_populacao = tkinter.Label(window, text="Tamanho da População:",background="gray")
label_probabilidade_de_cruzamento = tkinter.Label(window, text="Probabilidade de Cruzamento:",background="gray")
label_mutacao_probabilidade = tkinter.Label(window, text="Probabilidade de Mutação:",background="gray")
label_quantidade_geracoes = tkinter.Label(window, text="Quantidade de Geracoes:",background="gray")
label_tamanho_torneio =  tkinter.Label(window, text="Tamanho do Torneio:",background="gray")
label_tamanho_elitismo = tkinter.Label(window, text="Tamanho do Elitismo:", background="gray")
result_best_individual = tkinter.Label(window, text="Melhor Individuo Encontrado:")
result_function_value = tkinter.Label(window, text="Aptidão:")
melhor_geracao=tkinter.Label(window,text="Geração em que foi encontrado a melhor geração:")
resultadoreal=tkinter.Label(window,text="Valor Maximo da Função:")
porcentagem_de_erro=tkinter.Label(window,text="Porcentagem de erro entre o Máximo encontrado e o Maximo Real:")


form_tamanho_elitismo = tkinter.Entry()
form_tamanho_da_populacao=tkinter.Entry()
form_probabilidade_de_cruzamento=tkinter.Entry()
form_mutacao_probabilidade=tkinter.Entry()
form_quantidade_geracoes=tkinter.Entry()
form_tamanho_torneio=tkinter.Entry()


label_form.place(x=200,y=10)
label_tamanho_da_populacao.place(x=100,y=50)
form_tamanho_da_populacao.place(x=325,y=50)
label_probabilidade_de_cruzamento.place(x=100,y=80)
form_probabilidade_de_cruzamento.place(x=325,y=80)
label_quantidade_geracoes.place(x=100,y=110)
form_quantidade_geracoes.place(x=325,y=110)
label_mutacao_probabilidade.place(x=100,y=140)
form_mutacao_probabilidade.place(x=325,y=140)
label_tamanho_elitismo.place(x=100, y=170)
form_tamanho_elitismo.place(x=325, y=170)
result_best_individual.place(x=100, y=700)
result_function_value.place(x=100, y=750)
melhor_geracao.place(x=100,y=400)
resultadoreal.place(x=100,y=850)
porcentagem_de_erro.place(x=100,y=900)
#CHECKBOX
check_var = tkinter.BooleanVar()
check_torneio = tkinter.Checkbutton(window, text="Torneio", variable=check_var, command=toggle_torneio_visibility, background="gray")
check_torneio.place(x=100, y=230)
label_tamanho_torneio.place_forget()
form_tamanho_torneio.place_forget()


#SUBMIT
submit_button = tkinter.Button(window, text="Submit", command=submit_button_event)
submit_button.place(x=350, y=300)

#BOTAO PREENCHER
preencher_button=tkinter.Button(window,text="To Fill",command=fill_form)
preencher_button.place(x=350,y=350)

window.mainloop()