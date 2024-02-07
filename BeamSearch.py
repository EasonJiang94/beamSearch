import StringDouble
import ExtractGraph
# Please add comments along with your code.
class BeamSearch:

    graph = []

    def __init__(self, input_graph):
        self.graph = input_graph
        return

    def beamSearchV1(self, pre_words, beamK, maxToken):
    	# Basic beam search.
        sentence = ""
        probability = 0.0
        return StringDouble.StringDouble(sentence, probability)

    def beamSearchV2(self, pre_words, beamK, param_lambda, maxToken):
    	# Beam search with sentence length normalization.
        sentence = ""
        probability = 0.0
        return StringDouble.StringDouble(sentence, probability)
