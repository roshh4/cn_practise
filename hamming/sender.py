def text_to_binary(text):
    return ''.join(format(ord(char), '08b') for char in text)

def calculate_redundant_bits(m):
    r = 0
    while (2**r) < (m + r + 1):
        r += 1
    return r

def position_redundant_bits(data, r):
    j = 0
    k = 1
    res = ''
    for i in range(1, len(data) + r + 1):
        if i == 2**j:
            res += '0'
            j += 1
        else:
            res += data[-k]
            k += 1
    return res[::-1]

def set_parity_bits(data, r):
    n = len(data)
    for i in range(r):
        position = 2**i
        count = 0
        for j in range(1, n + 1):
            if j & position:
                count += int(data[j - 1])
        data = data[:position - 1] + str(count % 2) + data[position:]
    return data

def sender_program():
    input_text = input("Enter the text to send: ")
    binary_data = text_to_binary(input_text)
    r = calculate_redundant_bits(len(binary_data))
    data_with_redundant_bits = position_redundant_bits(binary_data, r)
    encoded_data = set_parity_bits(data_with_redundant_bits, r)

    with open("channel.txt", "w") as file:
        file.write(encoded_data)
    print("Data written to channel.txt")

if __name__ == "__main__":
    sender_program()
