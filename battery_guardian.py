import psutil
import ctypes
import winsound


def check_battery_status():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = battery.percent
    return plugged, percent

def display_notification(message):
    winsound.PlaySound("SystemDefault", winsound.SND_ALIAS)
    ctypes.windll.user32.MessageBoxW(0, message, "Battery Full", 0x40 | 0x1000 | 0x1)
    #winsound.PlaySound("SystemDefault", winsound.SND_ALIAS)


def main():
    while True:
        plugged, percent = check_battery_status()
        #print(percent)
        if plugged and percent>95:
            display_notification("Your battery is full. Please unplug the charger.")
            continue
if __name__ == "__main__":
    main()
