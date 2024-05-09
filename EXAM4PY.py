from collections import defaultdict
import sys

def find_substrings(sequence, k):
    """
    This code is used to find all substrings of size k and their subsequent k-mers in a sequence.
    
    Arguements used:
    sequence: The sequence to analyze.
    k: The length of substrings.
    
    This code returns: A dictionary where keys are substrings and values are lists of subsequent substrings.
    """
    # Creating a dictionary to store substrings and their subsequent k-mers
    substrings = defaultdict(list)
    # Iterating over the sequence to find substrings
    for i in range(len(sequence) - k):
        substring = sequence[i:i+k]
        next_substring = sequence[i+1:i+k+1]
        # This part of the function adds substrings if it is not currently in the dictonary
        if substring not in substrings:  
            substrings[substring] = []
        # This adds the subsequent k-mer to the list of subsequent k-mers for the current substring
        substrings[substring].append(next_substring)
    return substrings



def find_all_substrings(filename, k):
    """
    This code is used to find all possible substrings and their subsequent substrings for all sequences read from a file.
    
    Arguments used:
    filename: The name of the file containing sequence fragments.
    k: The length of substrings.
    
    This code returns: A dictionary containing all substrings and their subsequent substrings for all sequences.
    """
    # Creating a dictionary to store all substrings and their subsequent substrings
    all_substrings = defaultdict(list)
    # This opens the file containing sequence fragments
    with open(filename, 'r') as file:
        for line in file:
            sequence = line.strip()
            # This finds all substrings and their subsequent substrings for the current sequence
            substrings = find_substrings(sequence, k)
            # This part updates the dictionary with substrings and their subsequent substrings
            for key, value in substrings.items():
                all_substrings[key].extend(value)
    return all_substrings

def identify_smallest_k(filename):
    """
    This code is used to find the smallest value of k where every substring has only one possible subsequent substring.
    
    Arguments used:
    filename: The name of the file containing sequence fragments.
    
    This code returns: The smallest value of k satisfying the condition.
    """
    # Starting with k equaling 1
    k = 1
    # "while True" will continue looping until the condition is met
    while True:
        # Finding all substrings and their subsequent substrings for the file and k 
        all_substrings = find_all_substrings(filename, k)
        unique_next_substrings = {key: set(value) for key, value in all_substrings.items()}
        # Checking if every substring has only one possible subsequent substring
        if all(len(next_substrings) == 1 for next_substrings in unique_next_substrings.values()):
            # Finally, if the condition is met return the current value of k
            return k
        # This increases k for the next cycle
        k += 1

def main():
    """
    This is the main function that executes the script

    How to use:
    python EXAM4PY.py ../shared/439539/reads.fa

    Arguments used:
    filename: Path to the file containing sequence fragments

    """

    # Checking if correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python EXAM4PY.py <../shared/439539/reads.fa>")
        sys.exit(1)
    
    # Extracting the filename from command-line arguments
    filename = sys.argv[1]
    # Finding the smallest value of k used the provided filename
    smallest_k = identify_smallest_k(filename)
    # Printing the smallest value of k
    print("Smallest value of k:", smallest_k)

if __name__ == "__main__":
    main()


# Test find_substrings function
def test_find_substrings():
    sequence = "ATGTCTGTCTGAA"
    k = 2
    actual_output = find_substrings(sequence, k)
    
    # Verifying the output is a dictionary
    assert isinstance(actual_output, dict)
    # Checking that the dictionary is not empty
    assert len(actual_output) > 0  
    for key, value in actual_output.items():
        # Checking that keys are strings
        assert isinstance(key, str)  
        # Checking that values are lists
        assert isinstance(value, list)  

# Test find_all_substrings function
def test_find_all_substrings():
    filename = "testfile.txt"
    k = 2
    actual_output = find_all_substrings(filename, k)
    
    # Verifying that the output is a dictionary
    assert isinstance(actual_output, dict)
    # Checking that the dictionary is not empty
    assert len(actual_output) > 0  
    for key, value in actual_output.items():
        # Checking that keys are strings
        assert isinstance(key, str)  
        # Checking that values are lists
        assert isinstance(value, list) 

# Test identify_smallest_k function
def test_identify_smallest_k():
    filename = "testfile.txt"
    assert identify_smallest_k(filename) == 10

