import networkx as nx
import itertools
import time
import os
import matplotlib.pyplot as plt
import numpy as np

#define global variables
graph = nx.DiGraph()

def mask_list(n, mask):
    # return a list that gives res[i]==True if the i-th edge is in the graph
    res = [False] * n
    for i in mask:
        res[i] = True
    return res


def k_digraphs(n, k, ):
    '''
    generate all the directed graphs with exactly k edges
    '''
    global graph
    possible_edges =  graph.edges

    # go over all the possibilities of k edges out of all the n*(n-1) edges:
    for edge_mask in itertools.combinations(range(len(possible_edges)), k):
        # The result is already sorted
        yield tuple(edge for include, edge in zip(mask_list(len(possible_edges), edge_mask), possible_edges) if include)

def ret_and_print(graph,perm):
  # print(f'{perm=}\n{graph=}')
  ret = tuple(sorted((perm[i-1], perm[j-1]) for i, j in graph))
  return ret

def unique_motifs(n, k):
    '''
    generate all the unique graphs with exactly k edges (up to isomorphism)
    '''
    global graph
    already_seen = set()
    for k_graph in k_digraphs(n, k):
        if k_graph not in already_seen:
            # add all permutation of the current graph to the set of graphs we have already seen
            # (all permutations=all graphs isomorphic to the current one)
            currently_seen = set()
            # {
            #     ret_and_print(k_graph,perm)
            #     for perm in itertools.permutations(graph.nodes)
            # }
            c = 0
            for perm in itertools.permutations(graph.nodes):
              cur_graph = tuple(sorted((perm[i-1], perm[j-1]) for i, j in k_graph))
              cur_subgraph = graph.edge_subgraph(cur_graph)
              if len(cur_subgraph.edges)==len(cur_graph) and cur_graph not in currently_seen:
                  # print(f'{perm=}')
                  # print(f'{cur_graph=}')
                  # print(f'{graph.edge_subgraph(cur_graph).edges=}')
                  c+=1
                  currently_seen.add(cur_graph)

            already_seen |= currently_seen
            yield k_graph,c


def k_motifs(n, k):
    '''
    return all directed graphs with exactly k edges which keep the graph with n nodes connected
    '''
    # print(list(unique_motifs(n, k)))
    k_graphs = map(lambda t: (nx.DiGraph(t[0]),t[1]), unique_motifs(n, k))
    # print(list(k_graphs))
    connected_graphs = filter(lambda t: nx.is_weakly_connected(t[0]),
                              filter(lambda t: len(t[0].nodes) == n,
                                     k_graphs
                              )
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
            cur_str, cur_count = sum_k_motifs(motifs, verbose=verbose)
        str_all_motifs += cur_str
        sum += cur_count
    return str_all_motifs, sum


def sum_k_motifs(motifs, verbose=False):
    count = 0
    str_k_motifs = ''
    for motif in motifs:
        str_k_motifs += motif_to_str(motif, verbose)
        count += 1
    return str_k_motifs, count


def motif_to_str(motif, verbose=False):
    motif_str = f'#k={motif.number_of_edges()}\n'
    for u, v, d in motif.edges.data():
        motif_str += f'{u} {v}\n'
    if verbose:
        print(motif_str)
    return motif_str


def k_motifs_to_str(n, k):
    if n <= 1:
        return '', 0
    motifs = k_motifs(n, k)
    res = f'#{k}\n'
    count = 0
    for motif,c in motifs:
        edges = list(motif.edges())
        res += f'{edges} = {c}\n'
        count += 1
    if count==0:
      return '',0
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


def getNfromUser():
    N = input("Enter N: ")
    return N



def main():
    N = getNfromUser()
    # TODO:  read edges from file
    # create an empty directed graph
    global graph



    with open('edges.txt', 'r') as f:
        while True:
            # TODO: the format of the line in file is 'u v',
            edge = f.readline()

            # check if file is empty or end of file is reached
            if not edge:
                break

            # we want to obtain u and v as integers
            u, v = edge.split()
            u = int(u)
            v = int(v)

            # insert the edge to the graph
            graph.add_edge(u, v)
        # close the file
        f.close()
    # print(list(graph.edges))
    # call p1 code
    save_motifs(int(N))


if __name__ == "__main__":
    main()
