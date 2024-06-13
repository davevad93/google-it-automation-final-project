#!/usr/bin/env python3

# Import necessary modules
import psutil
import socket
import emails

# Set the threshold values for the system resources
MAX_CPU_USAGE = 80
MAX_DISK_THRESHOLD = 20
MAX_AVAILABLE_MEMORY = 500
LOCAL_HOST_IP = "127.0.0.1"

# Functions to check system resources
def check_cpu_usage():
    """Check if CPU usage exceeds max threshold."""
    return psutil.cpu_percent(interval=3) > MAX_CPU_USAGE

def check_disk_usage():
    """Check if disk usage exceeds max threshold."""
    return psutil.disk_usage("/").percent > (100 - MAX_DISK_THRESHOLD)

def check_memory_usage():
    """Check if available memory is below max threshold."""
    return psutil.virtual_memory().available < (MAX_AVAILABLE_MEMORY * (2 ** 20))

def check_network():
    """Check if localhost resolves to the correct IP address."""
    return socket.gethostbyname("localhost") != LOCAL_HOST_IP

def send_alert(alert):
    """Send an alert email and print the alert message."""
    data = {
        "sender": "automation@example.com",
        "receiver": "student@example.com",
        "subject": alert,
        "body": "Please check your system and resolve the issue as soon as possible.",
        "attachment": None,
    }
    try:
        message = emails.generate_email(**data)
        emails.send_email(message)
    except Exception as e:
        print(f"Unable to send alert email notification: {e}")
    finally:
        print(alert)
        exit(1)

# Main function to check system resources and send alerts if necessary
def main():
    """Check system resources and send alerts if necessary."""
    print("Checking system resources")
    alert = None
    if check_cpu_usage():
        alert = f"Error - CPU usage is over {MAX_CPU_USAGE}%"
    elif check_disk_usage():
        alert = f"Error - Available disk space is less than {MAX_DISK_THRESHOLD}%"
    elif check_memory_usage():
        alert = f"Error - Available memory is less than {MAX_AVAILABLE_MEMORY}MB"
    elif check_network():
        alert = f"Error - localhost cannot be resolved to {LOCAL_HOST_IP}"

    if alert:
        send_alert(alert)
    else:
        print("System is OK")

if __name__ == "__main__":
    main()
    