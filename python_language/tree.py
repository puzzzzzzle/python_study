from collections import defaultdict

Tree = lambda: defaultdict(Tree)

# 初始化一棵树
tree = Tree()

# 存入一些数据
tree['fruits']['apple'] = 10
tree['fruits']['pear'] = 20
tree['pets']['cat'] = 3
tree['pets']['dog'] = 1

# 树的第一层有两个分支
print(tree.keys())

# fruits子树下有两个节点
print(tree['fruits'].items())
