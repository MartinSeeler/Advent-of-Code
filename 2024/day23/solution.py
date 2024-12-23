import time
from collections import defaultdict


def solve_part_1(text: str):
    adjacency = defaultdict(set)
    for line in text.splitlines():
        x, y = line.strip().split("-")
        adjacency[x].add(y)
        adjacency[y].add(x)

    triangles = set()
    for u in adjacency:
        for v in adjacency[u]:
            if v > u:
                # Intersect the neighbors of u and v to find nodes w that connect to both
                common_neighbors = adjacency[u].intersection(adjacency[v])
                for w in common_neighbors:
                    if w > v:  # ordering is important to count each triangle only once
                        triangle = (u, v, w)
                        triangles.add(triangle)

    return sum(
        1
        for (x, y, z) in triangles
        if x.startswith("t") or y.startswith("t") or z.startswith("t")
    )


def solve_part_2(text: str):
    adjacency = defaultdict(set)
    for line in text.splitlines():
        x, y = line.strip().split("-")
        adjacency[x].add(y)
        adjacency[y].add(x)

    def bron_kerbosch(R, P, X):
        """
        Bron–Kerbosch algorithm with pivoting to find all maximal cliques.
        Yields one maximal clique at a time.

        R: set of vertices in the current clique
        P: set of candidate vertices to expand the clique
        X: set of vertices already processed (that must not be in any clique
           formed from this call)
        """
        if not P and not X:
            # R is a maximal clique
            yield R
        else:
            # Choose a pivot (any vertex in P ∪ X)
            # The pivot is used to reduce the search space
            pivot = next(iter(P.union(X)))
            # Explore vertices outside the pivot’s adjacency (P \ N(pivot))
            for v in P - adjacency[pivot]:
                yield from bron_kerbosch(
                    R | {v},  # add v to clique
                    P & adjacency[v],  # only keep neighbors of v
                    X & adjacency[v],  # only keep neighbors of v
                )
                P.remove(v)
                X.add(v)

    all_vertices = set(adjacency.keys())

    max_clique = set()
    for clique in bron_kerbosch(set(), all_vertices, set()):
        if len(clique) > len(max_clique):
            max_clique = clique

    return ",".join(sorted(max_clique))


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        quiz_input = f.read()
        start = time.time()
        p_1_solution = int(solve_part_1(quiz_input))
        middle = time.time()
        print(f"Part 1: {p_1_solution} (took {(middle - start) * 1000:.3f}ms)")
        p_2_solution = solve_part_2(quiz_input)
        end = time.time()
        print(f"Part 2: {p_2_solution} (took {(end - middle) * 1000:.3f}ms)")
