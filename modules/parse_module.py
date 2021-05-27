import argparse
from modules.ping_module import *
import os


def parse():
    print("    @@@@   @@  @@    @@   @@@@        @@@    @@  @@  @@@@@   @@@    @@   @@  @@@@@  @@@@@\n"
          + "   @@ @@  @@  @@@@  @@  @@          @@  @   @@  @@  @@     @@  @   @@  @@   @@     @@  @@\n"
          + "  @@@@   @@  @@ @@ @@  @@  @@@     @@      @@@@@@  @@@@@  @@      @@@@@    @@@@@  @@@@@\n"
          + " @@     @@  @@   @@@   @@   @      @@  @  @@  @@  @@      @@  @  @@ @@    @@     @@  @@\n"
          + "@@     @@  @@   @@@    @@@@@        @@@  @@  @@  @@@@@     @@@  @@   @@  @@@@@  @@    @@\n"
          + "                                                                 Network monitoring tool\n"
          + "                                                                 Made by Baka\n")
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_file",
                        help="Required parameter for setting input file. Format: '-i PATH_TO_FILE'. "
                             "Example:'-i input.txt'", required=True)
    parser.add_argument("-o", "--output_file",
                        help="Parameter for setting output file. If parameter is not given,"
                             " default output.txt file will be used."
                             " Format: '-o PATH_TO_FILE'. Example:'-o output.txt'")
    parser.add_argument("-t", "--timer",
                        help="Parameter for setting interval of pinging devices in seconds. "
                             "If parameter is not given, default interval 5 s will be used."
                             " Format: '-t INTERVAL'. Example:'-o 10'", type=int)
    parser.add_argument("-m", "--machine_output",
                        help="Parameter for setting format of output file. If parameter is not given,"
                             "user friendly format will be used instead. Format: '-m'", action="store_true")
    args = parser.parse_args()
    args = control(args)
    return args


def check_int(integer):
    try:
        number = int(integer)
    except ValueError or TypeError:
        print("Given parameter is not integer!")
        return False
    return number


def control(args):
    input_file = args.input_file
    if not os.path.isfile(input_file):
        return False
    else:
        list_of_ips = get_ips(input_file)
        if list_of_ips is False:
            return False
        else:
            list_of_hosts = create_list_of_hosts(list_of_ips)
    output_file = args.output_file

    timer = args.timer
    if timer is None:
        timer = 5
    machine_output = args.machine_output

    if output_file is None:
        if machine_output:
            output_file = "output.json"
        else:
            output_file = "output.txt"
    elif machine_output and output_file[len(output_file) - 5:len(output_file)] != ".json":
        print("Wrong format of output file!\nIf machine output is used, json file must be given!")
        return False
    return [list_of_hosts, output_file, timer, machine_output]


# function for getting IP addresses from file
def get_ips(path):
    set_of_ips = set()
    with open(path, 'r') as file:
        line = file.readline()
        if not check_ip(line):
            return False

        line = line.strip("\n")
        set_of_ips.add(line)
        while True:
            line = file.readline()
            if line == "":
                break
            line = remove_n(line)
            if not check_ip(line):
                return False
            set_of_ips.add(line)
    return set_of_ips


# help function for removing '\n'
def remove_n(ip):
    a = ip[len(ip) - 1:len(ip)]
    if ip[len(ip) - 1:len(ip)] == "\n":
        ip = ip[:len(ip) - 1]
    return ip


# function for checking format of IP address
def check_ip(ip_address):
    ip_parts = ip_address.split(".")

    if len(ip_parts) != 4:
        return False
    for part in ip_parts:
        part = check_int(part)

        if part is False or part > 255:
            return False
    return True


def create_list_of_hosts(set_of_ips):
    list_of_hosts = []
    for ip in set_of_ips:
        list_of_hosts.append(Host(ip))
    return list_of_hosts
