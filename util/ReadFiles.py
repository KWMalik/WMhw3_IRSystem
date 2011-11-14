'''
Created on 2011/11/13

@author: EE
'''
import string

def getAnswerList(filename='answer.txt'):    
    ans = open(filename, 'r')
    all_ans = {}
    linelist = ans.readlines()
    for line in linelist:
        tokens = line.strip().split('\t')
        if not all_ans.has_key(string.atoi(tokens[0])):
            all_ans[string.atoi(tokens[0])] = []
        all_ans[string.atoi(tokens[0])].append(tokens[1])
    return all_ans
