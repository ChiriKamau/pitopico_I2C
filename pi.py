import smbus
import time

# Raspberry Pi I2C bus (bus 1 on most recent Pi models)
bus = smbus.SMBus(1)

# Pico I2C slave address
PICO_ADDRESS = 8

# Send a message to the Pico
def send_message(message):
    bus.write_i2c_block_data(PICO_ADDRESS, 0, list(message.encode()))  # Send message (encoded as bytes)

# Read a message from the Pico
def read_message():
    try:
        message = bus.read_i2c_block_data(PICO_ADDRESS, 0, 32)  # Read 32 bytes
        return ''.join(chr(i) for i in message).strip()  # Convert byte data back to string
    except Exception as e:
        print(f"Error reading: {e}")
        return ""

while True:
    # Send a message to Pico
    send_message("Hello from Pi")
    
    # Wait and read the response from Pico
    time.sleep(1)
    response = read_message()
    if response:
        print("Pico says:", response)
    
    time.sleep(1)