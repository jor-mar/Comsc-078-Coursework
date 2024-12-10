def is_tree(tr):
    if type(tr) != list or len(tr) < 1:
        return False
    for branch in get_branches(tr):
        if not is_tree(branch):
            return False
    return True

def tree(label, branches = []):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def get_root(tr):
    return tr[0]

def get_branches(tr):
    return tr[1:]

def is_leaf(tr):
    return not get_branches(tr)

def count_leaves(tr):
    if is_leaf(tr):
        return 1
    else:
        return sum(count_leaves(branch) for branch in get_branches(tr))

def print_tree(tr, indent = 0):
    print('\t'*indent + str(get_root(tr)))
    for branch in get_branches(tr):
        print_tree(branch, indent = indent + 1)

def main():
    tree1 = tree(4, [tree(2, [tree(1), tree(3)]), tree(6, [tree(5)])])
    print_tree(tree1)
    print('\nNumber of leaves:', count_leaves(tree1))

if __name__ == '__main__':
    main()