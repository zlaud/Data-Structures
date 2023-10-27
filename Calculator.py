import numpy as np
import ArrayStack
import re
import BinaryTree
import ChainedHashTable
import DLList
import operator


class Calculator:
    def __init__(self):
        self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)

    def set_variable(self, k: str, v: float):
        self.dict.add(k, v)

    def matched_expression(self, s: str) -> bool:
        left = '([{'
        right = ')]}'
        expr = ArrayStack.ArrayStack()
        for i in s:
            if i in left:
                expr.push(i)
            if i in right:
                if len(expr) == 0:
                    return False
                if right.index(i) != left.index(expr.pop()):
                    return False
        if len(expr) != 0:
            return False
        return True

    def print_expression(self, expr):
        new = []
        variables = [x for x in re.split('\W+', expr) if x.isalnum()]
        expr = re.split('(\W+)', expr)
        for i in expr:
            if i not in variables:
                new.append(i)
            elif i in variables:
                val = str(self.dict.find(i))
                if self.dict.find(i) is None:
                    new.append(i)
                else:
                    new.append(val)
        return ("".join(new))

    def _build_parse_tree(self, exp: str) -> str:
        if self.matched_expression(exp) is False:
            raise ValueError
        t = BinaryTree.BinaryTree()
        variables = [x for x in re.split('\W+', exp) if x.isalnum()]
        t.r = t.Node()
        current = t.r
        if exp[0] != '(':
            exp ="(" + exp + ")"
        pattern = r'(\(|\)|[A-Za-z0-9]+|[+\-*/])'
        exp = re.findall(pattern, exp)
        for i in exp:
            if i == '(':
                current.insert_left(t.Node())
                current = current.left
            elif i in ['+', '-', '*', '/']:
                current.set_val(i)
                current.set_key(i)
                current.insert_right(t.Node())
                current = current.right
            elif i in variables:
                current.set_key(i)
                current.set_val(self.dict.find(i))
                current = current.parent
            elif i == ')':
                current = current.parent

        return t




    def _evaluate(self, root):
        op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        if root.left is not None and root.right is not None:
            fn = op[root.k]
            return fn(self._evaluate(root.left), self._evaluate(root.right))
        elif root.left is None and root.right is None:
            if root.v is not None:
                return root.v
            raise ValueError(f'Missing value for variable {root.k}')
        elif root.left is not None:
            return self._evaluate(root.left)
        else:
            return self._evaluate(root.right)

    def evaluate(self, exp):
        parseTree = self._build_parse_tree(exp)
        return self._evaluate(parseTree.r)


