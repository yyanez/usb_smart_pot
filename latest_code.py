from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD
 
__version__ = 1
firmware_url = "https://raw.githubusercontent.com/yyanez/usb_smart_pot/main"
 
ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")
ota_updater.download_and_install_update_if_available()

print("Version: " + str(__version__))
