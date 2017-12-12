from runners.python import Submission


class JulesSubmission(Submission):

    def run(self, s):
        links = {}
        for link in s.split('\n'):
            elements = link.split(' <-> ')
            first = elements[0]
            linked = set(elements[1].split(', '))
            links[first] = links.get(first, set()).union(linked)
        # print(links)
        groups = set()
        visited = set()
        for key in links:
            if key in visited:
                continue
            to_visit = set()
            to_visit.add(key)
            groups.add(key)
            while len(to_visit) > 0:
                visiting = to_visit.pop()
                if visiting not in visited:
                    visited.add(visiting)
                    to_visit = to_visit.union(links[visiting])
        return len(groups)
