# <PSEUDOCOD>
#departament_achizitii (rank 0)
 #    primeste de la manager (rank 1) un ordin (tip int - cate caiete?????)
  #   transmite celor 3 angajati (rank 2, 3, 4) cate caiete trebuie????

#angajatii (2, 3, 4)
  #genereaza oferte de tip array (numar +pret/unitate)
  #trimite inapoi la manager

#manager ()
  # primeste ofertele si genereaza o combinatie    
                                      
import random
import time

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()


if rank == 0:
    quantity = 100;
    comm.send(quantity, 1)

    
    offers = []
    for i in range(2, 4):
        offers.append(comm.recv(sorce = 1))

    sorted_offers = sorted(offers, key=lambda x: x['price_per_unit'])
    print.pprint(sorted_offers)

    #print (offers)

    for offer in sorted_offers:
        if quantity > 0:
            if offer['amount'] >= quantity:
               quantity -= offer['amount']
            else:
               quantity -= offer['amount']

if rank == 1:
    quantity = comm.rec(0)
    for i in range(2, 5):
        comm.send(quantity, 1)

# employees rank 2,3,4

if rank in range(2, 5):
    quantity = comm.recv(source = 1)

    # generat oferta / combinatie
    amount = random.randint(quantity-50, quantity+50)
    #price_per_unit = random.randint(1, 5) #RON
    price_per_unit = round(random.uniform(1, 5), 2)

    offer = {
        'amount' : amount;
        'price_per_unit' : price_per_unit;
    }

    comm.send(offer, 0)
