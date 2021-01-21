import string
import math


# Huffman Encoding

# Tree-Node Type
class Node:
    def __init__(self, freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq

    def isLeft(self):
        return self.father.left == self


# create nodes
def createNodes(freqs):
    return [Node(freq) for freq in freqs]


# create Huffman-Tree
def createHuffmanTree(nodes):
    queue = nodes[:]
    while len(queue) > 1:
        queue.sort(key=lambda item: item.freq)
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        node_father = Node(node_left.freq + node_right.freq)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        queue.append(node_father)
    queue[0].father = None
    return queue[0]


# Huffman
def huffmanEncoding(nodes, root):
    codes = [''] * len(nodes)
    for i in range(len(nodes)):
        node_tmp = nodes[i]
        while node_tmp != root:
            if node_tmp.isLeft():
                codes[i] = '1' + codes[i]
            else:
                codes[i] = '0' + codes[i]
            node_tmp = node_tmp.father
    return codes


path = '/Users/10782/Desktop/data.txt'
d_ch = []
with open(path, 'r') as text:
    while True:
        ch = text.read(1).lower()
        if not ch:
            break
        d_ch.append(ch)

    i_ch = set(d_ch)
    counts_dict = {index: d_ch.count(index) for index in i_ch}
for ch in sorted(counts_dict, key=lambda x: counts_dict[x], reverse=True):
    print('{}-{} times {}'.format(ch, counts_dict[ch], counts_dict[ch] / len(d_ch)))

nodes = createNodes([counts_dict[ch] for ch in counts_dict])
root = createHuffmanTree(nodes)
codes = huffmanEncoding(nodes, root)
ls = 0
for item in zip(counts_dict, codes):
    print('{} encode: {}'.format(item[0], item[1]))
    tem = counts_dict[item[0]] / len(d_ch)
    ls += tem * len(item[1])

hs = 0
for ch in counts_dict:
    tem = counts_dict[ch] / len(d_ch)
    hs -= tem * math.log2(tem)
print('H(s)={}  L={}'.format(hs, ls))
