# Alexander Allison - alexande.allison@ufl.edu
def encode(original_pass_string):
    decoded_pass_list = []
    # convert to decoded list of ints
    for num in original_pass_string:
        x = int(num)
        decoded_pass_list.append(x)
    encoded_pass_list = []
    for num in decoded_pass_list:
        if num < 7:
            encoded_pass_list.append(num + 3)
        else:  # num is > 6 (7,8,9)
            encoded_num = (num + 3) % 10  # last digit of 2-digit number
            encoded_pass_list.append(encoded_num)
    encoded_string = ''
    for num in encoded_pass_list:
        encoded_string += str(num)
    return encoded_string

# add decode() function here


if __name__ == '__main__':
    selector = None
    encoded_pass = None
    original_pass = None
    decoded_pass = None
    while selector != '3':
        print("Menu\n-------------")
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')

        selector = input('Please enter an option: ')
        if selector == '1':
            original_pass = input('Please enter your password to encode: ')
            encoded_pass = encode(original_pass)
            print('Your password has been encoded and stored!\n')
            pass
        if selector == '2':
            decoded_pass = decode(encoded_pass)
            print(f'The encoded password is {encoded_pass}, and the original password is {decoded_pass}.\n')
            pass
