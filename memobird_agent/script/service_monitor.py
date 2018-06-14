import subprocess
import json
from .document import ReportDocument

APP_CONFIG_PATH = "/etc/memobird_agent/service_monitor.json"
STATE_FILE_PATH = "/etc/memobird_agent/data/service_monitor.json"


def main():
    # Open and Parse config
    process_list = []
    try:
        config_f = open(APP_CONFIG_PATH)
        config = json.load(config_f)
        config_f.close()
        process_list = config["processes"]
    except:
        print("Error occurred when parsing config file, exiting")
        exit(-1)

    # Open and Parse data
    state = {}
    try:
        state_f = open(STATE_FILE_PATH, "r")
        state = json.load(state_f)
        state_f.close()
    except:
        print("Cannot read state file")

    doc = ReportDocument()
    # Scan through configured processes
    running_processes = subprocess.run(["ps", "-e", "-o", "command"], stdout=subprocess.PIPE).stdout.decode()
    for process in process_list:
        if process in running_processes:
            new_status = "UP"
        else:
            new_status = "DOWN"
        # For each process, if exists in data, then Compare with stored data.
        # If same then continue, else change current state and print
        if process in state:
            if state[process] == new_status:
                continue
            else:
                state[process] = new_status
                doc.add_text(process + ' is ' + new_status)
        # if DNE in data, then add current state and print
        else:
            state[process] = new_status
            doc.add_text(process + ' is ' + new_status)
    doc.print()

    # Write data back to data location
    try:
        state_f = open(STATE_FILE_PATH, "w")
        json.dump(state, state_f)
    except:
        print("Error occurred when writing process data back to file")
        exit(-1)


if __name__ == "__main__":
    main()
