import math
import StringDouble
import ExtractGraph
import pprint 
pp = pprint.PrettyPrinter(indent=1)

# Please add comments along with your code.
class BeamSearch:
    graph = []
    def __init__(self, input_graph):
        self.graph = input_graph
        return

    def add_top_ten_next_word(self, post_sentence, pre_sentence, score, beamK, param_lambda=0):
        ## calculate the scores of top beamK next words with highest prob
        ## add the completed sentence into post sentence
        ## the param_lambda is used to lengh-normalized score
        preword=pre_sentence.split(' ')[-1]
        length=len(pre_sentence.split(' '))
        length = length + 1
        top_ten = sorted(self.graph.prob[preword].items(), key=lambda x: x[1], reverse=True)[:beamK]
        for item in top_ten:
            post_sentence[pre_sentence+" " + item[0]] = \
                (score + math.log(item[1])) /((length) ** param_lambda)
        return length
    
    def beamSearch(self, pre_words, beamK, maxToken, param_lambda=0):
        # Basic beam search.
        sentence = pre_words
        length=len(sentence)
        sentence_map={}
        sentence_map[sentence] = 0
        prev = {}
        while length < maxToken:
            post_sentence={}
            for key, value in sentence_map.items():
                if key.split(' ')[-1]=='</s>':
                    post_sentence[key] = value
                    continue
                length = self.add_top_ten_next_word(post_sentence, key, value, beamK, param_lambda=param_lambda)
            sorted_items = sorted(post_sentence.items(), key=lambda x: x[1], reverse=True)
            sentence_map = dict(sorted_items[:beamK])  
            if prev == sentence_map:
                break
            prev = sentence_map       
        sentence, probability = max(sentence_map.items(), key=lambda x: x[1])
        return StringDouble.StringDouble(sentence, probability)

    def beamSearchV1(self, pre_words, beamK, maxToken):
        return self.beamSearch(pre_words, beamK, maxToken)

    def beamSearchV2(self, pre_words, beamK, param_lambda, maxToken):
        # Beam search with sentence length normalization.
        return self.beamSearch(pre_words, beamK, maxToken, param_lambda=param_lambda)


if __name__ == "__main__":
    graph = ExtractGraph.ExtractGraph()
    beam_search = BeamSearch(graph)
    plist = [0, 0.3, 0.5, 0.7, 0.99]
    for param_lambda in plist:
        print(f"[{param_lambda = }]")
        prefix = "<s> It was"
        print(f"pre_word = {prefix}")
        sentence_prob = beam_search.beamSearchV2(prefix, 10, param_lambda, 20)
        print(str(sentence_prob.score) + "\t" + sentence_prob.string)
        prefix = "<s> The weather"
        print(f"pre_word : {prefix}")
        sentence_prob = beam_search.beamSearchV2(prefix, 10, param_lambda, 40)
        print(str(sentence_prob.score) + "\t" + sentence_prob.string)
        prefix = "<s> I"
        print(f"pre_word = {prefix}")
        sentence_prob = beam_search.beamSearchV2(prefix, 10, param_lambda, 15)
        print(str(sentence_prob.score) + "\t" + sentence_prob.string)