import psutil
import time

def monitor_system(thresholds):
    """
    Continuously monitors the system's CPU, memory, and disk usage,
    and prints warnings if usage exceeds specified thresholds.
    """
    while True:
        # Get CPU, memory, and disk usage statistics
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        # Check if any usage exceeds the defined thresholds and print warnings
        if cpu > thresholds['cpu']:
            print(f'Warning: CPU usage at {cpu}%')
        if memory > thresholds['memory']:
            print(f'Warning: Memory usage at {memory}%')
        if disk > thresholds['disk']:
            print(f'Warning: Disk usage at {disk}%')
        
        # Wait for 10 seconds before checking again
        time.sleep(10)

# Define the usage thresholds for CPU, memory, and disk
system_data = {'cpu': 20, 'memory': 15, 'disk': 15}

# Start monitoring the system with the defined thresholds
monitor_system(system_data)
