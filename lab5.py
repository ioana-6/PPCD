from mpi4py import MPI
import random

def random_1_9(times = 1): #daca cineva a apelat functia fara vreun parametru, times va fi by default 1
    """
    random_1_9 generates a random number between 1 and 9, simulating a dice.

    :return: integer values of generated numbers under an array.

    """
    result = []
    for time in times:
        result.append(random.randint(1,9))
    return result

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

match rank:
    case 0:
        x0 = random_1_9()
        print(f"Process {rank} threw a {x0}")
    case 1:
        x1 = random_1_9()
        x1x0 = x1*10 + x0
        print(f"Process {rank} threw a {x1x0}")
    case 2:
        x2 = random_1_9()
        x2x1x0 = x2*100 + x1*10 + x0
        print(f"Process {rank} threw a {x2x1x0}")
    case 3:
        x3 = random_1_9()
        x3x2x1x0 = x3*1000 + x2*100 + x1*10 + x0
        print(f"Process {rank} threw a {x3x2x1x0}")
