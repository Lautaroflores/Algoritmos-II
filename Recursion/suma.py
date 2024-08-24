def pares_recursivo(n: int, i: int = 1):
    if i > n // 2:
        return
    j = n - i
    print(f"({i}, {j})")
    pares_recursivo(n, i + 1)

# Example usage:
pares_recursivo(5)
# Output:
# (1, 4)
# (2, 3)