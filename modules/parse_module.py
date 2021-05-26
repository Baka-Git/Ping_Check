import argparse
from modules.ping_module import *


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
                             "Example:'-i input.txt'")
    parser.add_argument("-o", "--output_file",
                        help="Parameter for setting output file. If parameter is not given,"
                             " default output.txt file will be used."
                             " Format: '-o PATH_TO_FILE'. Example:'-o output.txt'")
    parser.add_argument("-t", "--timer",
                        help="Parameter for setting interval of pinging devices in seconds. "
                             "If parameter is not given, default interval 5 s will be used."
                             " Format: '-t INTERVAL'. Example:'-o 10'")
    parser.add_argument("-m", "--machine_output",
                        help="Parameter for setting format of output file. If parameter is not given,"
                             "user friendly format will be used instead. Format: '-m'", action="store_true")
    args = parser.parse_args()
    # print(args)
    args = control(args)
    return args


def check_file(path):
    try:
        f = open(path, "r")
        f.readline()
    except FileNotFoundError:
        print("Given file " + path + " does not exists!")
        return False
    return True


def check_int(integer):
    try:
        print(integer)
        a = int(integer)
    except ValueError or TypeError:
        print("Given parameter is not integer!")
        return False
    return a


def control(args):
    input_file = args.input_file
    if input_file is None or not check_file(input_file):
        return False
    else:
        list_of_ips = get_ips(input_file)
        if list_of_ips is False:
            return False
        else:
            list_of_hosts = create_list_of_hosts(list_of_ips)
    output_file = args.output_file
    if output_file is None:
        output_file = "output.txt"
    timer = args.timer
    if timer is not None:
        timer = check_int(timer)
        if timer is False:
            return False
    else:
        timer = 5
    machine_output = args.machine_output
    return [list_of_hosts, output_file, timer, machine_output]


# function for getting IP addresses from file
def get_ips(path):
    list_of_ips = []
    try:
        with open(path, 'r') as file:
            file.readline()
    except FileNotFoundError:
        print("File not found")
        return False
    with open(path, 'r') as file:
        line = file.readline()
        if not check_ip(line):
            return False
        line = remove_n(line)
        list_of_ips.append(line)
        while True:
            line = file.readline()
            if line == "":
                break
            line = remove_n(line)
            if not check_ip(line):
                return False
            list_of_ips.append(line)
    print(list_of_ips)
    return list_of_ips


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
        try:
            part = int(part)
        except ValueError:
            return False
        if part > 255:
            return False
    return True


def create_list_of_hosts(list_of_ips):
    list_of_hosts = []
    for ip in list_of_ips:
        list_of_hosts.append(Host(ip))
    return list_of_hosts
