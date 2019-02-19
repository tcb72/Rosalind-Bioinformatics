def lexOrder(letters, length):
    # permutation with repeats, and join tuple of characters as string
    string_list = [''.join(i) for i in itertools.product(letters,repeat=length)]
    return(string_list)
