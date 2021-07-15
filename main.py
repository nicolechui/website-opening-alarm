import time 
import webbrowser

set_alarm = input("Set the website alarm as H:M:S(all in 2 digits):")
url = input("Enter the website you want to open:")
actual_time = time.strftime("%I:%M:%S")
while (actual_time != set_alarm):
    print("The time is " + actual_time)
    actual_time = time.strftime("%I:%M:%S")
    time.sleep(1)
    if (actual_time == set_alarm):
        print("This is your web!")
        webbrowser.open(url)
