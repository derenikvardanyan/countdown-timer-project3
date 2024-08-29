import time


def parse_time(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours}:{minutes:02}:{seconds:02}"


def countdown_timer():
    time_str = input("Insert time to count down (h:m:s): ")
    total_seconds = parse_time(time_str)

    while total_seconds >= 0:
        print(format_time(total_seconds))
        time.sleep(1)  # Wait for one second
        total_seconds -= 1


if __name__ == "__main__":
    countdown_timer()