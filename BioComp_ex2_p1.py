import timeit
import networkx as nx
import itertools
import time
import os
import matplotlib.pyplot as plt
import numpy as np
import tqdm


def mask_list(n, mask):
    # return a list that gives res[i]==True if the i-th edge is in the graph
    res = [False] * (n ** 2 - n)
    for i in mask:
        res[i] = True
    return res


def k_digraphs(n, k):
    '''
    generate all the directed graphs with exactly k edges
    '''
    possible_edges = [
        (i, j) for i, j in itertools.product(range(n), repeat=2) if i != j
    ]

    # go over all the possibilities of k edges out of all the n*(n-1) edges:
    for edge_mask in itertools.combinations(range(n * n - n), k):
        # The result is already sorted
        yield tuple(edge for include, edge in zip(mask_list(n, edge_mask), possible_edges) if include)


def unique_motifs(n, k):
    '''
    generate all the unique graphs with exactly k edges (up to isomorphism)
    '''
    already_seen = set()
    for graph in k_digraphs(n, k):
        if graph not in already_seen:
            # add all permutation of the current graph to the set of graphs we have already seen
            # (all permutations=all graphs isomorphic to the current one)
            already_seen |= {
                tuple(sorted((perm[i], perm[j]) for i, j in graph))
                for perm in itertools.permutations(range(n))
            }
            yield graph


def k_motifs(n, k):
    '''
    return all directed graphs with exactly k edges which keep the graph with n nodes connected
    '''
    k_graphs = map(nx.DiGraph, unique_motifs(n, k))
    connected_graphs = filter(nx.is_weakly_connected,
                              filter(lambda g: len(g) == n,
                                     k_graphs)
                              )
    return connected_graphs


def all_motifs(n, format='list'):
    '''
    return all graphs of n nodes which are connected, that are unique up to isomorphism
    list them and the sum of how many are there
    '''
    sum = 0
    str_all_motifs = ''
    for k in range(n - 1, n ** 2 - n + 1):
        # Go over all the graphs of size k \in [n-1,n**2-n] (if k<n-1 the graph cannot be connected)
        if format == 'list':
            cur_str, cur_count = k_motifs_to_str(n, k)
        else:
            motifs = k_motifs(n, k)
            cur_str, cur_count = sum_k_motifs(motifs)
        str_all_motifs += cur_str
        sum += cur_count
    return str_all_motifs, sum


def sum_k_motifs(motifs):
    count = 0
    str_k_motifs = ''
    for motif in motifs:
        str_k_motifs += motif_to_str(motif)
        count += 1
    return str_k_motifs, count


def motif_to_str(motif):
    motif_str = f'#k={motif.number_of_edges()}\n'
    for u, v, d in motif.edges.data():
        motif_str += f'{u} {v}\n'
    return motif_str


def k_motifs_to_str(n, k, verbose=False):
    if n <= 1:
        return '', 0
    motifs = k_motifs(n, k)
    res = f'#{k}\n'
    count = 0
    for motif in motifs:
        edges = list(motif.edges())
        res += f'{edges}\n'
        count += 1
    return res, count


def main_n(n, format='list'):
    '''
    give the result for the question for graph of size n
    '''
    res_str, count = all_motifs(n, format='list')
    res_str = f'n={n}\ncount={count}\n' + res_str

    return res_str


def save_motifs(n, path='.'):
    '''
    save a file with the details of graph of n nodes
    '''
    format = 'D-%d-%m-T-%H-%M-%S'
    stamp = time.strftime(format, time.localtime())
    file_name = f'M-{n}-{stamp}.txt'
    full_path = os.path.join(path, file_name)
    with open(full_path, 'w') as f:
        f.write(main_n(n))


def save_motifs_range(start, end=None, path='.', verbose=False):
    '''
    save a file with details on all graphs in the range [start,end]
    or [1,start] if end is None
    '''
    if end is None:
        start, end = 1, start
    assert end >= start
    format = 'D-%d-%m-T-%H-%M-%S'  # D-{day}-{month}-T-{hour}-{minute}-{second}
    stamp = time.strftime(format, time.localtime())
    file_name = f'M-{start}to{end}-{stamp}.txt'  # M-{motif range}-D-{day}-T-{time of day}
    full_path = os.path.join(path, file_name)
    res = ''
    for n in range(start, end + 1):
        with open(full_path, 'a') as f:
            res = main_n(n, verbose)
            f.write(res)
            f.write('\n')

#save_motifs_range(5)


# run on different n's and save the running time
running_times = np.zeros(5)
for n in tqdm.tqdm(range(1, 6)):
    start = timeit.default_timer()
    save_motifs(n)
    end = timeit.default_timer()
    running_times[n - 1] = end - start

# plot the running time
plt.plot(range(1, 6), running_times)
plt.xlabel('n')
plt.ylabel('running time [sec]')
plt.title('running time as a function of n')
plt.show()

# save the running time to a file and note which n the running time is for
with open('running_times.txt', 'w') as f:
    f.write('n\ttime\n')
    for n, t in enumerate(running_times):
        f.write(f'{n + 1}\t{t}\n')
