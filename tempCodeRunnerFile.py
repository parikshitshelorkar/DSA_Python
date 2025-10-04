def hash_function(key):
    return sum(ord(char) for char in key) % TABLE_SIZE