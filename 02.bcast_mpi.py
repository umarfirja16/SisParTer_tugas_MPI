# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
total = comm.Get_size()

# jika saya rank 0 maka saya akan melakukan broadscast
if rank == 0:
	pesan = 'pesan'

# jika saya bukan rank 0 maka saya menerima pesan
else:
	pesan = None

data = comm.bcast(data, root=0)
print("rank : ",rank, "Pesan : ",pesan)
