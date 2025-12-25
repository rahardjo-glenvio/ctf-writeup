# Extract input_list
input_list = [4, 54, 41, 0, 112, 32, 25, 49, 33, 3, 0, 0, 57, 32, 108, 23, 48, 4, 9, 70, 7, 110, 36, 8, 108, 7, 49, 10, 4, 86, 43, 110, 43, 88, 0, 67, 104, 125, 9, 78]

# Build key_str step by step (following bytecode order)
key_str = "J"
key_str = "_" + key_str
key_str = key_str + "o"
key_str = key_str + "3"
key_str = "t" + key_str

print(f"[*] Key string: {key_str}")
print(f"[*] Key string repr: {repr(key_str)}")

# Convert to list of ord values
key_list = [ord(char) for char in key_str]

# Extend until length matches input_list
while len(key_list) < len(input_list):
    key_list.extend(key_list)

# Truncate to match exact length
key_list = key_list[:len(input_list)]

print(f"[*] Input list length: {len(input_list)}")
print(f"[*] Key list length: {len(key_list)}")

# XOR operation
result = [a ^ b for a, b in zip(input_list, key_list)]

# Convert to string
result_text = ''.join(map(chr, result))

print(f"\n[+] Result: {result_text}")
