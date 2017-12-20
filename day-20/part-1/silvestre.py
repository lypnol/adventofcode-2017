import operator
from submission import Submission


class SilvestreSubmission(Submission):

    def run(self, s):
        particles = self.read_input(s)

        d = {i : sum(map(operator.abs, particle[2])) for i, particle in enumerate(particles)}
        return min(d, key=d.get)

    def read_input(self, s):
        """
        On crée une liste de particules. Une particule est un tuple (pos, vit, acc)
        pos est un tuple (pos_x, pos,y, pos_z) etc..
        """
        particles = []
        for row in s.split("\n"):
            elements = row.split(", ")
            particle = []
            for element in elements:
                coord = element.split(",")
                particle.append((int(coord[0][3:]), int(coord[1]), int(coord[2][:-1])))
            particles.append(tuple(particle))

        return particles
