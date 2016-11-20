#coding:latin
from bintree import BinTree
tree=BinTree()
print("Write some words for the tree.")
while True:
    word=input()
    if word=="": break
    tree.put(word)
print("Whole tree:")
tree.write()
print ("Search for a word in the tree.")
while True:
    word=input()
    if word=="": break
    if tree.exists(word):
        print ( word,"exists in the tree!")
