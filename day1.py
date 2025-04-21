#Grom groq
# Function to generate primes up to max_num using Sieve of Eratosthenes
def sieve_of_eratosthenes(max_num):
    # Create a boolean array "is_prime[0..max_num]" and initialize all entries as true
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    
    # Use Sieve to mark non-primes as False
    for i in range(2, int(max_num ** 0.5) + 1):
        if is_prime[i]:
            # Mark all multiples of i starting from i*i as non-prime
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
    
    # Collect all prime numbers in a list
    primes = [i for i in range(max_num + 1) if is_prime[i]]
    return primes

# Step 1: Generate all primes up to 1.5 million
max_num = 1500000  # Large enough to cover the 100,000th prime
primes = sieve_of_eratosthenes(max_num)

# Step 2: Read input N
N = int(input())

# Step 3: Find the N-th prime and compute its square
# N is 1-based, so we use primes[N-1] to get the N-th prime
nth_prime = primes[N - 1]
result = nth_prime * nth_prime  # Square the N-th prime

# Step 4: Output the result
print(result)