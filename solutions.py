#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 07:16:48 2017
SOLUTIONS TECHNICAL INTERVIEW PRACTICE
@author: jpinzon
"""
''' 
QUESTION 1:
    Given two strings s and t, determine whether some anagram of t is a 
    substring of s. For example: if s = "udacity" and t = "ad", then the 
    function returns True. Your function definition should look like: 
    question1(s, t) and return a boolean True or False.
'''
def question1(s, t):
    import itertools
    s = s.lower()
    t = t.lower()
    anag_s = ["".join(anag_l) for anag_l in itertools.permutations(t)]
    anag_test = False
    if anag_test == False:
        for anag in anag_s:
            if anag in s:
                anag_test = True
    return anag_test

# TESTS
s = 'da'
t = 'udacity'           
print('Question 1 Test 1: \n', question1(t, s))# True

print('Question 1 Test 1: \n', question1('competition', 'attiino')) # False

print('Question 1 Test 1: \n', question1("millos", 'Mil')) # True

'''
QUESTION 2
Given a string a, find the longest palindromic substring contained in a. 
Your function definition should look like question2(a), and return a string.
'''
def question2(a):
    import string
    string_txt = ''.join(l for l in a if l not in string.punctuation).replace(' ','').lower()
    palindromes = []

    substrings = [string_txt[a:a+k] for k in range(1,1+len(string_txt)) 
                 for a in range(1+len(string_txt)-k)]
    for sub_str in substrings:
        if len(sub_str) > 1:
            if str(sub_str) == str(sub_str)[::-1]:
                palindromes.append(sub_str)
    if len(palindromes)>0:
        res = max(palindromes, key = len)
    
        return res
    else:
        print(' No palimdromes found in the string')
        return
    

# TESTS
print('Question 2 Test 1: \n', question2('ada is redivider') )
#redivider

print('Question 2 Test 2: \n', question2('redivider'))
# redivider

print('Question 2 Test 3: \n', question2('A new order began, a more Roman age bred Rowena'))
#aneworderbeganamoreromanagebredrowena

print('Question 2 Test 4:')
print(question2('House'))
#No palimdromes found in the string

'''
QUESTION 3
Given an undirected graph G, find the minimum spanning tree within G. 
A minimum spanning tree connects all vertices in a graph with the smallest 
possible total weight of edges. 
Your function should take in and return an 
adjacency list structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}

Vertices are represented as unique strings. 
The function definition should be question3(G)
'''
def question3(G):
    nodes = list(G.keys())
    mst={}
    main_node = (nodes[0])
    GM = G[main_node]
    node_ele = []

    while main_node in nodes:
        node_ele.append(main_node)
        mst[main_node]=[]
        distances = [(dist, value) for (value, dist) in GM]
        min_dist, node = min(distances)
        min_node = (node, min_dist)
        mst[main_node] = min_node
        nodes.remove(main_node)
        main_node = node
        GM = G[main_node]
        GM = [i for i in GM if i[0] not in node_ele]
        print((nodes))
        if len(GM) ==0:
            return(mst)

g1 = {'A': [('B', 2), ('C',1)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}

g2 = {'A': [('B', 3), ('E', 1), ('D',4)],
            'B': [('A', 3), ('C', 9), ('D', 2), ('E', 2)],
            'C': [('B', 9), ('D', 3), ('E', 7)],
            'D': [('B', 2), ('C', 3)],
            'E': [('A', 1), ('B', 2), ('C', 7)]}

g3 = {'A': [('B',1), ('C',2)],
             'B': [('C',1),('D',3)],
             'C': [('D',4)],
             'D': [('C',4)],
             'E': [('F',1)],
             'F': [('C',2)]}

# TESTS
print('Question 3 Test 1: \n', question3(g1))
 #{'A': ('C', 1), 'B': ('A', 2), 'C': ('B', 5)}

print('Question 3 Test 2: \n', question3(g2))
# {'A': ('E', 1), 'E': ('B', 2), 'B': ('D', 2), 'D': ('C', 3)}

print('Question 3 Test 3: \n', question3(g3))
 #{'A': ('B', 1), 'B': ('C', 1), 'C': ('D', 4)}

'''
QUESTION 4
Find the least common ancestor between two nodes on a binary search tree. 
The least common ancestor is the farthest node from the root that is an ancestor 
of both nodes. For example, the root is a common ancestor of all nodes on the 
tree, but if both nodes are descendents of the root's left child, then that 
left child might be the lowest common ancestor. You can assume that both nodes 
are in the tree, and the tree itself adheres to all BST properties. 

The function definition should look like question4(T, r, n1, n2), where T is 
the tree represented as a matrix, where the index of the list is equal to the 
integer stored in that node and a 1 represents a child node, r is a non-negative 
integer representing the root, and n1 and n2 are non-negative integers 
representing the two nodes in no particular order. For example, one test case 
might be

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.
'''
def question4(T, r, n1, n2):
    if r in (None, n1, n2):
        return r
    i, d = sorted([n1, n2])
    if r < i |r > d:
        return i
    while not  i <= r <= d:
        r = T.left if i <= r else T.right
    return r

# TESTS
print('Question 4 Test 1: \n', question4([[0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0]],
          2,
          4,
          1))
# Result = 2

print('Question 4 Test 2: \n', question4([[0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0]],
          3,
          5,
          2)) 
# Result = 3

print('Question 4 Test 3: \n', question4([[0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0]],
          3,
          3,
          1))
# Result = 3

print('Question 4 Test 4: \n', question4([[0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0],
                      [1, 0, 0, 0, 1],
                      [0, 0, 0, 0, 0]],
          3,
          5,
          4)) 
# Result = 4

'''
QUESTION 5
Find the element in a singly linked list that's m elements from the end. 
For example, if a linked list has 5 elements, the 3rd element from the end is
the 3rd element. The function definition should look like question5(ll, m), 
where ll is the first node of a linked list and m is the "mth number from 
the end". You should copy/paste the Node class below to use as a 
representation of a node in the linked list. Return the value of the node at
that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
    
'''
class node:
	def __init__(self,data=None):
		self.data=data
		self.next=None
# The following functions taken from:
# https://github.com/bfaure/Python_Data_Structures/blob/master/Linked_List/main.py

import numpy as np

class linked_list:
	def __init__(self):
		self.head=node()

	def append(self,data):
		new_node=node(data)
		cur=self.head
		while cur.next!=None:
			cur=cur.next
		cur.next=new_node

	def length(self):
		cur=self.head
		total=0
		while cur.next!=None:
			total+=1
			cur=cur.next
		return total 

	def get(self,index):
		if index>=self.length():
			print ("ERROR: 'Get' Index out of range!")
			return None
		cur_idx=0
		cur_node=self.head
		while True:
			cur_node=cur_node.next
			if cur_idx==index: return cur_node.data
			cur_idx+=1

################################
# I present two solutions for this question: question5 and question5a
            
def create_llist(i_value, n_nodes=10):
    ''' i_value = first node '''
    l = linked_list()
    l.append(i_value)
    for i in range(n_nodes-1):
        l.append(np.random.randint(0,100))
    return l

def question5(ll, m):
    l_dict={}
    l = create_llist(ll, 10)
        
    if m > l.length():
        print ('m is larger than the lenght of the list')
        return
    for i in range(0, l.length()):
        l_dict[i]=l.get(i)
    pos = l.length() - (m)
    val = l_dict[pos]
    #return (l_dict, val)
    return (val)

def question5a(ll, m):
    l = create_llist(ll, 10)
    if m > l.length():
        print ('m is larger than the lenght of the list')
        return    
    pos = l.length() - (m)
    aa = eval('l.head.next.'+'next.'*pos+'data')
    return aa


# TESTS - Results can not be given as the list is created within the function from random numbers

print('Question 5 Test 1: \n', question5(5,1)) 
# last value

print('Question 5 Test 2: \n',question5(8,10) )
# first value. should be the same as ll

print('Question 5 Test 3: \n',question5(5,11) )
# out of range node

print('Question 5 Test 4: \n',question5(3,2))

print('Question 5 Test 5: \n',question5(4,7))


print('Question 5a Test 1: \n',question5a(5,1))
# last value

print('Question 5a Test 2: \n',question5a(8,10) )
# first value. should be the same as ll

print('Question 5a Test 3: \n',question5a(5,11) )
# out of range node

print('Question 5a Test 4: \n',question5a(3,2))

print('Question 5a Test 5: \n',question5a(4,7))