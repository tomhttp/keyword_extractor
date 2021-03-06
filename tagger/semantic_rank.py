#!/usr/bin/python
#coding: utf-8
# @author: zuotaoliu@126.com
# @created: 2014-06-23
import os
import sys
import math
sys.path.append('../../jieba')
import jieba
import jieba.posseg as pseg

class SemanticTagger(object):
    legal_pos_dict = {v:1 for v in ['a', 'an', 'i', 'j', 'l', 'n', 'nr', 'ns', 'nt', 'nz']}
    
    def __init__(self):
        jieba.initialize()
        jieba.enable_parallel(8)

    def tokenize(self, text):
        # wordseg, NER, phrase
        pos_list = pseg.cut(text)
        legal_list = []
        for v in pos_list:
            w, p = v.word, v.flag 
            if len(w)>1 and p in self.legal_pos_dict:
                legal_list.append(w.encode('utf-8'))
            else:
                legal_list.append('')
        return legal_list

    def do_rank(self, w_dict):
        pass

    def rerank_by_candidate_relation(self, w_dict, relation_graph):
        # relation: adjust in doc, linguistic, semantic
        # reranking: pagerank
        return w_dict

    def rerank_by_doc_category(self, w_dict, category_term_weights):
        # reranking: score * p(term | class) * p(class | doc)
        return w_dict

    def rerank_by_task_bias(self, terms):
        # score + task_depent_bias
        return w_dict

    def get_topK(self, w_dict, K=5):
        sort_list = sorted(w_dict.items(), key=lambda d:d[1], reverse=True)
        return sort_list[:K]

    def extract_keywords(self, text, n_count=5):
        word_list = self.tokenize(text)
        w_dict = {w:1 for w in word_list} 
        self.do_rank(w_dict)
        return self.get_topK(w_dict, n_count)

def test():
    tagger = SemanticTagger()
    docs = [
            '走到哪都是一个人的旅行，不过，我相信宁可没有不了迁就！我想走遍天涯海角，直到找到属于我的她，让我可以落叶归根！',
            '1949年10月1日，中华人民共和国成立了，全球1/4的人口得到解放，百分之八十的耕地都给予农民，十几亿农民得到了实惠，120%的力气发展生产。',
            '开发者可以指定自己自定义的词典，以便包含jieba词库里没有的词。虽然jieba有新词识别能力，但是自行添加新词可以保证更高的正确率',
            ]
    for text in docs:
        print 'text:', text
        result = tagger.extract_keywords(text)
        for k, v in result: 
            print '\tkeyword:', k, v

if __name__ == '__main__':
    test()


