# BioComp_Ex2
BioComp_Ex2


1. `mask_list(n, mask)`: This function takes an integer `n` and a list `mask` as input and returns a list of Boolean values. Each element in the resulting list is `True` if the corresponding index is present in the `mask` list, and `False` otherwise.

2. `k_digraphs(n, k)`: This function generates all the directed graphs with exactly `k` edges. It takes two integers `n` and `k` as input and yields tuples representing the edges of the graphs.

3. `unique_motifs(n, k)`: This function generates all the unique graphs with exactly `k` edges (up to isomorphism). It takes two integers `n` and `k` as input and yields the graphs.

4. `k_motifs(n, k)`: This function returns all directed graphs with exactly `k` edges that keep the graph with `n` nodes connected. It takes two integers `n` and `k` as input and returns the connected graphs.

5. `all_motifs(n, format='list', verbose=False)`: This function returns all graphs of `n` nodes that are connected and unique up to isomorphism. It takes an integer `n`, an optional string `format` (default is 'list'), and an optional Boolean `verbose` flag (default is `False`). It returns a string representation of the motifs and the count of how many motifs there are.

6. `sum_k_motifs(motifs, verbose=False)`: This function calculates the count of motifs and their string representation. It takes a sequence of motifs and an optional Boolean `verbose` flag (default is `False`). It returns the string representation of the motifs and the count.

7. `motif_to_str(motif, verbose=False)`: This function converts a motif (graph) to its string representation. It takes a graph `motif` and an optional Boolean `verbose` flag (default is `False`). It returns the string representation of the motif.

8. `k_motifs_to_str(n, k, verbose=False)`: This function returns the string representation of motifs with `k` edges for a graph of `n` nodes. It takes two integers `n` and `k`, and an optional Boolean `verbose` flag (default is `False`). It returns the string representation of the motifs and their count.

9. `main_n(n, format='list', verbose=False)`: This function provides the result for the question for a graph of size `n`. It takes an integer `n`, an optional string `format` (default is 'list'), and an optional Boolean `verbose` flag (default is `False`). It returns the string representation of the motifs and their count.

10. `save_motifs(n, path='.', verbose=False)`: This function saves a file with the details of a graph of `n` nodes. It takes an integer `n`, an optional string `path` representing the file path (default is '.'), and an optional Boolean `verbose` flag (default is `False`).

11. `save_motifs_range(start, end=None, path='.', verbose=False)`: This function saves a file with details on all graphs in the range `[start, end]` or `[1, start]` if `end` is `None`. It takes an integer `start`, an optional integer `end` (default is `None`), an optional string `path` representing the file path (default is '.'), and an optional Boolean `verbose` flag (default is `False`).


To run the code: the steps are the same for each part of the exercise .
1. open the .py file of part 1 or 2
2. chack that all libraries are known to the IDE
2a. If not : install them , else continue to step 3.
3. Run the code 
4. The code will generate a .txt file with the current date and time in the formt : 
5. 5. Open the file and examin the results.
