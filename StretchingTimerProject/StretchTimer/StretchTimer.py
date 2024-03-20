
# Ask the user for the amount of stretches, seconds of stretch, and seconds of rest. 
# Then, the program will start a timer for the amount of stretches, and for each stretch, it will start a timer for 
# the amount of seconds of stretch and then for the amount of seconds of rest.

# There should be a bell/sound at the end of each stretch and rest period.
# And a final bell/sound at the end of the last stretch...
# The user's setting should be saved between sessions.
# The program should have commands for changing the setting... or starting the timer

import time
import winsound
import pickle

# Load settings
try:
    with open('settings.pkl', 'rb') as f:
        stretches, stretch_seconds, rest_seconds = pickle.load(f)
except (FileNotFoundError, EOFError):
    stretches, stretch_seconds, rest_seconds = 3, 30, 15

# Ask the user for the amount of stretches, seconds of stretch, and seconds of rest
stretches = int(input("Enter the number of stretches: "))
stretch_seconds = int(input("Enter the number of seconds for each stretch: "))
rest_seconds = int(input("Enter the number of seconds for each rest period: "))

# Save settings
with open('settings.pkl', 'wb') as f:
    pickle.dump((stretches, stretch_seconds, rest_seconds), f)

# Start the timer
for i in range(stretches):
    print(f"Stretch {i+1} of {stretches}. Stretch for {stretch_seconds} seconds.")
    time.sleep(stretch_seconds)
    winsound.Beep(440, 500)  # Play a beep sound

    if i < stretches - 1:  # Don't rest after the last stretch
        print(f"Rest for {rest_seconds} seconds.")
        time.sleep(rest_seconds)
        winsound.Beep(440, 500)  # Play a beep sound

print("All stretches completed!")
winsound.Beep(440, 500)  # Play a beep sound

