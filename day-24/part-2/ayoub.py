from runners.python import Submission
from collections import defaultdict


def get_paths(graph, path=[(0, 0)]):
    last = path[-1][1]
    for node in graph[last]:
        if (node, last) in path or (last, node) in path:
            continue
        new_path = path + [(last, node)]
        yield new_path
        yield from get_paths(graph, new_path)

class AyoubSubmission(Submission):

    def run(self, s):
        graph = defaultdict(set)
        for line in s.split('\n'):
            a, b = list(map(int, line.split('/')))
            graph[a].add(b)
            graph[b].add(a)

        max_length = 0
        max_strength = 0
        for path in get_paths(graph):
            strength = sum([x + y for (x, y) in path])
            length = len(path)
            if max_length < length:
                max_length = length
                max_strength = strength
            elif length == max_length and max_strength < strength:
                max_strength =  strength

        return max_strength