BASE = 101
MOD = int(1e9 + 9)

def get_hash(s):
    h = 0
    for c in s:
        h = (h * BASE + ord(c)) % MOD
    return h

def get_occurrences(pattern, text):
    n = len(text)
    m = len(pattern)
    p_hash = get_hash(pattern)
    t_hash = get_hash(text[:m])
    occurrences = []
    for i in range(n - m + 1):
        if t_hash == p_hash and text[i:i+m] == pattern:
            occurrences.append(i)
        if i < n - m:
            # Update rolling hash by removing leftmost character and adding rightmost character
            t_hash = ((t_hash - ord(text[i]) * pow(BASE, m-1, MOD)) * BASE + ord(text[i+m])) % MOD
    return occurrences

def main():
    source = input().strip()
    if source == 'I':
        pattern = input().strip()
        text = input().strip()
    elif source == 'F':
        with open('tests/06') as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    else:
        print('Invalid input source')
        return
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)

def print_occurrences(occurrences):
    print(' '.join(map(str, occurrences)))

if __name__ == '__main__':
    main()

    
