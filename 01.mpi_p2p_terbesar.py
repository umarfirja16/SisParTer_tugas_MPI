# import mpi4py
from mpi4py import MPI

# buat COMM
comm = MPI.COMM_WORLD

# dapatkan rank proses
rank = comm.Get_rank()

# dapatkan total proses berjalan
total = comm.Get_size()

# jika saya rank terbesar maka saya akan mengirimkan pesan ke proses yang mempunyai rank 0 s.d rank terbesar-1
if rank == total-1:
	pesan = "pesan"
	for i in range(0, size-1):
		comm.send(data, dest=i)
		print('Mengirim pesan : '.format(rank), pesan,' ke ',i)
		
# jika saya bukan rank terbesar maka saya akan menerima pesan yang berasal dari proses dengan rank terbesar
else:
	pesan = comm.recv(source = total-1)
	print('Menerima pesan : '.format(rank), pesan)
