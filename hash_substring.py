# python3
def rabin_karp(pattern, text):
    # Define the hash function
    BASE = 26  # or any other prime number
    MOD = 10**9+7  # or any other large prime number
    def hash(s):
        h = 0
        for c in s:
            h = (h * BASE + ord(c)) % MOD
        return h

    # Preprocess the pattern and text
    M = len(pattern)
    N = len(text)
    pattern_hash = hash(pattern)
    text_hashes = [hash(text[i:i+M]) for i in range(N-M+1)]

    # Compare the hash values and check for matches
    matches = []
    for i, h in enumerate(text_hashes):
        if h == pattern_hash and text[i:i+M] == pattern:
            matches.append(i)

    # Output the results
    return matches

# Read input from keyboard
choice = input()
if choice == 'I':
    pattern = input().strip()
    text = input().strip()
else:
    with open('input.txt') as f:
        pattern = f.readline().strip()
        text = f.readline().strip()

# Apply the Rabin-Karp algorithm
matches = rabin_karp(pattern, text)

# Print the output
print(' '.join(str(i) for i in matches))
