import operator
from collections import Counter
from submission import Submission


class SilvestreSubmission(Submission):

    def run(self, s):
        particles = self.read_input(s)

        keep_going = True
        t = 0
        last_coll_t = t
        while keep_going:
            collision_checker = Counter()
            for j, particle in enumerate(particles):
                i, p_pos, p_cel, p_acc = particle
                p_cel = tuple(map(operator.add, p_cel, p_acc))
                p_pos = tuple(map(operator.add, p_pos, p_cel))
                particles[j] = (i, p_pos, p_cel, p_acc)
                collision_checker[p_pos] += 1

            collision_detected = [p_pos for p_pos, count in collision_checker.items() if count > 1]
            if collision_detected:
                last_coll_t = t
                for coll_pos in collision_detected:
                    for i, p_pos, p_cel, p_acc in particles.copy():
                        if p_pos == coll_pos:
                            particles.remove((i, p_pos, p_cel, p_acc))

            if t - last_coll_t >= 100:
                keep_going = False
            t += 1

        return len(particles)


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
