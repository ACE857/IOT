import cpuinfo
import os

def freq_settings(choice):
    if choice == "read":
        cpu_frequency = cpuinfo.get_cpu_info()['hz_actual']
        print("Current Frequency :: ", cpu_frequency)
    elif choice == "set":
        os.system("sudo cpufreq-set -f 600MHz")
        print("New Frequency is set at :: 600MHz")
    else:
        print("Invalid Choice.")


while(True):
    input_choice = input();
    freq_settings(str(input_choice))
