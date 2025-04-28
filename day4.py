def validate_password(password):
    """
    Write your logic here.
    Parameters:
        password (list): List of integers representing the password elements
    Returns:
        tuple: A tuple containing a string ("VALID" or "INVALID") and an integer (the most frequent element)
    """
    pass


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])  # First input is the integer N
    password = list(map(int, data[1:]))  # Remaining input is the password array
    
    # Call user logic function
    validation_result, most_frequent_element = validate_password(password)
    
    # Print the output
    print(validation_result)
    print(most_frequent_element)

if __name__ == "__main__":
    main()