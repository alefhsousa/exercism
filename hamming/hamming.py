def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Not possible to indicate the difference between DNAs")
    
    difference = [strand_b[index] for index, letter in enumerate(strand_a) if letter != strand_b[index]]

    return len(difference)
