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
                    data.append([words[0], int(words[1][1:-1]), word])
            else :
                data.append([words[0], int(words[1][1:-1])])
        
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
        # node is root here
        node = node_to_test.pop()
        balance_info = self.get_balance_info(graph,node)
        diff = balance_info[2] - balance_info[1]

        new_diff = diff
        node = balance_info[0]
        while new_diff != 0:
            new_diff = diff
            balance_info = self.get_balance_info(graph,node)
            try:
                new_diff = abs(balance_info[1] - balance_info[2])
                node = balance_info[0]
            except TypeError :
                break

        return graph[node][0] + diff


    def get_weight(self, graph, node):
        weight = graph[node][0]

        child_nodes = graph[node][1:]
        for node in child_nodes:
            weight += self.get_weight(graph, node)

        return weight  

    def get_balance_info(self, graph, node):
        child_nodes = graph[node][1:]
        if len(child_nodes) == 0:
            return
        w = self.get_weight(graph, child_nodes[0])
        w1 = self.get_weight(graph, child_nodes[1])
        if (w == w1):
            for node in child_nodes[2:]:
                ub_w = self.get_weight(graph, node)
                if (ub_w != w):
                    return [node, ub_w, w] 
            return                
        if (w == self.get_weight(graph, child_nodes[2])):
            return [child_nodes[1], w1 ,w]
        else : 
            return [child_nodes[0], w, w1]
            
            
