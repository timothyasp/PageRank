import sys, math, random, csv, types, networkx as nx
from collections import defaultdict

"""
    Input format: 
        EvaluateCFRandom <method> <size>
            - method: Collaborative filtering method to use
            - size: number of test cases to generate

        EvaluateCFList <method> <filename>
            - method: ID of the collaborative filtering method to be used
            - filename: name of the file containing the list of test cases
                - format: (UserID, ItemID)

    Output format: 
        For each test case it prints a single line in the format below:
            userID, itemID, Actual_Rating, Predicted_Rating, Delta_Rating
            MAE Measure - printed at the end of the list

"""

def parse(filename, isDirected):
    reader = csv.reader(open(filename, 'r'), delimiter=',')
    data = [row for row in reader]

    print "Reading and parsing the data into memory..."
    if isDirected:
        return parse_directed(data)
    else:
        return parse_undirected(data)

def parse_undirected(data):
    G = nx.Graph()
    nodes = set([row[0] for row in data])
    edges = [(row[0], row[2]) for row in data]

    G.add_nodes_from(nodes)
    G.add_edges_from(edges)

    return G

def parse_directed(data):
    DG = nx.DiGraph()

    for i, row in enumerate(data):
        node_a = row[0].strip()
        node_b = row[2].strip()
        val_a = int(row[1])
        val_b = int(row[3])

        DG.add_edge(node_a, node_b)
        if val_a >= val_b:
            DG.add_path([node_a, node_b])
        else:
            DG.add_path([node_b, node_a])

    return DG

def print_results(f, method, results):
    print method

