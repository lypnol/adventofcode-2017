from submission import Submission

class SilvestreSubmission(Submission):
    """
    https://codereview.stackexchange.com/questions/108629/converting-a-list-of-arcs-into-adjacency-list-representation-for-graph-using-dic
    """
    def run(self, s):
        rows = s.split("\n")
        data = []
        for row in rows:
            words = row.split()
            if "->" in words :
                for word in words[3:]:
                    if "," in word:
                        word = word[:-1]
                    data.append([words[0], words[1][1:-1], word])
            else :
                data.append([words[0], words[1][1:-1]])
        
        graph={}

        for row in data:
            if row[0] in graph.keys() and len(row) == 3 :
                graph[row[0]].append(row[2])
            else :
                graph[row[0]]=[]
                graph[row[0]].append(row[1])
                if len(row) == 3:
                    graph[row[0]].append(row[2])

        node_to_test = set(graph.keys())
        for l in graph.values(): 
            for v in l[1:] :              
                try:
                    node_to_test.remove(v)
                except KeyError:
                    pass;
        root = node_to_test.pop()
        return root
        
