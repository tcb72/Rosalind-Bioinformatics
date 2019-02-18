def modCombinations(protein_string):
    # enter stop codon at end
    protein_string += 'Z'
    # amount of times a protein corresponds to different codons
    codon_dict = {'A': 4,
             'C': 2,
             'D': 2,
             'E': 2,
             'F': 2,
             'G': 4,
             'H': 2,
             'I': 3,
             'K': 2,
             'L': 6,
             'M': 1,
             'N': 2,
             'P': 4,
             'Q': 2,
             'R': 6,
             'S': 6,
             'Z': 3,
             'T': 4,
             'V': 4,
             'W': 1,
             'Y': 2}
    # initiate as 1
    full_val = 1
    
    # get value from protein key, multiply until end of string
    for char in protein_string:
        full_val *= codon_dict[char]
    
    # modulo 1000000
    modulo = full_val % 1000000
    return(modulo)
