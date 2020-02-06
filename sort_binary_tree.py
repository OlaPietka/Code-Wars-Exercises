def tree_by_levels(node):
    if node == None: return []
    
    roots = [node]
    i = 0

    while i < len(roots):
        if roots[i].left != None: roots.append(roots[i].left)
        if roots[i].right != None: roots.append(roots[i].right)
        i += 1
        
    return [i.value for i in roots]