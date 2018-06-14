import subprocess
import json
from .document import ReportDocument

APP_CONFIG_PATH = "/etc/memobird_agent/transmission_monitor.json"
TORRENT_STATE_PATH = "/etc/memobird_agent/data/transmission_monitor.json"


def main():
    # Parse config
    config = {}
    try:
        config_f = open(APP_CONFIG_PATH)
        config = json.load(config_f)
        config_f.close()
        if "username" not in config or "password" not in config:
            print("Missing item in config file, exiting")
            exit(-1)
    except:
        print("Error occured while parsing config file, exiting")
        exit(-1)

    # get_ids
    id_list = []
    command = subprocess.run(["transmission-remote", "-n", config["username"] + ":" + config["password"], "-l"],
                             stdout=subprocess.PIPE)
    results = command.stdout.decode().splitlines()
    for value in results:
        value = value.split()
        if value[0].isdecimal():
            id_list.append(int(value[0]))

    # torrent_info
    torrent_info = []
    new_completed_torrent = []
    for ids in id_list:
        command = subprocess.run(
            ["transmission-remote", "-n", config["username"] + ":" + config["password"], "-t", str(ids), "-i"],
            stdout=subprocess.PIPE)
        result = command.stdout.decode().splitlines()
        name = ""
        percent_done = ""
        hash_of_torrent = ""
        for value in result:
            if value.startswith("  Name"):
                name = value[7:]
            if value.startswith("  Percent"):
                percent_done = value.split()[2]
            if value.startswith("  Hash"):
                hash_of_torrent = value.split()[1]
        if percent_done == "100%":
            torrent_info.append((name, hash_of_torrent, percent_done))

        # new_torrent
        f = open(TORRENT_STATE_PATH, "r+")
        content = f.readlines()
        for torrent in torrent_info:
            flag = False
            for c in content:
                if c.find(torrent[1]) != -1:
                    flag = True
            if flag is False:
                f.write(torrent[1] + "\n")
                new_completed_torrent.append(torrent)
        f.close()

    # Print
    if len(new_completed_torrent) is not 0:
        doc = ReportDocument()
        doc.add_text("New Torrent(s) Finished:")
        for t in new_completed_torrent:
            doc.add_text(t[0])
        doc.print()
