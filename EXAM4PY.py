from collections import defaultdict
import sys

def find_substrings(sequence, k):
    """
    Code to find all substrings of size k and their subsequent k-mers in a sequence.
    
    Arguments:
    sequence: The sequence to analyze.
    k: The length of substrings.
    
    This code returns: A dictionary where keys are substrings and values are lists of subsequent substrings.
    """
    substrings = defaultdict(list)
    for i in range(len(sequence) - k):
        substring = sequence[i:i+k]
        next_substring = sequence[i+1:i+k+1]
        if substring not in substrings:  
            substrings[substring] = []
        substrings[substring].append(next_substring)
    return substrings



def find_all_substrings(filename, k):
    """
    Code to find all possible substrings and their subsequent substrings for all sequences read from a file.
    
    Arguments:
    filename: The name of the file containing sequence fragments.
    k: The length of substrings.
    
    This code returns: A dictionary containing all substrings and their subsequent substrings for all sequences.
    """
    all_substrings = defaultdict(list)
    with open(filename, 'r') as file:
        for line in file:
            sequence = line.strip()
            substrings = find_substrings(sequence, k)
            for key, value in substrings.items():
                all_substrings[key].extend(value)
    return all_substrings

def identify_smallest_k(filename):
    """
    Code to find the smallest value of k where every substring has only one possible subsequent substring.
    
    Arguments:
    filename: The name of the file containing sequence fragments.
    
    This code returns: The smallest value of k satisfying the condition.
    """
    k = 1
    while True:
        all_substrings = find_all_substrings(filename, k)
        unique_next_substrings = {key: set(value) for key, value in all_substrings.items()}
        if all(len(next_substrings) == 1 for next_substrings in unique_next_substrings.values()):
            return k
        k += 1

def main():
    if len(sys.argv) != 2:
        print("Usage: python EXAM4PY.py <../shared/439539/reads.fa>")
        sys.exit(1)
    
    filename = sys.argv[1]
    smallest_k = identify_smallest_k(filename)
    print("Smallest value of k:", smallest_k)

if __name__ == "__main__":
    main()


# Test find_substrings function
def test_find_substrings():
    sequence = "ATGTCTGTCTGAA"
    k = 2
    actual_output = find_substrings(sequence, k)
    
    # Verify that the output is a dictionary
    assert isinstance(actual_output, dict)
    
    # Verify certain properties of the output
    assert len(actual_output) > 0  # Check that the dictionary is not empty
    for key, value in actual_output.items():
        assert isinstance(key, str)  # Check that keys are strings
        assert isinstance(value, list)  # Check that values are lists

# Test find_all_substrings function
def test_find_all_substrings():
    filename = "testfile.txt"
    k = 2
    actual_output = find_all_substrings(filename, k)
    
    # Verify that the output is a dictionary
    assert isinstance(actual_output, dict)
    
    # Verify certain properties of the output
    assert len(actual_output) > 0  # Check that the dictionary is not empty
    for key, value in actual_output.items():
        assert isinstance(key, str)  # Check that keys are strings
        assert isinstance(value, list)  # Check that values are lists

# Test identify_smallest_k function
def test_identify_smallest_k():
    filename = "testfile.txt"
    assert identify_smallest_k(filename) == 10


