# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

def print_tab(tab):
    for i in tab:
        print(i, '- ', end='')
    print()


def generate_tab_I_p(D, M, p):
    m = 2 * p

    nbTacheDuree1 = 4 * p
    nbTacheDuree2 = 2 * p * (p - 1)

    for i in range(nbTacheDuree1):
        D.append(1)

    for i in range(nbTacheDuree2):
        D.append(2)

    D.append(2 * p)

    for i in range(m):
        M.append(0)

def generate_tab_I_r(D, M):

    m = int(input("Nombre de machine : "))
    n = int(input("Nombre de tâche : "))
    k = int(input("Nombre d'instance : "))

    d_min = int(input("Durée de tâche minimum : "))
    d_max = int(input("Durée de tâche maximum : "))

    for i in range(m):
        D.append(0)

    for i in range(n):
        M.append(random.randint(d_min, d_max))

    return k




def stubLSA(D, M):
    return 0, 0


def stubLPT(D, M):
    return 0, 1


def stubRMA(D, M):
    return 1, 0


def launcher():
    type = -1

    D = []
    M = []

    print("Type d'instance :\n",
          "[1] Génération d'une instance de type I_p\n",
          "[2] Génération aléatoire de plusieurs instance")

    while int(type) not in (1, 2):
        type = int(input("choix: "))

    if type == 1:
        p = int(input("Entrée la valeur de p: "))
        generate_tab_I_p(D, M, p)

        #TODO borne inferieur max
        #TODO borne inferieur moyenne

        result = stubLSA(D, M)
        print("Résultat LSA = ", result[0])
        print("ratio LSA    = ", result[1])

        print()

        result = stubLPT(D, M)
        print("Résultat LPT = ", result[0])
        print("ratio LPT    = ", result[1])

        print()

        result = stubRMA(D, M)
        print("Résultat RMA = ", result[0])
        print("ratio RMA    = ", result[1])

    elif type == 2:
        k = generate_tab_I_r(D, M)

        print_tab(D)
        print_tab(M)

    print("finis")

def LPT(machine_list, task_list, middle_bound, max_bound ):

    sorted(task_list)
    task_list.sort(reverse = True)

    for i in range(len(task_list)):
        min_machine_list = min(machine_list)
        pos = machine_list.index(min_machine_list)
        machine_list[pos] += task_list[i]

    max = max(machine_list)
    max_bound = max(max_bound,middle_bound)
    ratio =  max_bound/max

    return max,ratio

def RMA(machine_list, task_list, middle_bound, max_bound):

    for i in range(len(task_list)):
        next_machine = random.randint(0,len(task_list-1))
        machine_list[next_machine] += task_list[i]

    max = max(machine_list)
    max_bound = max(max_bound,middle_bound)
    ratio =  max_bound/max

    return max,ratio

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    launcher()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
