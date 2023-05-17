import time

def timer(seconds):
    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        minutes, seconds = divmod(remaining_seconds, 60)
        time_format = '{:02d}:{:02d}'.format(minutes, seconds)

        # Clear previous output by printing backspaces
        print('\b' * len(time_format), end='', flush=True)
        print(time_format, end='', flush=True)
        time.sleep(1)

    print('\nTimer finished!')

# Set the timer duration (in seconds)
duration = 60

print(f"Timer set for {duration} seconds.")
timer(duration)
