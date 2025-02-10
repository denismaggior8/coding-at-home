import network
import espnow

sta = network.WLAN(network.WLAN.IF_STA)
sta.config(channel=6) 
sta.active(True)
sta.disconnect() 

esp = espnow.ESPNow()
esp.active(True)

esp_a_mac = b'\x08\xd1\xf9\xe8\xdc\x84'
esp_b_mac = b'\x88\x13\xbfj\xc9\xcc'
# esp_c_mac = ""

esp.add_peer(esp_a_mac)
esp.add_peer(esp_b_mac)
# esp.add_peer(esp_c_mac)

esp.send(esp_a_mac,"Ciao...")