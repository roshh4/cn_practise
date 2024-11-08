import random

def receive_frames():
    with open("Sender_Buffer.txt", "r") as sender_file:
        frames = sender_file.readlines()

    expected_frame = 1
    response = ""

    print("Receiving frames:")
    for line in frames:
        # Skip empty lines or improperly formatted lines
        if not line.strip() or ": " not in line:
            continue

        try:
            frame_number, data = line.strip().split(": ")
            frame_number = int(frame_number.split()[1])
        except (ValueError, IndexError) as e:
            print(f"Skipping malformed line: '{line.strip()}'")
            continue

        if frame_number == expected_frame:
            print(f"Frame {frame_number} received correctly with data '{data}'.")
            expected_frame += 1
        else:
            print(f"Frame {frame_number} is out of order or missing. Sending NACK for frame {expected_frame}.")
            response = f"NACK {expected_frame}"
            break

    if not response:
        response = f"ACK {expected_frame}"

    with open("Receiver_Buffer.txt", "w") as receiver_file:
        receiver_file.write(response)
    print(f"Sent {response} to sender.")

if __name__ == "__main__":
    receive_frames()
