#made with python, this notification system uses the plyer library to send notifications, the plyer package needs to be installed before use
#it also uses tkinter to create a GUI
#an easy and straight forward way to set up a notification and even sends a reminder 5 minutes prior to the event if the duration is slightly bigger
#threading is used in order to make sure the GUI doesn't freeze when you're out of the GUI so it still works
#It basically constantly checks the correct time, sends a reminder 5 minutes prior and keeps checking until it reaches the required time and sends a notification
#this notification is then stored inside a log to check what all alarms you have and deletes them once the event is over
