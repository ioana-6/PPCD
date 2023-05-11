from mpi4py import MPI
import random

#Simulate throwing a dice
#ca sa explicam optim o functie, in loc sa folosim comentarii si sa ingreunam editorul, putem adauga o descriere (on hover) ca pentru cele integrate
def random_1_6(times = 1): #daca cineva a apelat functia fara vreun parametru, times va fi by default 1
    """
    random_1_6 generates a random number between 1 and 6, simulating a dice.

    :return: integer values of generated numbers under an array.

    """
    result = []
    for time in times:
        result.append(random.randint(1,6))
    return result

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

match rank:
    case 0:
        #Throw once
        rank_0_throws = random_1_6()
        print(f"Process {rank} threw a {rank_0_throws}")
    case 1:
        #Throw twice
        rank_1_throws = random_1_6(2)
        print(f"Process {rank} threw a {rank_1_throws}")
        #Sum values
        sum_rank_1 = sum(rank_1_throws)
        print(f"Sum of values thrown by process {rank} is {sum_rank_1}")
    case 2:
        #Throw thrice
        rank_2_throws = random_1_6(3)
        #Sum values
        sum_rank_2 = sum(rank_2_throws)
        print(f"Sum of values thrown by process {rank} is {sum_rank_2}")
