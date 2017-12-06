from submission import Submission

class SilvestreSubmission(Submission):

    def run(self,s):
        m = list(map(int,s.split("\t")))
        loop = False
        count =0
        state = [m.copy()]
        while loop is False:
            m = self.reallocate_memory(m)
            loop = m in state
            state.append(m.copy())
            count += 1
        return count

    def reallocate_memory(self, m):
        max_v = max(m)
        max_i = m.index(max_v)
        m[max_i] = 0
        for i in range(1, max_v+1):
            m[(max_i+i) % len(m)] += 1
        return m
