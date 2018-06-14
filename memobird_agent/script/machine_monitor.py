import subprocess
import json
from .document import ReportDocument

APP_CONFIG_PATH = "/etc/memobird_agent/machine_monitor.json"
STATE_FILE_PATH = "/etc/memobird_agent/data/machine_monitor.json"


def ping(address):
    response = subprocess.run(["ping", "-c", "1", "-W", "2", address], stdout=subprocess.PIPE)
    return response.returncode


def main():
    # Open and Parse config
    machine_list = []
    try:
        config_f = open(APP_CONFIG_PATH)
        config = json.load(config_f)
        config_f.close()
        machine_list = config["machines"]
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
    for machine in machine_list:
        if ping(machine) is 0:
            curr_status = "reachable"
        else:
            curr_status = "unreachable"
        if machine in state:
            if state[machine] == curr_status:
                continue
            else:
                state[machine] = curr_status
                doc.add_text(machine + ' is ' + curr_status)
        else:
            state[machine] = curr_status
            doc.add_text(machine + ' is ' + curr_status)
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
