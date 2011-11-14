#!/usr/bin/python
# -*- coding: <utf-8> -*-
'''
Created on 2011/11/7

@author: EE
'''
import sys
import os
import codecs
from elementtree.ElementTree import parse
from model.Query import Query
from model.Doc import Doc
import string
from util.ReadFiles import getAnswerList
import math

if len(sys.argv) == 2:
    
    #Read vocab.all
    f_vocab = codecs.open('vocab.all', 'r', encoding='utf8')
    vocab = {}
    linelist = f_vocab.readlines()
    index = 0
    for line in linelist:        
        vocab[str(index)] = line.strip()
        index = index + 1
    #print vocab
    
    #Read the answer
    ans_list = getAnswerList()[25]
    print ans_list
    
    #Get query
    xml = parse(sys.argv[1]) #argv[1] = query.xml
    q = Query(xml.getroot()[4])
    print q.title
    
    #Create ngram and count mapping for a query
    q.createNGram()
    
    #Get word count of the reference corpus
    corpus_totalcount = 0
    corpus_wordcount = {}
    corpus_ngram = open('unigram_all', 'r')
    linelist = corpus_ngram.readlines()
    for line in linelist:
        tokens = line.strip().split(' ')
        corpus_wordcount[tokens[0]] = string.atoi(tokens[1])
        corpus_totalcount = corpus_totalcount + string.atoi(tokens[1])
        
    #Find the probability for every document
    doc_list = []
    filelist = os.listdir('cirb010')
    
    for filename in filelist:        
        #create word count map
        #print filename
        d = Doc('cirb010\\' + filename)
        d.createNGram(filename)        
        doc_list.append(d)
        
        #Calculate probability            
        p = 1.0
        mu = 150.0
        d_size = 150.0
        
        param1 = 0.5
        param2 = 0.7    #increase => favor differentiation between R/NR (order of probability increases)
        param3 = 0.3   #increase => favor unseen probability    
        
        for key in q.wordcount.keys():            
            p1 = 0.0
            p2 = 0.0 
            p3 = 0.001 #smaller => recall decreases
            tokens = key.split('_')
            """
            if len(tokens) == 1: #Unigram
                if d.wordcount.has_key(key):                                
                    #p1 = (d_size / (d_size + mu)) * (float(d.wordcount[key]) / float(d.totalcount))
                    p1 = param1 * float(d.wordcount[key]) / float(d.totalcount)
                if corpus_wordcount.has_key(key):
                    #p3 = (mu / (d_size + mu)) * (float(corpus_wordcount[key]) / float(corpus_totalcount))
                    p3 = param3 * float(corpus_wordcount[key]) / float(corpus_totalcount)
            """
            if len(tokens) == 2: #Bigram
                wi = tokens[0]
                if d.wordcount.has_key(key):
                    p2 = param2 * float(d.wordcount[key]) / float(d.wordcount[wi])
                if corpus_wordcount.has_key(key):                    
                    p3 = param3 * float(corpus_wordcount[key]) / float(corpus_wordcount[wi])
               
            #p *= (p1 + p3)
            p *= (p2 + p3)
            #d.prob_word[vocab[key]] = (p1 + p3)
            #d.prob_word[vocab[key]] = (p2 + p3)
            
            #if d.docid in ans_list:
                #print d.docid
                #print vocab[key], p1
        #ppp = 1
        #for value in d.prob_word.values():
        #    ppp = ppp * value 
        #d.prob = ppp
        d.prob = p
        
        if d.docid in ans_list:
            print 'ans', d.title, d.docid, d.prob
            #print d.prob_word
        
    #Sort w.r.t. probability
    sorted_doc_list = sorted(doc_list, key=lambda doc : doc.prob, reverse=True)

    largest_doc = sorted_doc_list[0]
    
    #Get my answers
    f_ans = open('answer_test.txt', 'w')
    correct = 0.0
    my_ans = []
    for doc in sorted_doc_list:#[:len(ans_list)]:
        #f_ans.write('21 ' + doc.docid + '\n')
        if doc.prob > (10**(-5)) * largest_doc.prob: 
            my_ans.append(doc)
            print 'my', doc.title, doc.docid, doc.prob
            if doc.docid in ans_list:
                correct = correct + 1
    print 'ans size:', len(ans_list)
    print 'my_ans size:', len(my_ans)                     
    print 'accuracy:', correct/len(my_ans)
    f_ans.close()
    
else:
    print "Usage: python GetDocText [query.xml]"