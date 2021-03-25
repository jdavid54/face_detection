# fibonnacci

def bottom_up(n):
    f = [1, 1]
    for k in range(2, n):
        f.append(f[k-1]+f[k-2])
    return f[-1],f, len(f)

f = bottom_up(100)
print(f)

def k_last_digit(n, k):
    return n%10**k

d = k_last_digit(787, 2)
#print(d)

# repeating unit digit
ld = []    
for n in f[1]:
    ld.append(k_last_digit(n, 3))
print(ld)