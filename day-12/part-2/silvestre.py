from submission import Submission

class SilvestreSubmission(Submission):

    def run(self, s):
        programs = {}
        for line in s.split("\n"):
            parts = line.split(" <-> ")
            programs[parts[0]] = parts[1].split(", ")
        
        visited = set()
        n = 0
        while len(visited) < len(programs):
            to_visit = set()
            to_visit.add([x for x in programs.keys() if x not in visited][0])
            while len(to_visit) > 0:
                current_p = to_visit.pop()
                for program in programs[current_p]:
                    if program not in visited:
                        to_visit.add(program)
                    visited.add(program)
            n += 1

        return n
            