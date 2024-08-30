#!/usr/bin/python3
""" Log parsing """
import sys
import signal

# Initialize variables
total_size = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_stats():
    """Print the current statistics."""
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handle the keyboard interruption (CTRL + C) and print stats."""
    print_stats()
    sys.exit(0)


# Setting the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        # Splitting and parse the line
        parts = line.split()
        if len(parts) < 7:
            continue

        ip_address = parts[0]
        date = parts[3][1:]  # Stripping the '['
        request = parts[5] + " " + parts[6] + " " + parts[7]
        status_code = parts[-2]
        file_size = parts[-1]

        # Checking if the line format is correct
        if request != '"GET /projects/260 HTTP/1.1"':
            continue

        # Updating total size
        try:
            total_size += int(file_size)
        except ValueError:
            continue

        # Updating status codes
        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        # Every 10 lines, print the stats
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
