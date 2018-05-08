# for correct performance, run unbuffered with 3 processes:
# mpiexec -n 3 python26 scratch.py -u
import numpy
from mpi4py import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
        #x = numpy.linspace(0,100,11)
        x = ['aaa','bbb','ccc','ddd','eee']
else:
        x = None

if rank == 2:
        xlocal = numpy.zeros(2)
else:
        xlocal = numpy.zeros(1)

if rank ==0:
        print ("Scatter")

comm.Scatterv([x,(1,1,2,1),(0,1,2,3),MPI.DOUBLE],xlocal)
print ("process " + str(rank) + " has " +str(xlocal))