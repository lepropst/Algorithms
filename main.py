import json
import os
import sys
from heaps.max_heap import create_max_heap
from heaps.min_heap import create_min_heap
from sorts.radix_sort import radixSort

from trees.avl_tree import AVLTree
from trees.binary_tree import construct_binary_tree
from trees.huffman_coding import construct_huffman_coding_tree

# from huffman_coding import huffman_coding_tree


if __name__ == "__main__":
    file = sys.argv[1]
    with open(os.path.join(os.getcwd(), file), "r") as f:
        s = f.read()

        f = json.loads(s)
    if f.get("data"):
        li = f.get("data")
        # huffman_tree = construct_huffman_coding_tree(f.get("data"))
        # huffman_tree.print_tree("huffman tree", dir="huffman")
        # root = construct_binary_tree(li)
        # root.print_tree("Saample bst")

        # root = AVLTree(li)
        # for x in li[1:]:
        #     root.insert(x)
        # root.print_tree("sample avl_tree")

        # radixSort(li)
        # max_heap = create_max_heap(li)
        # print(max_heap)
        # min_heap = create_min_heap(li)
        # print(min_heap)
        exit()
