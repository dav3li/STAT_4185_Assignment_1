

# Write Code Here
def decrypt2(file):
    encrypted_file = open(file, 'r')

    encrypted_message = encrypted_file.readline().strip()
    print(encrypted_message)
    encrypted_file.close()
    encrypted_message = list(encrypted_message)
    len_encrypted_message = len(encrypted_message)
    index_start = 1 #encrypted_message
    index_end = len_encrypted_message - 2
    print(index_start, index_end, len_encrypted_message)
    while index_start < index_end:
        encrypted_message[index_start], encrypted_message[index_end] = encrypted_message[index_end], encrypted_message[index_start]
        index_start += 2
        index_end -= 2

    return "".join(encrypted_message)

print(decrypt2("./Git_Github_HW/encrypted_message_two.txt"))

