import operator
from submission import Submission


class SilvestreSubmission(Submission):

    def run(self, s):
        particles = self.read_input(s)

        FRAME = 1000
        t = 0
        while t < FRAME:
            for i, p_pos, p_cel, p_acc in particles:
                p_cel = tuple(map(operator.add, p_cel, p_acc))
                p_pos = tuple(map(operator.add, p_pos, p_cel))
                particles[i] = (i, p_pos, p_cel, p_acc)

            t += 1

        result = {i : sum(map(operator.abs, particle[1])) for i, particle in enumerate(particles)}
        return min(result, key=result.get)

    def read_input(self, s):
        """
        On crée une liste de particules. Une particule est un tuple (i, pos, vit, acc)
        pos est un tuple (pos_x, pos,y, pos_z) etc..
        """
        particles = []
        for i, row in enumerate(s.split("\n")):
            elements = row.split(", ")
            particle = [i]
            for element in elements:
                coord = element.split(",")
                particle.append((int(coord[0][3:]), int(coord[1]), int(coord[2][:-1])))
            assert len(particle) == 4, f'{particle}'
            particles.append(tuple(particle))

        return particles
