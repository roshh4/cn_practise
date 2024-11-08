def calculate_redundant_bits(m):
    r = 0
    while (2**r) < (m + r + 1):
        r += 1
    return r

def detect_error(data, r):
    n = len(data)
    error_position = 0
    for i in range(r):
        position = 2**i
        count = 0
        for j in range(1, n + 1):
            if j & position:
                count += int(data[j - 1])
        if count % 2 != 0:
            error_position += position
    return error_position

def remove_redundant_bits(data, r):
    result = ''
    j = 0
    for i in range(1, len(data) + 1):
        if i != 2**j:
            result += data[i - 1]
        else:
            j += 1
    return result

def binary_to_text(binary_data):
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    return ''.join(chr(int(char, 2)) for char in chars)

def receiver_program():
    with open("channel.txt", "r") as file:
        received_data = file.read()

    r = calculate_redundant_bits(len(received_data) - 1)
    error_position = detect_error(received_data, r)

    if error_position:
        print(f"Error detected at position: {error_position}")
    else:
        print("No errors detected.")
        corrected_data = remove_redundant_bits(received_data, r)
        original_text = binary_to_text(corrected_data)
        print("Original text:", original_text)

if __name__ == "__main__":
    receiver_program()
