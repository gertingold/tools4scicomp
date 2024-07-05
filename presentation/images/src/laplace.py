from mpi4py import MPI
import numpy as np
from numpy import r_
import matplotlib.pyplot as plt

def jacobi_step(u):
    u_old = u.copy()
    u[1:-1, 1:-1] = 0.25*(u[0:-2, 1:-1] + u[2:, 1:-1] 
                          + u[1:-1,0:-2] + u[1:-1, 2:])
    v = (u-u_old).flat
    return u, np.dot(v,v)

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
root = 0

num_points = 500
rows_per_process = num_points//size
max_iter = 5000
num_iter = 0
total_err = 1

m = None

if rank == root:
    m = np.zeros((num_points, num_points), dtype=float)
    m[0, :] = 1
    m[:, 0] = 1
    m[-1, :] = -1
    m[:, -1] = -1

my_grid = np.empty((rows_per_process, num_points), dtype=float)
comm.Scatterv(m, my_grid, root)

while num_iter < max_iter and total_err > 1e-7:
    if rank == 0:
        comm.Send(my_grid[-1, :], 1)

    if rank > 0 and rank < size-1:
        row_above = np.empty((1, num_points), dtype=float)
        comm.Recv(row_above, rank-1)
        comm.Send(my_grid[-1, :], rank+1)

    if rank == size-1:
        row_above = np.empty((1, num_points), dtype=float)
        comm.Recv(row_above, rank-1)
        comm.Send(my_grid[0, :], rank-1)

    if rank > 0 and rank < size-1:
        row_below = np.empty((1, num_points), dtype=float)
        comm.Recv(row_below, rank+1)
        comm.Send(my_grid[0, :], rank-1)

    if rank == 0:
        row_below = np.empty((1, num_points), dtype=float)
        comm.Recv(row_below, 1)

    if rank > 0 and rank < size-1:
        u, err = jacobi_step(r_[row_above, my_grid, row_below])
        my_grid = u[1:-1, :]

    if rank == 0:
        u, err = jacobi_step(r_[my_grid, row_below])
        my_grid = u[0:-1, :]

    if rank == size-1:
        u, err = jacobi_step(r_[row_above, my_grid])
        my_grid = u[1:, :]

    if num_iter % 500 == 0:
        err_list = np.empty(size, dtype=float)
        comm.Gather(err, err_list, root)
        if rank == 0:
            total_err = 0
            for err in err_list:
                total_err = total_err + err
            total_err = np.sqrt(total_err)/num_points**2
            print(f"{total_err = :8.3g}")
        total_err = comm.bcast(total_err, root)

    num_iter=num_iter+1

recvbuf = np.empty_like(m)

comm.Gather(my_grid, recvbuf, root)
if rank == 0:
    sol = np.array(recvbuf)
    sol.shape = (num_points,num_points)
    print(f"{num_iter = }")
    plt.imshow(sol)
    plt.show()
