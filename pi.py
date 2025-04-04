import smbus
import time

bus = smbus.SMBus(1)
PICO_ADDRESS = 0x08

def send_message(msg):
    try:
        data = list(msg.encode('utf-8')[:16])  # Limit to 16 bytes
        bus.write_i2c_block_data(PICO_ADDRESS, 0, data)
        print("Sent:", msg)
    except OSError as e:
        print("I2C write error:", e)

def read_message():
    try:
        response = bus.read_i2c_block_data(PICO_ADDRESS, 0, 16)
        message = ''.join(chr(byte) for byte in response).strip()
        print("Received:", message)
    except OSError as e:
        print("I2C read error:", e)

while True:
    send_message("Hello Pico")
    time.sleep(0.5)
    read_message()
    time.sleep(1)
