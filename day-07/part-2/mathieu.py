from runners.python import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        inputs = [line.replace(',', '').split() for line in s.split('\n')]
        weights, sons, root = self.extract(inputs)
        total_weights = dict()
        for program in weights:
            total_weights[program] = self.total_weights(program, weights, sons)
        wrong_programs = self.wrong_weight(total_weights, weights, sons)
        print(wrong_programs)
        return min(wrong_programs, key=lambda x: x[0])[1]

    def extract(self, inputs):
        weights = dict()
        sons = dict()
        children = set()
        for line in inputs:
            weights[line[0]] = int(line[1].replace('(', '').replace(')', ''))
            if len(line) > 2:
                sons[line[0]] = set()
                for son in line[3:]:
                    sons[line[0]].add(son)
                    children.add(son)
        return weights, sons, (set(weights.keys()) - set(children)).pop()

    def total_weights(self, program, weights, sons):
        res = 0
        if program in sons:
            for sub_program in sons[program]:
                res += self.total_weights(sub_program, weights, sons)
        return weights[program] + res

    def wrong_weight(self, total_weights, weights, sons):
        wrong_programs = []
        for program in sons:
            total_weights_son = [(subprogram, total_weights[subprogram]) for subprogram in sons[program]]
            sub_max, max_son = max(total_weights_son, key=lambda x: x[1])
            sub_min, min_son = min(total_weights_son, key=lambda x: x[1])
            if max_son - min_son:
                wrong_programs.append((max_son, weights[sub_max] - max_son + min_son))
        return wrong_programs
