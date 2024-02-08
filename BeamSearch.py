import math
import StringDouble
import ExtractGraph
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
            post_sentence[pre_sentence+" "+item[0]]=score + math.log(item[1]) /((length) ** param_lambda)
        return length
    
    def beamSearchV1(self, pre_words, beamK, maxToken):
        # Basic beam search.
        sentence = pre_words
        length=len(sentence)
        sentence_map={}
        sentence_map[sentence] = 0
        prev = {}
        while length<maxToken:
            post_sentence={}
            for key, value in sentence_map.items():
                if key.split(' ')[-1]=='</s>':
                    post_sentence[key] = value
                    continue
                length = self.add_top_ten_next_word(post_sentence, key, value, beamK)
            sorted_items = sorted(post_sentence.items(), key=lambda x: x[1], reverse=True)
            sentence_map = dict(sorted_items[:beamK])  
            if prev == sentence_map:
                break
            prev = sentence_map       
        sentence, probability = max(sentence_map.items(), key=lambda x: x[1])
        return StringDouble.StringDouble(sentence, probability)

    def beamSearchV2(self, pre_words, beamK, param_lambda, maxToken):
        # Beam search with sentence length normalization.
        sentence = ""+pre_words
        length=len(sentence)
        sentence_map={}
        sentence_map[sentence] = 0
        while length<maxToken:
            post_sentence={}
            for key, value in sentence_map.items():
                if key.split(' ')[-1]=='</s>':
                    continue
                length = self.add_top_ten_next_word(post_sentence, key,value,beamK, param_lambda=param_lambda)
            sorted_items = sorted(post_sentence.items(), key=lambda x: x[1], reverse=True)
            sentence_map = dict(sorted_items[:beamK])         
        sentence, probability = max(sentence_map.items(), key=lambda x: x[1])
        return StringDouble.StringDouble(sentence, probability)


if __name__ == "__main__":
    graph = ExtractGraph.ExtractGraph()
    beam_search = BeamSearch(graph)
    print("=========== V1 ===========")
    sentence_prob = beam_search.beamSearchV1("<s>", 10, 20)
    print(str(sentence_prob.score) + "\t" + sentence_prob.string)
    sentence_prob = beam_search.beamSearchV1("<s> Israel and Jordan signed the peace", 10, 40)
    print(str(sentence_prob.score) + "\t" + sentence_prob.string)
    sentence_prob = beam_search.beamSearchV1("<s> It is", 10, 15)
    print(str(sentence_prob.score) + "\t" + sentence_prob.string)
    
    print("=========== V2 ===========")
    param_lambda = 0.3
    sentence_prob = beam_search.beamSearchV2("<s>", 10, param_lambda, 20)
    print(str(sentence_prob.score) + "\t" + sentence_prob.string)
    sentence_prob = beam_search.beamSearchV2("<s> Israel and Jordan signed the peace", 10, param_lambda, 40)
    print(str(sentence_prob.score) + "\t" + sentence_prob.string)
    sentence_prob = beam_search.beamSearchV2("<s> It is", 10, param_lambda, 15)
    print(str(sentence_prob.score) + "\t" + sentence_prob.string)