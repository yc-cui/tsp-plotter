# python=3.7

import fileinput
import pandas as pd
import matplotlib.pyplot as plt

# change the directory below
tsp_file_dir = '/root/tsp/GA_EAX_1.0/Normal/'
sol_file_dir = '/root/tsp/GA_EAX_1.0/Normal/'


def read_coord(tsp_file_name):
    flag = False
    COORD = []
    COORD_dict = {}
    for line in fileinput.input(tsp_file_dir + tsp_file_name):
        if flag and line.replace(' ', '').replace('\n', '') != 'EOF':
            line_list = [int(i) for i in line.split(' ')]
            COORD.append(line_list)
            COORD_dict[line_list[0]] = [line_list[1], line_list[2]]
        if line.replace(' ', '').replace('\n', '') == 'NODE_COORD_SECTION':
            flag = True
    fileinput.close()
    COORD_df = pd.DataFrame(COORD)
    return COORD_df, COORD_dict


def read_sols(sol_file_name):
    sols = []
    seqs = []
    with open(sol_file_dir + sol_file_name, 'r') as f:
        lines = f.readlines()
    f.close()
    for i in range(int(len(lines) / 2)):
        sols.append(lines[i * 2].strip(' \n').split(' ')[-1])
        seqs.append([int(j) for j in lines[i * 2 + 1].strip(' \n').split(' ')])
    return sols, seqs


def plot(COORD_seq, dot_x, dot_y, title):
    COORD_seq = pd.DataFrame(COORD_seq)
    plt.scatter(x=dot_x, y=dot_y, marker='o', s=1)
    plt.plot(COORD_seq[0], COORD_seq[1], linewidth=0.5)
    plt.title(title)
    plt.show()


if __name__ == '__main__':
    tsp_file_name = 'pla7397.tsp'
    sol_file_name = 'DATA_BestSol'

    # note the instance must match the solution

    COORD_df, COORD_dict = read_coord(tsp_file_name)
    sols, seqs = read_sols(sol_file_name)

    COORD_seqs = []
    for i in range(len(seqs)):
        COORD_seq = []
        for j in range(len(seqs[i])):
            COORD_seq.append((COORD_dict[seqs[i][j]]))
        COORD_seq.append(COORD_dict[seqs[i][0]])
        COORD_seqs.append(COORD_seq)

    for i in range(len(COORD_seqs)):
        plot(COORD_seqs[i], COORD_df[1], COORD_df[2], tsp_file_name + " " + sols[i])
