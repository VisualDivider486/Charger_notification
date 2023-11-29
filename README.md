# Charger_notification

battery_guardian.py is a Python script designed to help users extend their laptop battery's lifespan and prevent overheating by notifying them when their battery is fully charged. This script monitors the battery status and displays a notification when the battery reaches full charge, encouraging the user to unplug the charger and avoid overcharging.

## How It Works
Battery Guardian utilizes the psutil library to monitor the laptop's battery status. When the battery is fully charged and the laptop is plugged in, the script triggers a notification, reminding the user to disconnect the charger and conserve battery health. The notification is displayed using a message box, and it's accompanied by a sound alert to ensure that the user notices it promptly.

Add the .exe file to the startup file in order to start automatically as the laptop powers up

Defaults are  
40% low battery   
               80% for charged  
               (Those are the advised percentages of removing and plugging in the charger)
