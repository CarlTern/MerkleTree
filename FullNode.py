import sys
import hashlib
import math
import subprocess
#Filen är full av löv. Första talet i filen (i) säger vilket av dessa löv vi ska hitta merkle-pathen till
#Vi ska kunna printa ut hela merkle-pathen, samt merkle-noden vid platsen som ges av andra talet i filen (j)
#Vi ska även ge merkle roten.

# Obtains all numbers from file. 
def getRows(filePath):
    try:
        file = open(filePath, "r")
        rows = file.read().splitlines()
        file.close()
        return rows
    except:
        print("No file found with name:", filePath)
        exit()

def buildTree(currentRow,fullTree):
    newRow = []
    if (len(currentRow) is 1):
        return fullTree
    for index in range(len(currentRow)):
        if (len(currentRow) % 2 is not 0 and currentRow[-1] is currentRow[index]):
            currentRow.append(currentRow[-1]) 
        if (index % 2 is 0):
            node = bytes.fromhex(currentRow[index] + currentRow[index+1])
            node = hashlib.sha1(node).hexdigest()
            #node = hashlib.sha1(currentNode + sibling).hexdigest()
            newRow.append(node)
    fullTree.append(newRow)

    return buildTree(newRow,fullTree)

def getSiblingAndParent(leaf, level):
    if(leaf[0] is ("R" or "L")):
        leaf[0] = ""
    for index in range(len(level)):
        if (len(level) % 2 is not 0 and level[-1] is level[index] and leaf is level(index)): # If odd, is the last and leaf equals the current
            parent = level[index]
            return ["R" + level[index], level[index]]
        if (index % 2 is 0):
            sibling1 = level[index]
            sibling2 = level[index + 1]
            parent = hashlib.sha1(bytes.fromhex(sibling1 + sibling2)).hexdigest()
            if(sibling1 == leaf):
                return ["R" + sibling2, parent]
            elif(sibling2 == leaf):
                return ["L" + sibling1, parent]

def getMerklePath(leaf, tree):
    merklePath = []
    merklePath.append(leaf)
    tree.pop() # We are not interested in the root. 
    for level in tree:
        result = getSiblingAndParent(leaf, level)
        merklePath.append(result[0]) # Add the sibling
        leaf = result[1] # Update the leaf
    return merklePath

# Main method.   
if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except:
        print ("Please specify a file path")
        exit()
    result = []
    rows = getRows(path)
    i = int(rows[0])
    j = int(rows[1])
    tree = buildTree(rows[2:], [rows[2:]])
    merklePath = getMerklePath(rows[2 + i], tree)
    merklePathNode = merklePath[-j]

    #Creates a txt file with array in it, elements seperated by \n
    with open('fullMerklePath.txt', 'w') as f:
        for line in merklePath:
            f.write("%s\n" % line)
    
    merkleRoot = subprocess.run(["python3", "SpvNode.py", "fullMerklePath.txt"], stdout=subprocess.PIPE).stdout.decode('utf-8') # Run the program and obatin the merkleRoot
    merkleRoot = merkleRoot.replace("\n", "")
    print("Answer:", merklePathNode + merkleRoot)
