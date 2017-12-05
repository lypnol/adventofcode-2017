from submission import Submission


class MathieuSubmission(Submission):
    def run(self, s):
        square = int(s)

        # Part 1 : Find the index layer of square
        layer_nb = 1
        stop_layer = 9
        while square > stop_layer:
            layer_nb += 1
            stop_layer += 8 * layer_nb

        # Part 2 : Find the cardinal points value on this layer
        cardinal_directions = list()

        s_layer = stop_layer - layer_nb
        cardinal_directions.append(s_layer)

        o_layer = s_layer - 2 * layer_nb
        cardinal_directions.append(o_layer)

        n_layer = o_layer - 2 * layer_nb
        cardinal_directions.append(n_layer)

        e_layer = n_layer - 2 * layer_nb
        cardinal_directions.append(e_layer)

        # The distance is the index layer + minimum distance to cardinal points
        return layer_nb + min(list(abs(square - c_point) for c_point in cardinal_directions))
