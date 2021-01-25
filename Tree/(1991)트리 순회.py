N = int(input())
binary_tree = dict()
answer1 = list()
answer2 = list()
answer3 = list()

for _ in range(N):
    root, left, right = input().split()
    binary_tree[root] = (left, right)


def prefix(root):
    if root == '.':
        return

    answer1.append(root)
    prefix(binary_tree[root][0])
    prefix(binary_tree[root][1])


def infix(root):
    if root == '.':
        return

    infix(binary_tree[root][0])
    answer2.append(root)
    infix(binary_tree[root][1])


def postfix(root):
    if root == '.':
        return

    postfix(binary_tree[root][0])
    postfix(binary_tree[root][1])
    answer3.append(root)


prefix('A')
infix('A')
postfix('A')
print(''.join(answer1))
print(''.join(answer2))
print(''.join(answer3))
