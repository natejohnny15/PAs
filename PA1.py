import random 
from tabulate import tabulate
import time

def _1D(moves):
    count = 0 
    particle = 0 
    step = [-1,1]
    for i in range(moves):
        particle += random.choice(step)
        if particle == 0:
            count += 1
            break
    return count
def _2D(moves):
    count = 0 
    particle = [0,0]
    step = [-1,1]
    AxisChoice = [0,1]
    for i in range(moves):
        particle[random.choice(AxisChoice)] += random.choice(step)
        if particle == [0,0]:
            count += 1
            break
    return count
def _3D(moves):
    count = 0 
    particle = [0,0,0]
    step = [-1,1]
    AxisChoice = [0,1,2]
    for i in range(moves):
        particle[random.choice(AxisChoice)] += random.choice(step)
        if particle == [0,0,0]:
            count += 1
            break
    return count
def main():
    moves = [20,200,2000,20000,200000,2000000]
    _1D_list = ['1D']
    _2D_list = ['2D']
    _3D_list = ['3D']
    for i in moves:
        _1D_percentage = 0
        for j in range(100):
            _1D_percentage += _1D(i)
        _1D_list.append(_1D_percentage)
    for i in moves: 
        _2D_percentage = 0 
        for j in range(100):
            _2D_percentage += _2D(i)
        _2D_list.append(_2D_percentage)
    startTime = time.time()
    for i in moves: 
        _3D_percentage = 0 
        for j in range(100):
            _3D_percentage += _3D(i)
        _3D_list.append(_3D_percentage)
    endTime = time.time()
    _3D_time = endTime - startTime
    headers = ["Number of steps: ", '20', '200', '2,000', '20,000', '200,000', '2,000,000']
    data = [_1D_list,_2D_list,_3D_list]
    table = tabulate(data, headers)
    return print(f'Percentages of time particle returned to origin:\n{table}\nRun time of 3D: {_3D_time:.2f} seconds')

main()