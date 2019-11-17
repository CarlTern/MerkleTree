import sys
import hashlib

# Obtains all numbers from file. 
def getNodes(filePath):
    try:
        file = open(filePath, "r")
        nodes = file.read().splitlines()
        file.close()
        return nodes
    except:
        print("No file found with name:", filePath)
        exit()

def getRoot(nodes):
    currentNode = bytes.fromhex(nodes[0])
    for index in range(len(nodes)):
        if (nodes[index][0] is "L"):
            leftNode = bytes.fromhex(nodes[index][1:])
            currentNode = bytes.fromhex(hashlib.sha1(leftNode + currentNode).hexdigest())
        elif (nodes[index][0] is "R"):
            rightNode = bytes.fromhex(nodes[index][1:])
            currentNode = bytes.fromhex(hashlib.sha1(currentNode + rightNode).hexdigest())

    return currentNode.hex()


# Main method.   
if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except:
        print ("Please specify a file path")
        exit()
    result = []
    nodes = getNodes(path)
    root = getRoot(nodes)
    print(root)