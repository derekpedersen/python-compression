from app import app
from flask import request, jsonify, send_file
from werkzeug.utils import secure_filename

import glob
import os
import json

import heapq
from heapq import heappop, heappush

class FileCompare:
    def __init__(self, ogfilename, ogfilesize, compfilename, compfilesize):
        self.originalFileName = ogfilename
        self.originalFileSize = ogfilesize
        self.compressedFileName = compfilename
        self.compressedFileSize = compfilesize
        self.sizeDifference = (self.originalFileSize - self.compressedFileSize)

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    originalFileName = ""
    originalFileSize = 0
    compressedFileName = ""
    compressedFileSize = 0
    sizeDifference = 0


class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        self.prob = prob
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ''

codes = dict()


def _to_Bytes(data):
  b = bytearray()
  for i in range(0, len(data), 8):
    b.append(int(data[i:i+8], 2))
  return bytes(b)


def _codes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.code)

    if(node.left):
        _codes(node.left, newVal)
    if(node.right):
        _codes(node.right, newVal)

    if(not node.left and not node.right):
        codes[node.symbol] = newVal
         
    return codes        


def _probability(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) == None:
            symbols[element] = 1
        else: 
            symbols[element] += 1     
    return symbols


def _encoded(data, coding):
    encoding_output = []
    for c in data:
        encoding_output.append(coding[c])
        
    string = ''.join([str(item) for item in encoding_output])    
    return string


def _to_Huffman(data):
    symbol_with_probs = _probability(data)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    
    nodes = []
    
    # converting symbols and probabilities into huffman tree nodes
    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))
    
    while len(nodes) > 1:
        # sort all the nodes in ascending order based on their probability
        nodes = sorted(nodes, key=lambda x: x.prob)
    
        # pick 2 smallest nodes
        right = nodes[0]
        left = nodes[1]
    
        left.code = 0
        right.code = 1
    
        # combine the 2 smallest nodes to create new node
        newNode = Node(left.prob+right.prob, left.symbol+right.symbol, left, right)
    
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
            
    _to_Huffman = _codes(nodes[0])
    encoded_output = _encoded(data,_to_Huffman)
    return encoded_output 
    

@app.route('/api/file/list', methods=['GET'])
def file_list():
    typeParam = request.args.get('type', None)
    if typeParam == None:
        return jsonify(glob.glob('*.bin'))
    if request.args["type"] == "compressed":
        return jsonify(glob.glob('compressed*'))
    if request.args["type"] == "original":
        return jsonify(glob.glob('!compressed'))
    return jsonify(glob.glob('*.bin'))


@app.route('/api/file/download', methods=['GET'])
def file_download ():
    return send_file("../" + request.args["filename"], as_attachment=True)


@app.route('/api/file/upload', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))
      return jsonify(f.filename)


@app.route('/api/file/compress', methods=['GET'])
def file_compress():
    originalfilename = request.args["filename"]
    originalfile = open(originalfilename, 'rb')
    data = originalfile.read()
    originalfile.close()
    originalsize = os.path.getsize(originalfile.name)
    encoding = _to_Huffman(data)
    compressedfile = open("_compressed_" + originalfilename, 'wb')
    compressedfile.write(_to_Bytes(encoding))
    compressedfile.close()
    compressedsize = os.path.getsize(compressedfile.name)

    compare = FileCompare(originalfile.name, originalsize, compressedfile.name, compressedsize)

    return compare.toJson()
