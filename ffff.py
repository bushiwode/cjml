import math

def phi(n):
    """Compute the Euler totient function for n."""
    result = n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
    if n > 1:
        result -= result // n
    return result

def is_non_decreasing(seq):
    """Check if a sequence is non-decreasing."""
    for i in range(1, len(seq)):
        if seq[i] < seq[i-1]:
            return False
    return True

def longest_non_decreasing_phi_subsequence(n):
    """Find the length of the longest subsequence of {1,...,n} on which phi is non-decreasing."""
    phi_values = [phi(i) for i in range(1, n+1)]
    max_length = 0
    for i in range(n):
        for j in range(i, n):
            if is_non_decreasing(phi_values[i:j+1]):
                max_length = max(max_length, j-i+1)
    return max_length

n = 6
print(longest_non_decreasing_phi_subsequence(n))  # Output: 5

import math

def phi(n):
    """Compute the Euler totient function for n."""
    result = n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
    if n > 1:
        result -= result // n
    return result

def is_non_decreasing(seq):
    """Check if a sequence is non-decreasing."""
    for i in range(1, len(seq)):
        if seq[i] < seq[i-1]:
            return False
    return True

def longest_non_decreasing_phi_subsequence(n):
    """Find the length of the longest subsequence of {1,...,n} on which phi is non-decreasing."""
    phi_values = [phi(i) for i in range(1, n+1)]
    max_length = 0
    for i in range(n):
        for j in range(i, n):
            if is_non_decreasing(phi_values[i:j+1]):
                max_length = max(max_length, j-i+1)
    return max_length

n = 6
print(longest_non_decreasing_phi_subsequence(n))  # Output: 5


