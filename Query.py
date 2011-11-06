'''
Created on 2011/11/6

@author: EE
'''
class Query:
    
    number = ''
    title = ''
    question = ''
    narrative = ''
    concept = ''
       
    def __init__(self, q):                
        self.number = q[0].text
        self.title = q[1].text
        self.question = q[2].text
        self.narrative = q[3].text
        self.concept = q[4].text
