import math, random, sys, csv, networkx as nx
from utils import parse, print_results

class PageRank:
    def __init__(self, graph):
        self.graph = graph
        self.V = len(self.graph)
        self.d = 0.85
    
    def rank(self):
        for key, node in self.graph.nodes(data=True):
            curr_rank = node.get('rank')
            # Rank is there, but I dont know how to access the rank from the
            # neighbors.. cant get at the rank field in the object
            print curr_rank
            neighbors = self.graph[key]
            rank_sum = 0
            for n, val in neighbors.iteritems():
                outlinks = len(self.graph.neighbors(n))
                rank_sum += (1 / outlinks)
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

