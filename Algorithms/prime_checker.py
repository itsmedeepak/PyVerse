def is_prime(n: int) -> bool:
    """
    Determines whether a given number is prime.
    A prime number is a natural number greater than 1 that has no positive 
    divisors other than 1 and itself.
    
    Args:
        n: The integer to check for primality
        
    Returns:
        True if n is prime, False otherwise
    """
    
    # Handle edge cases: numbers less than or equal to 1 are not prime
    if n <= 1:
        return False
    
    # 2 and 3 are the smallest prime numbers
    if n <= 3:
        return True
    
    # Even numbers (except 2, already handled above) are not prime
    if n % 2 == 0:
        return False
    
    # Start checking odd divisors from 3
    i = 3
    
    # Mathematical reasoning: If n has a divisor greater than √n, 
    # it must also have a corresponding divisor less than √n
    # For example: if n = 36, divisors are 1,2,3,4,6,9,12,18,36
    # After √36 = 6, all divisors (9,12,18,36) have corresponding pairs below 6
    while i * i <= n:
        # Check if n is divisible by i
        if n % i == 0:
            return False  
        
        # Increment by 2 to check only odd numbers (3, 5, 7, 9, ...)
        i += 2
    
    
    return True

if __name__ == "__main__":
    
    tests = [0, 1, 2, 3, 4, 16, 17, 18, 19, 100, 101]
    for t in tests:
        print(f"{t}: {'Prime' if is_prime(t) else 'Composite'}")