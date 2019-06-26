from typing import List, Dict

J = [4, 4, 4, 9, 10, 11, 12]
p = 3

def gen_seq(j_list: List[int], p: int) -> Dict[float, float]:
    """Generates sequence of tuples from a list 
    and calculates the min-max averages
    """
    sequences =[]
    output = {}

    for ind, _ in enumerate(j_list):
        seq = j_list[ind:ind+p]
        if len(seq) == p:
            sequences.append(seq)
    
    avgs = [sum(sq)/len(sq) for sq in sequences]

    output['min'] = min(avgs)
    output['max'] = max(avgs)

    return output

print(gen_seq(J, p))
