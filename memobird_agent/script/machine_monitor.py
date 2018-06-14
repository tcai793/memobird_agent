import subprocess
import json
import memobird_agent

APP_CONFIG_PATH = "/etc/memobird_agent/machine_monitor.json"
GENERAL_CONFIG_PATH = "/etc/memobird_agent/general.json"


def memo_print(machine):
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
    text = config["machine_name"] + ":" + machine + "is" + "reachable."
    doc.add_text(text)
    doc.print(config["smart_guid"], config["user_id"])


def ping(address):
    response = subprocess.run(["ping", "-c 1", address], stdout=subprocess.PIPE)
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

    # Scan through configured processes
    for machine in machine_list:
        if ping(machine) != 0:
            memo_print(machine)


if __name__ == "__main__":
    main()
