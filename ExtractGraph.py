import re
import pprint
pp = pprint.PrettyPrinter(indent=1)

class ExtractGraph(object):

    # Please add comments along with your code.
    # key is head word; value stores next word and corresponding probability.
    graph = {}

    sentences_add = "data/assign1_sentences.txt"

    def __init__(self):
        # Extract the directed weighted graph, and save to {head_word, {tail_word, probability}}
        self.graph = {}
        self.prob = {}
        txt_lines = self.parse_txt_file(ExtractGraph.sentences_add)
        self.construct_graph(txt_lines)
        self.init_prob(show=False)
        return

    def parse_txt_file(self, txt_file_path):
        # read file and return the contents
        with open(txt_file_path, "r") as f :
            # parse every line
            lines = f.readlines()
        return lines

    def construct_graph(self, txt_lines):
        # sort the content and construct the graph by the structure of dictionary
        for line in txt_lines:
            line = line.replace('\n', '')
            words = line.split(' ')
            for i, word in enumerate(words[:-1]):
                if not word in self.graph.keys():
                    self.graph[word] = {}
                next_word = words[i+1]
                if not next_word in self.graph[word]:
                    self.graph[word][next_word] = 0
                self.graph[word][next_word] += 1
    
    def init_prob(self, show=False):
        # the part to init the prob graph
        for word in self.graph:
            if not word in self.prob:
                self.prob[word] = {}
            sum_num = sum([self.graph[word][next_word] for next_word in self.graph[word]])
            for next_word in self.graph[word]:
                self.prob[word][next_word] = self.graph[word][next_word]/sum_num
        if show:
            pp.pprint(self.prob)

    def getProb(self, head_word, tail_word):
        # the be called and return the probability
        # As the head_word/tail_word doesn't exist in the graph
        # return the probability of ZERO
        if not head_word in self.prob:
            return 0
        if not tail_word in self.prob[head_word]:
            return 0
        return self.prob[head_word][tail_word]
    
if __name__ == '__main__':
    graph = ExtractGraph()
    pp.pprint(graph.graph)