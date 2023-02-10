def generate_binary_strings(n, string=""):
    if n == 0:
        print(string)
        return
    generate_binary_strings(n-1, string + "0")
    generate_binary_strings(n-1, string + "1")

# Example usage
n = 3
generate_binary_strings(n)

# Output:
# 000
# 001
# 010
# 011
# 100
# 101
# 110
# 111
