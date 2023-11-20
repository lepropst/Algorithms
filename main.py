import json
import os
import random
import sys

import numpy
import pandas as pd
from dynamic_programming.lcs import lcs
from dynamic_programming.scheduling_problem import job, schedule_jobs
from heaps.max_heap import create_max_heap
from heaps.min_heap import create_min_heap

from sorts.bin_sort import binSort, binSortLexical
from sorts.bubble_sort import BubbleSort
from sorts.insertion_sort import insertionSort

# from sorts.bucket_sort import bucketSort
from sorts.radix_sort import radixSort

from trees.avl_tree import AVLTree
from trees.binary_tree import construct_binary_tree
from trees.huffman_coding import construct_huffman_coding_tree

# from huffman_coding import huffman_coding_tree
from dynamic_programming.strassens_algorithm import pretty_print, strassen

if __name__ == "__main__":
    file = sys.argv[1]
    with open(os.path.join(os.getcwd(), file), "r") as f:
        s = f.read()

        f = json.loads(s)
    if f.get("data"):
        li = f.get("data")
        lex_li = f.get("data_lexical")
        job_li = f.get("data_jobs")
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
        # print(BubbleSort(li))
        ####### HEAPS
        # max_heap = create_max_heap(li)
        # print(max_heap)
        # min_heap = create_min_heap(li)
        # min_heap.remove()
        # # print(min_heap)

        ######## WEEK 4
        # huffman_tree = construct_huffman_coding_tree(f.get("data"))
        # huffman_tree.print_tree("huffman tree", dir="huffman")

        # job scheduling
        # jobs = [job(x.get("start")[:-1], x.get("end")[:-1]) for x in job_li]
        # schedule_jobs(jobs)
        # print(jobs)
        ######## WEEK 5
        x = numpy.array([[5, 2], [12, -3]])
        y = numpy.array([[-2, 8], [6, 3]])
        # x = numpy.array(
        #     [
        #         [5, 2, 9, 5, 4, 2],
        #         [12, 3, 4, 3, 2, 4],
        #         [12, 3, 4, 3, 2, 4],
        #         [12, 3, 4, 3, 2, 4],
        #         [12, 3, 4, 3, 2, 4],
        #         [12, 3, 4, 3, 2, 4],
        #     ]
        # )
        # y = numpy.array(
        #     [
        #         [2, 8, 5, 2, 3, 2],
        #         [6, 3, 4, 3, 2, 4],
        #         [12, 3, 4, 3, 2, 4],
        #         [12, 3, 4, 3, 2, 4],
        #         [12, 3, 4, 3, 2, 4],
        #         [12, 3, 4, 3, 2, 4],
        #     ]
        # )

        # print("MULTIPLY A and B using Strassen's method\n", "A = ")
        # pretty_print(x)
        # pretty_print(y)

        # print("RESULT:\n")
        # for l in strassen(x, y):
        #     print(l)

        # list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        # l1 = []
        # for i in range(0, 7):
        #     l1.append((random.choice(list1), random.choice(list1)))
        # l1[l1.index(max(l1))] = (
        #     l1[l1.index(max(l1))][0] + 5,
        #     l1[l1.index(max(l1))][1] + 5,
        # )
        # print(l1)
        # print(max(l1))

        obj = []
        for j in job_li:
            obj.append(
                [
                    j.get("id"),
                    j.get("start"),
                    j.get("finish"),
                    j.get("benefit"),
                ]
            )
        sequenced_jobs = pd.DataFrame(
            data=obj, columns=["id", "start", "finish", "benefit"]
        )
        print(sequenced_jobs)
        schedule = schedule_jobs(sequenced_jobs)

        exit()
