def encrypt(input_string, codes):
    """
    function to map key value pairs in the dictionary to encrypt the input provided
    :param input_string: string - the input that needs to be encrypted
    :param codes: dictionary of key value pair to enable the mapping
    :return: encrypted message as a string
    """
    return_value = input_string
    for index, each_character in enumerate(input_string):
        if each_character in codes:
            return_value = return_value[:index] + str(codes[each_character]) + return_value[index + 1:]
    return return_value


def decrypt(input_string, codes):
    """
    function to decrypt the message by reversing the original dictionary to get the original message back
    :param input_string: encrypted string
    :param codes: dictionary having the original code matching pattern
    :return: decrypted message as a string
    """
    return_value = input_string
    inverse_codes = {str(v): k for k, v in codes.items()}
    for index, each_character in enumerate(input_string):
        if each_character in inverse_codes:
            return_value = return_value[:index] + str(inverse_codes[each_character]) + return_value[index + 1:]
    return return_value


# main
codes = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
print('codes: %s\n' % (codes))
input_message = "another message here!"
encrypted_input = encrypt(input_message, codes)
print('input_message: %s' % (input_message))
print('After encryption: %s' % encrypted_input)
print('After decryption: %s\n' % decrypt(encrypted_input, codes))

encrypted_input = "th3s 3s 1 m2ss1g2."
print("Encrypted input: %s" % encrypted_input)
print('After decryption: %s' % decrypt(encrypted_input, codes))
