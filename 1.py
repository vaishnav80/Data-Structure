# # def tower_of_hanoi(n, source, auxiliary, destination):
# #     if n == 1:
# #         print(f"Move disk 1 from {source} to {destination}")
# #         return
# #     tower_of_hanoi(n-1, source, destination, auxiliary)
# #     print(f"Move disk {n} from {source} to {destination}")
# #     tower_of_hanoi(n-1, auxiliary, source, destination)

# # # Example usage:
# # n = 3  # Number of disks
# # tower_of_hanoi(n, 'A', 'B', 'C')


# def ensure_period(s):
#     """
#     Ensure that the string s ends with a period.
    
#     Args:
#     s (str): The input string.
    
#     Returns:
#     str: The string ending with a period.
#     """
#     # Check if the string already ends with a period
#     if not s.endswith('.'):
#         # Append a period if it does not end with one
#         s += '.'
#     return s

# print(ensure_period('dfdsfjdsfk'))


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Generate the first few prime numbers
def generate_primes(count):
    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Number of rows
rows = 4
primes = generate_primes(rows)

# Generate the pattern
for i in range(rows):
    # Select the prime number for the current row
    prime = primes[i]
    
    # Left side: descending from prime down to 1
    left_side = " ".join(str(x) for x in range(prime, 0, -1))
    
    # Right side: ascending from 1 up to prime
    right_side = " ".join(str(x) for x in range(1, prime + 1))
    
    # Calculate spaces for the middle and adjust the alignment for symmetry
    middle_space = " " * (4 * (rows - i - 1))  # Adjust spacing based on row index
    
    # Print the row with left side, middle space, and right side
    print(f"{left_side}{middle_space}{right_side}")
