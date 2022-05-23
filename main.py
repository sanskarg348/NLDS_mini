from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network


class Node:
    def __init__(self, name):
        self.name = name
        self.connections = set()
        self.visited = False


class Main:
    def __init__(self):
        self.number_of_years = int(input('Please enter number of years the exam is to be conducted for: '))
        self.year_wise_subjects = {i+1: set(input(f'Enter the subjects for the {i+1} Year: ').split()) for i in range(self.number_of_years)}
        self.num_of_slots = int(input('please enter number of exams that can be taken at one time'))
        self.slots = []
        self.x = set()
        self.subjects = set()
        self.nodes = {}
        self.order = []
        self.dic = {}
        self.curr = 0
        self.colors = {}
        self.happen()

    def happen(self):
        for i in self.year_wise_subjects.values():
            self.subjects = self.subjects.union(i)
        self.nodes = {i: Node(i) for i in self.subjects}

        for i in range(1,self.number_of_years+1):
            for j in self.year_wise_subjects[i]:
                node = self.nodes[j]
                for k in self.year_wise_subjects[i]:
                    if k != j:
                        node.connections.add(k)
        self.order = list(self.nodes.keys())
        self.dic = defaultdict(list)
        for i in self.order:
            for m,j in self.nodes.items():
                if i in j.connections:
                    self.dic[m].append(1)
                else:
                    self.dic[m].append(0)
        for i in self.order:
            if i not in self.colors.keys():
                curr_var = {i}
                self.colors[i] = self.curr
                self.curr += 1
                for j in range(len(self.dic[i])):
                    if self.dic[i][j] == 0:
                        c = 0
                        for k in curr_var:
                            if self.dic[k][j] == 0:
                                c += 1
                        if c == len(curr_var):
                            if self.order[j] not in self.colors.keys() and len(curr_var) < self.num_of_slots:
                                self.colors[self.order[j]] = self.colors[i]
                                curr_var.add(self.order[j])
        for i in range(self.curr):
            s = input(f'please enter Date of slot {i+1}') + '#' + input(f'please enter timing of slot {i+1}')
            self.slots.append(s)
        print(self.colors)
        cmap = ['red','green','blue','yellow','brown','cyan','pink','grey','magenta']
        G = nx.from_dict_of_lists({i: self.nodes[i].connections for i in self.nodes.keys()})
        nx.draw(G, node_color=[cmap[self.colors[i]-1] for i in self.order], with_labels=True)
        plt.show()
# net = Network(notebook=True)
# net.from_nx(G,)
# net.show('jatt.html')
# net.set_options()

