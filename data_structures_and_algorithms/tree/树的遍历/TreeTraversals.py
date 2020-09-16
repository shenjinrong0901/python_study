def preorder(tree):
    if tree:
        print(tree.getRoolVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

#将前序遍历算法实现为外部函数
def preorder(self):
    print(self.key)
    if self.leftChild:
        self.leftChild.preorder()
    if self.rightChild:
        self.rightChild.preorder()

def postorder(tree):
    if tree != None:
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        print(tree.getRoolVal())


#后序遍历在求值上面的应用
def postordereval(tree):
    opers = {'+':operator.add,'-':operator.sub,\
             '*':operator.mul,'/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRoolVal()](res1,res2)
        else:
            return tree.getRoolVal()



def inorder(tree):
    if tree != None:
        preorder(tree.getLeftChild())
        print(tree.getRoolVal())
        preorder(tree.getRightChild())

#中序遍历函数应用
def printexp(tree):
    sVal = ""
    if tree:
        sVal = '(' + printexp(tree.getLeftChild())
        sVal = sVal + str(tree.getRootVal())
        sVal = sVal + printexp(tree.getRightChild()) + ')'
    return sVal