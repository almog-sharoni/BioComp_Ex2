#import BioComp_ex2_p
import itertools
import networkx as nx


def getNfromUser():
    N = input("Please enter the number of sequences you want to generate: ")
    return N


def main():
    N = getNfromUser()
    # TODO:  read edges from file
    # create an empty directed graph
    graph = nx.DiGraph()


    with open('edges.txt', 'r') as f:
        while True:
            edge = f.readline()
            # check if file is empty or end of file is reached
            if not edge:
                break
            # TODO: the format of the line in file is 'u v',
            # we want to obtain u and v as integers
            u, v = edge.split()
            u = int(u)
            v = int(v)
            # insert the edge to the graph
            graph.add_edge(u, v)
        # close the file
        f.close()



    # print the edges
    print(graph.edges())


if __name__ == "__main__":
    main()
