def print_upper_words (words, must_start_with):
    """
    prints matching words in all caps
    
    Example:
    ```py 
    # this should print "HELLO", "HEY", "YO", and "YES"

    print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})
    ```
    """
    for word in words:
        if word[0] in must_start_with:
            print(f"{word.upper()} \n")
    
    
    # Add a doc string look up docstring, hint: ###
    # Make a loop, hint: for word in words
    # Check if the word starts with one of the must_start_with words
    # Print words that match, hint: with an 'fstring'


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})