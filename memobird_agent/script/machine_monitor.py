import subprocess
import json
from .document import ReportDocument

APP_CONFIG_PATH = "/etc/memobird_agent/machine_monitor.json"
STATE_FILE_PATH = "/etc/memobird_agent/data/machine_monitor.json"


class UnknownStateError(Exception):
    def __init__(self, state):
        self.state = state


def _state_machine(old_state, reachability):
    valid_state = ['reachable', 'unreachable', 'printed']
    transition_table = {
        'reachable': {True: 'reachable', False: 'unreachable'},
        'unreachable': {True: 'reachable', False: 'printed'},
        'printed': {True: 'reachable', False: 'printed'}
    }
    output_table = {
        'reachable': {True: '', False: ''},
        'unreachable': {True: '', False: 'unreachable'},
        'printed': {True: 'reachable', False: ''}
    }
    if old_state not in valid_state:
        raise UnknownStateError
    new_state = transition_table[old_state][reachability]
    print_message = output_table[old_state][reachability]
    return new_state, print_message


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
        if machine not in state:
            state[machine] = 'reachable'
        reachability = True if ping(machine) is 0 else False
        state[machine], print_message = _state_machine(state[machine], reachability)
        if print_message:
            doc.add_text(machine + ' is ' + print_message)
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
