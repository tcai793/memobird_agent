import subprocess
import json
import memobird_agent
from .document import ReportDocument

APP_CONFIG_PATH = "/etc/memobird_agent/machine_monitor.json"


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

    doc = ReportDocument()

    # Scan through configured processes
    for machine in machine_list:
        if ping(machine) != 0:
            doc.add_text(machine + ' is unreachable')
    doc.print()


if __name__ == "__main__":
    main()
