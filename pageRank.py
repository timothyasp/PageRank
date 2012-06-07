import math, random, sys, csv 
from utils import parse, print_results

class PageRank:
    def __init__(self, graph):
        self.graph = graph
        self.V = len(self.graph)
        self.d = 0.85
        self.ranks = dict()
    
    def rank(self):
        for key, node in self.graph.nodes(data=True):
            self.ranks[key] = node.get('rank')

        for key, node in self.graph.nodes(data=True):
            curr_rank = node.get('rank')
            # Rank is there, but I dont know how to access the rank from the
            # neighbors.. cant get at the rank field in the object
            neighbors = self.graph[key]
            rank_sum = 0
            for n in neighbors:
                if self.ranks[n] is not None:
                    outlinks = len(self.graph.neighbors(n))
                    rank_sum += (1 / float(outlinks)) * self.ranks[n]
            
            node['rank'] = ((1 - self.d) * (1/self.V)) + self.d*rank_sum
            print node['rank']

        return p

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'Expected input format: python pageRank.py <data_filename> <directed OR undirected>'
    else:
        filename = sys.argv[1]
        isDirected = False
        if sys.argv[2] == 'directed':
            isDirected = True

        graph = parse(filename, isDirected)
        p = PageRank(graph)
        p.rank()

 #       for node in graph.nodes():
 #          print node + rank(graph, node)

            #neighbs = graph.neighbors(node)
            #print node + " " + str(neighbs)
            #print random.uniform(0,1)

def rank(graph, node):
    #V
    nodes = graph.nodes()
    #|V|
    nodes_sz = len(nodes) 
    #I
    neighbs = graph.neighbors(node)
    #d
    rand_jmp = random.uniform(0, 1)

    ranks = []
    ranks.append( (1/nodes_sz) )
    
    for n in nodes:
        rank = (1-rand_jmp) * (1/nodes_sz) 
        trank = 0
        for nei in neighbs:
            trank += (1/len(neighbs)) * ranks[len(ranks)-1]
        rank = rank + (d * trank)
        ranks.append(rank)

 
