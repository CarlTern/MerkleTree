import sys
import hashlib
import math
import subprocess

#Filen är full av löv. Första talet i filen (i) säger vilket av dessa löv vi ska hitta merkle-pathen till
#Vi ska kunna printa ut hela merkle-pathen, samt merkle-noden vid platsen som ges av andra talet i filen (j)
#Vi ska även ge merkle roten.

# Obtains all numbers from file. 
def getRows(filePath):
    nodes = []
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
        if (len(currentRow) % 2 is not 0):
            currentRow.append(currentRow[len(currentRow)-1])
        if (index % 2 is not 0):
            currentNode = hashlib.sha1(currentRow[index].encode('utf-8'))
            sibling = hashlib.sha1(currentRow[index+1].encode('utf-8'))
            node = bytes.fromhex(currentNode + sibling).hexdigest()
            newRow.append(node)
            print("Row:", node)
    fullTree.update(newRow)
    return buildTree(newRow)
        
def getFullNode(rows):
    leaf = rows[int(rows[0])+2]
    j = rows[1]
    numberOfNodesNeeded = round(math.log(len(rows)-2,2))
    answerArray = []
    #answer = recursiveTreefunction(rows,numberOfNodesNeeded, answerArray)
    #return answer 

def recursiveTreefunction(rows, rounds, answerArray):
    if (rounds is 0):
        return answerArray;
    else: 
        answerArray.append(SomeAnswer)
        return recursiveTreefunction(rows,rounds-1)

# Main method.   
if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except:
        print ("Please specify a file path")
        exit()
    result = []
    rows = getRows(path)

    fullTree = {}
    buildTree = buildTree(rows[2:], fullTree)

    fullNode = getFullNode(rows)

    #Creates a txt file with array in it, elements seperated by \n
    with open('fullMerklePath.txt', 'w') as f:
        for item in rows:
            f.write("%s\n" % item)
    
    #Run Bash script through python to run SpvNode and use the created file as input to the script to find root:

    #root = subprocess.run(["python3", "SpvNode.py", "fullMerklePath.txt"])
    
    #answer = root + fullmerklepath[len(fullmerklepath)-(rows[1]-1)]
    
    

    #root = getRoot(values)
    #print("Merkle Root:", root)