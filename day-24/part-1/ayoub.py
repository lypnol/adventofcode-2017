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

        max_strength = 0
        for path in get_paths(graph):
            max_strength = max(max_strength, sum([x + y for (x, y) in path]))

        return max_strength