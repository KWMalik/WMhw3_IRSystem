'''
Created on 2011/11/6

@author: EE
'''
from elementtree.ElementTree import parse
import string

class Doc:
    """
    docid = ''
    date = ''
    title = ''
    text = '' 
    wordcount = {}
    prob = 1.0
    totalcount = 0
    prob_word = {}
    """
    
    def __init__(self, filename):
        
        xml = parse(filename)        
        doc = xml.getroot()[0]
                        
        self.docid = doc[0].text
        self.date = doc[1].text
        self.title = doc[2].text
        
        text = ''
        paragraphes = doc[3]
        for p in paragraphes:
            text += p.text
        self.text = text
        
        self.wordcount = {}
        self.prob = 1.0
        self.totalcount = 0
        self.prob_word = {}
        
    def createNGram(self, filename2):
        d_ngram = open('cirb010_ngram\\' + filename2 + '_ngram', 'r')
        linelist = d_ngram.readlines()
        for line in linelist:
            items = line.split(' ')
            #print 'items[0]', items[0]
            #print 'items[1]', items[1]              
            self.wordcount[items[0]] = string.atoi(items[1])
            self.totalcount = self.totalcount + string.atoi(items[1])
        d_ngram.close()
        #print self.wordcount
"""       
    def __init__(self, root):
        doc = root[0]
                        
        self.docid = doc[0].text
        self.date = doc[1].text
        self.title = doc[2].text
        
        text = ''
        paragraphes = doc[3]
        for p in paragraphes:
            text += p.text
        self.text = text    
"""