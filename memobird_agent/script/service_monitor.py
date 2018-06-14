import subprocess
import json
import memobird_agent

APP_CONFIG_PATH = "/etc/memobird_agent/service_monitor.json"
STATE_FILE_PATH = "/etc/memobird_agent/data/service_monitor.json"
GENERAL_CONFIG_PATH = "/etc/memobird_agent/general.json"


def memo_print(process, state):
    config = {}
    try:
        config_f = open(GENERAL_CONFIG_PATH)
        config = json.load(config_f)
        config_f.close()
    except:
        print("Error occurred when parsing general config file, exiting")
        exit(-1)
    if "smart_guid" not in config or "user_id" not in config or "machine_name" not in config:
        print("Machine config file missing item, exiting")
        exit(-1)
    doc = memobird_agent.Document()
    text = config["machine_name"] + ":" + process + "is" + state
    doc.add_text(text)
    doc.print(config["smart_guid"], config["user_id"])


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

    # Scan through configured processes
    running_processes = subprocess.run(["ps", "aux"], stdout=subprocess.PIPE).stdout.decode()
    for process in process_list:
        if running_processes.find(process):
            new_status = "UP"
        else:
            new_status = "DOWN"
        # For each process, if exists in data, then Compare with stored data.
        # If same then continue, else change current state and print
        if process in state:
            if state[process] == new_status:
                continue
            else:
                memo_print(process, new_status)
        # if DNE in data, then add current state and print
        else:
            state[process] = new_status
            memo_print(process, new_status)

    # Write data back to data location
    try:
        state_f = open(STATE_FILE_PATH, "w")
        json.dump(state, state_f)
    except:
        print("Error occurred when writing process data back to file")
        exit(-1)


if __name__ == "__main__":
    main()
