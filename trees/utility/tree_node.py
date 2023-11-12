import graphviz


class Node:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val, comparator=lambda x, y: x < y):
        if not self.val:
            self.val = val
            return
        if self.val == val:
            return
        if comparator(val, self.val):
            if self.left:
                self.left.insert(val)
                return
            self.left = Node(val)
            return
        if self.right:
            self.right.insert(val)
            return
        self.right = Node(val)
        self.print_tree(f"{val}/after_insert")

    def delete(self, val):
        self.print_tree(f"{val}/before_delete")

        print(f"deleting {val} using right sub-tree")
        if self == None:
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
            return self
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
            return self
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        self.print_tree(f"{val}/after_delete")

        return self

    def inorder_traverse(self, vals):
        if self.left is not None:
            self.left.inorder_traverse(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder_traverse(vals)

        return vals

    def preorder_traverse(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder_traverse(vals)
        if self.right is not None:
            self.right.preorder_traverse(vals)
        return vals

    def postorder_traverse(self, vals):
        if self.left is not None:
            self.left.postorder_traverse(vals)
        if self.right is not None:
            self.right.postorder_traverse(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals

    # def print_tree(self, string):
    # 	dot = graphviz.Digraph(comment=string)
    # 	dot.node(str(self.val))

    # 	def add_nodes_edges(node):
    # 		if node.left:
    # 			dot.node(str(node.left.val))
    # 			dot.edge(str(node.val), str(node.left.val))
    # 			add_nodes_edges(node.left)
    # 		if node.right:
    # 			dot.node(str(node.right.val))
    # 			dot.edge(str(node.val), str(node.right.val))
    # 			add_nodes_edges(node.right)

    # 	add_nodes_edges(self)
    # 	dot.render(string, view=True, format='png', directory="./graph_images/binary-search-tree")

    def print_tree(self, string, dir="default", key=lambda x: x.val):
        dot = graphviz.Digraph(comment=string)

        dot.node(str(key(self)))
        accessed_node = self

        def add_nodes_edges(accessed_node):
            if accessed_node.left:
                dot.node(str(key(accessed_node.left)))
                dot.edge(str(key(accessed_node)), str(key(accessed_node.left)))
                add_nodes_edges(accessed_node.left)
            if accessed_node.right:
                dot.node(str(key(accessed_node.right)))
                dot.edge(str(key(accessed_node)), str(key(accessed_node.right)))
                add_nodes_edges(accessed_node.right)

        add_nodes_edges(accessed_node)
        dot.render(string, format="png", directory=f"./graph_images/{dir}", view=False)
