import subprocess


def current_process_utilization():
    subprocess.call("ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%mem | head", shell=True)
    return 0


def current_cpu_utilization():
    subprocess.call("ps -A -o pcpu | tail -n+2 | paste -sd+ | bc", shell=True)
    return 0


def current_ram_utilization():
    subprocess.call("cat /proc/meminfo | grep -E 'MemTotal|MemFree'", shell=True)
    return 0



