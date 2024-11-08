import time

def create_frames(message):
    return [[i + 1, char] for i, char in enumerate(message)]

def send_frames(frames, window_size):
    current_frame = 0
    total_frames = len(frames)

    while current_frame < total_frames:
        # Sending frames within the current window
        window_end = min(current_frame + window_size, total_frames)
        window_frames = frames[current_frame:window_end]

        # Print and write the current window to Sender_Buffer
        print("Sending frames:")
        with open("Sender_Buffer.txt", "w") as sender_file:
            for frame in window_frames:
                print(f"Frame {frame[0]}: {frame[1]}")
                sender_file.write(f"Frame {frame[0]}: {frame[1]}\n")

        # Simulate delay while waiting for ACK
        time.sleep(2)

        # Read the Receiver_Buffer for acknowledgments
        with open("Receiver_Buffer.txt", "r") as receiver_file:
            ack_data = receiver_file.read().strip()

        # Check the ACK received
        if ack_data.startswith("ACK"):
            ack_number = int(ack_data.split()[1])
            print(f"Received ACK for frame {ack_number}.")
            current_frame = ack_number
        elif ack_data.startswith("NACK"):
            nack_number = int(ack_data.split()[1])
            print(f"Received NACK for frame {nack_number}. Retransmitting from frame {nack_number}.")
            current_frame = nack_number - 1  # Resend starting from the NACKed frame

if __name__ == "__main__":
    window_size = int(input("Enter window size: "))
    message = input("Enter the text message: ")

    frames = create_frames(message)
    send_frames(frames, window_size)
