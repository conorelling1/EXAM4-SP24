# EXAM4-SP24
Conor Elling
BIO/DSP 439/539
EXAM 4

This repository contains a Python script designed to address the requirements for Exam 4 for BIO/DSP 439/539. The assignment entails the development of functions to analyze genome sequence fragments and identify subsequences of specified lengths, along with their subsequent subsequences. Below is a breakdown of the repository contents and instructions on usage.



Contents:

EXAM4PY.py: contains the implentation and testing of defined functions for the assignment. 
testfile.txt: serves as an example for the actual filename that contains the sequence fragments for analysis 

reads.fa: this file used in the code contains sequence data and was acquired from my local path "../shared/439539/reads.fa"



Usage Instructions:

Clone the repository, navigate to the repository, run tests usng "pytest EXAM4PY.py", and execute the script using "python EXAM4PY.py ../shared/439539/reads.fa"

Functionality:
1. Identify Substrings: The script defines a function to identify all substrings of a specified size k for a single sequence, along with their subsequent substrings.

2. Process Sequence Fragments: Another function is defined to read sequence fragments from a file, applying the substring identification function to each sequence.

3. Find Smallest Value of K: A function is implemented to identify the smallest value of k where every substring has only one possible subsequent substring.


The repository is structured to allow for easy execution of the provided script and tests without requiring any changes to the code

For any issues or questions, feel free to contact Conor Elling at conorelling@gmail.com



