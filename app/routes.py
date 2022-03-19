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


def isLeaf(root):
    return root.left is None and root.right is None


class Node:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


def encode(root, s, code):

    if root is None:
        return

    if isLeaf(root):
        code[root.ch] = s if len(s) > 0 else '1'

    encode(root.left, s + '0', code)
    encode(root.right, s + '1', code)


def decode(root, index, s):

    if root is None:
        return index

    if isLeaf(root):
        print(root.ch, end='')
        return index

    index = index + 1
    root = root.left if s[index] == '0' else root.right
    return decode(root, index, s)


def compress(text):

    if len(text) == 0:
        return

    freq = {i: text.count(i) for i in set(text)}

    pq = [Node(k, v) for k, v in freq.items()]
    heapq.heapify(pq)

    while len(pq) != 1:

        left = heappop(pq)
        right = heappop(pq)

        total = left.freq + right.freq
        heappush(pq, Node(None, total, left, right))

    root = pq[0]

    code = {}
    encode(root, '', code)

    s = ''
    for c in text:
        s += code.get(c)

    return s


@app.route('/api/file/compress', methods=['GET'])
def file_compress():
    originalfilename = request.args["filename"]
    originalfile = open(originalfilename, 'rb')
    arr = list(originalfile.read())
    originalfile.close()
    originalsize = os.path.getsize(originalfile.name)
    comp = compress(arr)
    compressedfile = open("_compressed_" + originalfilename, "a")
    compressedfile.write(comp)
    compressedfile.close()
    compressedsize = os.path.getsize(compressedfile.name)

    compare = FileCompare(originalfile.name, originalsize, compressedfile.name, compressedsize)

    return compare.toJson()


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