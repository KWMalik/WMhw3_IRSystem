'''
Created on 2011/11/6

@author: EE
'''
import os
import codecs
import string

class Query:
    
    number = ''
    title = ''
    question = ''
    narrative = ''
    concept = '' 
    wordcount = {} 
    relevant_list = []
       
    def __init__(self, topic):                
        self.number = topic[0].text
        self.title = topic[1].text
        self.question = topic[2].text
        self.narrative = topic[3].text
        self.concept = topic[4].text
        
    def createNGram(self):
        q_filename = 'query_ngram/' + self.number
        fout = codecs.open(q_filename, encoding='utf-8', mode='w')    
        fout.write(self.title) #The content of query!!!!
        fout.close()
        os.system('create-ngram.exe -vocab vocab.all -n 1 -o ' + q_filename + '_unigram ' + ' -encoding utf8 ' + q_filename)
        os.system('create-ngram.exe -vocab vocab.all -n 2 -o ' + q_filename + '_bigram ' + ' -encoding utf8 ' + q_filename)    
        os.system('create-ngram.exe -vocab vocab.all -n 3 -o ' + q_filename + '_trigram ' + ' -encoding utf8 ' + q_filename)
        os.system('merge-ngram.exe -o ' + q_filename +'_ngram ' + q_filename + '_unigram ' + q_filename + '_bigram ' + q_filename + '_trigram ')
        
        q_ngram = open(q_filename+'_bigram', 'r') #The ngram this query used
        linelist = q_ngram.readlines()
        for line in linelist:
            pair = line.split(' ')
            self.wordcount[pair[0]] = string.atoi(pair[1])
        q_ngram.close()