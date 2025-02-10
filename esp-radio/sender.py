import network
import espnow

sta = network.WLAN(network.WLAN.IF_STA)
sta.config(channel=6) 
sta.active(True)
sta.disconnect() 

esp = espnow.ESPNow()
esp.active(True)

esp_a_mac = ""
esp_b_mac = ""
esp_c_mac = ""

esp.add_peer(esp_a_mac)
esp.add_peer(esp_b_mac)
esp.add_peer(esp_c_mac)

esp.send(esp_a_mac,"Ciao...")