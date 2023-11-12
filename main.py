import json
import os
import sys
from heaps.max_heap import create_max_heap
from heaps.min_heap import create_min_heap
from logic.task_scheduling import schedule_tasks, task
from sorts.bin_sort import binSort, binSortLexical
from sorts.bubble_sort import BubbleSort

# from sorts.bucket_sort import bucketSort
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
        lex_li = f.get("data_lexical")
        task_li = f.get("data_tasks")
        ###### TREES
        # root = AVLTree(li)
        # for x in li[1:]:
        #     root.insert(x)
        # root.print_tree("sample avl_tree")

        # root = construct_binary_tree(li)
        # root.print_tree("Saample bst")

        ####### SORTS
        # radixSort(li)
        # print(bucketSort(li))
        # print(binSort(li))
        # print(binSortLexical(lex_li))
        print(BubbleSort(li))
        ####### HEAPS
        # max_heap = create_max_heap(li)
        # print(max_heap)
        # min_heap = create_min_heap(li)
        # min_heap.remove()
        # # print(min_heap)

        ######## WEEK 4
        # huffman_tree = construct_huffman_coding_tree(f.get("data"))
        # huffman_tree.print_tree("huffman tree", dir="huffman")

        # Task scheduling
        # tasks = [task(x.get("start")[:-1], x.get("end")[:-1]) for x in task_li]
        # schedule_tasks(tasks)
        # print(tasks)
        exit()
