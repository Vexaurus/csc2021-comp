#!/usr/bin/env python3.10

# For making it faster :P
import concurrent.futures

# For making it look nice.
from rich.progress import BarColumn, Progress, TimeRemainingColumn

def is_palindrome(string):
    """Check if a string is a palindrome"""
    return string == string[::-1]


def find_largest_palindrome(string, start, end, limit):
    """Recursively find the largest possible palindrome"""
    
    if end - start <= limit:
        # Base case
        # return a blank string if substring is too small
        return (0, 0)

    if is_palindrome(string[start:end]):
        # The current substring is a palindrome.
        return (start, end)

    # look from the left
    l_s, l_e = find_largest_palindrome(string, start, end - 1, limit)
    
    # look from the right
    r_s, r_e = find_largest_palindrome(string, start + 1, end, limit)

    # Return the larger substring
    return (l_s, l_e) if l_e - l_s > r_e - r_s else (r_s, r_e)


def palindrome_driver(string):
    """Interface for finding the largest palindrome"""

    # begin with the whole string
    start, end = find_largest_palindrome(string, 0, len(string), 5)
    
    # Return the found substring
    return string[start:end]

if __name__ == '__main__':

    # Open the file, parse each line into an array.
    with open('palindrome.txt', 'r') as inputs:
        palindromes = inputs.readlines()

    with (
        # Multi-processing rocks!
        concurrent.futures.ProcessPoolExecutor(max_workers=16) as executor,
        
        # Progress bar to make it pretty :P
        Progress(
            "{task.completed} of {task.total} palindromes searched.",
            "[progress.description]{task.description}",
            BarColumn(),
            "[progress.percentage]{task.percentage:>3.0f}%",
            "ETA approx:",
            TimeRemainingColumn(),
            transient=True,
        ) as status
    ):
        # start the task tracker
        task_tracker = status.add_task(description='Parsing palindromes', total=len(palindromes))
        
        # Starting comparison string.
        longest = ''

        # Loop through the palindromes using the multi-processing executor
        for palindrome in executor.map(palindrome_driver, palindromes, chunksize=16):
            # Code here will run whenever a task is completed.
            # so update the status bar accordingly
            status.update(task_tracker, advance=1)

            # If the palindrome found is longer then current longest replace.
            if len(palindrome) > len(longest):
                # inform the user that a new longest palindrome has been found.
                longest = palindrome
                status.console.print(f'Found a new longest! => [red]{longest}')

        # Print the final answer here.
        status.console.print (f'Final answer => [red]{longest}')
