from submission import Submission

class SilvestreSubmission(Submission):
    """
    https://codereview.stackexchange.com/questions/108629/converting-a-list-of-arcs-into-adjacency-list-representation-for-graph-using-dic
    la v2 contient le parsing inspiré d'Ayoub bien plus court/clair que le mien
    """
    def run(self, s):
        graph = {}
        for line in s.split("\n"):
            parts = line.split()
            graph[parts[0]] = [int(parts[1][1:-1])]
            if "->" in parts:
                graph[parts[0]] = graph[parts[0]] + ''.join(parts[3:]).split(',')

        """
        Here we got a graph (a dict)
        one node example : 
        'ezar' : [48, 'rfvt', tfdc' , 'ertp']
        48 is the weight of the node
        """

        return self.find_root(graph)

    def find_root(self, graph):
        node_to_test = set(graph.keys())
        for l in graph.values(): 
            for v in l[1:] :              
                try:
                    node_to_test.remove(v)
                except KeyError:
                    pass;
        return node_to_test.pop()
        
