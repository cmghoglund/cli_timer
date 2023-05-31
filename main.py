# Simple timer that works in the terminal

import time

def timer(seconds):
    start_time = time.time()
    rounded_start_time = round(start_time)
    end_time = rounded_start_time + seconds

    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        minutes, seconds = divmod(remaining_seconds, 60)
        time_format = f"{minutes:02d}:{seconds:02d}"

        # Clear previous output by printing backspaces
        print('\b' * len(time_format), end='', flush=True)
        print(time_format, end='', flush=True)
        time.sleep(1)

    print("\n\nTimer finished!\n")

# Set the timer duration (in seconds)
duration = 5

print(f"\nTimer set for {duration} seconds.\n")
timer(duration)
