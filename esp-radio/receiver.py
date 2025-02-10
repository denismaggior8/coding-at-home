import network
import espnow

sta = network.WLAN(network.STA_IF)
sta.config(channel=6) 
sta.active(True)
sta.disconnect()

esp = espnow.ESPNow()
esp.active(True)

print("Waiting for messages...")

while True:
    host, msg = esp.recv() 
    if msg:
        print(f"Received from {host}: {msg}")
    if msg == b'end':
        break