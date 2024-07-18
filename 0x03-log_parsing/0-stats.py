#!/usr/bin/python3
import sys
import signal

# Global variables to store the total file size and the count of status codes
total_size = 0
status_codes_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

# Function to print the statistics
def print_stats():
    global total_size, status_codes_count
    print(f"File size: {total_size}")
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")

# Function to handle the keyboard interrupt signal
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Main loop to read input and process lines
line_count = 0
try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 7:
            continue

        ip, dash, date, request, http_version, status_code_str, file_size_str = parts
        if not (request.startswith('"GET') and request.endswith('HTTP/1.1"')):
            continue

        try:
            status_code = int(status_code_str)
            file_size = int(file_size_str)
        except ValueError:
            continue

        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
            total_size += file_size

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

print_stats()
