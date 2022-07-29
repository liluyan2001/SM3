import hashlib
import random
import math

def Init(node_num):                     #将各项数据进行初始化
    if node_num & (node_num - 1) == 0:  # n为2的幂次
        deep = int(math.log(node_num, 2)) + 1
    else:                               # n不为2的幂次
        deep = int(math.log(node_num, 2)) + 2
    k = deep
    tree = [None] * k
    leaf_node = [None] * node_num
    data_block = [None] * node_num
    data_message = 'liluyan202022180198'
    tree[k - 1] = data_block
    k = k - 2
    for i in range(node_num):       # 生成叶子结点
        for j in range(10):
            data_message += random.choice('sducst')
        leaf_node[i] = data_message
        data_block[i] = hash_sha256('00' + data_message)
    return k,deep,tree,leaf_node,data_block

def hash_sha256(data):              #hash函数
    obj = hashlib.sha256()
    obj.update(data.encode('utf-8'))
    return obj.hexdigest()


def create_tree(node_list):         #创建Merkle Tree
    l = len(node_list)
    if l == 1:
        return node_list[0]        
    new_node_list = []
    for i in range(0, l-1, 2):      
        new_node_list.append(hash_sha256('01' + node_list[i] + node_list[i+1]))
    if l % 2 == 1:
        new_node_list.append(node_list[l-1])
    return create_tree(new_node_list)


k,deep,tree,leaf_node,data_block = Init(1000)   # 10w时间开销大，于是暂时选择了1000

root = create_tree(data_block)

#存在性证明：
hash_index = []
direction  = []


def path(m,node_num):
    global hash_index
    global data_block
    if node_num == 1:
        hash_index.append(data_block[0])
        return 0
    if node_num & (node_num - 1) == 0:
        p = 2 ** (int(math.log(node_num, 2))-1)
    else:
        p = 2 ** int(math.log(node_num, 2))
    if m < p:
        hash_index.append(create_tree(data_block[p:node_num]))
        data_block = data_block[0:p]
        new_m = m
        new_node_num = p
        direction.append(1)
    else:
        hash_index.append(create_tree(data_block[0:p]))
        data_block = data_block[p:node_num]
        new_m = m - p
        new_node_num = node_num - p
        direction.append(2)
    return path(new_m,new_node_num)
def Calculate_hash():
    l = len(hash_index)
    if l == 1:
        return hash_index[0]
    if direction[l-2] == 1:
        hash_index[l-2] = hash_sha256('01' + hash_index[l-1] + hash_index[l-2])
    else:
        hash_index[l-2] = hash_sha256('01' + hash_index[l - 2] + hash_index[l - 1])
    hash_index.pop()
    direction.pop()
    return Calculate_hash()
def existence(m,node_num):
    path(m, node_num)
    print('给定数据为：',leaf_node[m])
    proof = Calculate_hash()
    if root == proof:
        print('该叶子结点存在')
        return
    else:
        print('该叶子结点不存在')
        return
existence(4,1000)