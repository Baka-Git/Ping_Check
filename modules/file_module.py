from modules.ping_module import *
import time


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


def show(list_of_hosts):
    ip_size = 17  # 15 + 2
    time_size = 26  # 24 + 2
    info_size = get_max_size(list_of_hosts, 7) + 2
    rate_size = 11  # 9 + 2
    print(" " + (ip_size + time_size + info_size * 4 + rate_size - 3) * "_" + "\n"
          + "|" + same_size(" ", ip_size) + same_size(" ", time_size) + same_size("ICMP",
                                                                                  3 * (info_size + 1) + rate_size)
          + "\n"
          + "|" + same_size("IP Address", ip_size) + same_size("Last Response", time_size)
          + same_size("Total", info_size) + same_size("Success", info_size) + same_size("Fail", info_size)
          + same_size("Fail Rate", rate_size) + "\n"
          + "|" + same_size_special(ip_size) + same_size_special(time_size)
          + same_size_special(info_size) + same_size_special(info_size) + same_size_special(info_size)
          + same_size_special(rate_size)

          )
    for i in range(0, len(list_of_hosts)):
        if list_of_hosts[i].last_response == 0:
            time_response = "No response"
        else:
            time_response=time.ctime(list_of_hosts[i].last_response)
        print("|" + same_size(list_of_hosts[i].address, ip_size)
              + same_size(time_response, time_size)
              + same_size(list_of_hosts[i].total_ping, info_size)
              + same_size(list_of_hosts[i].success_ping, info_size)
              + same_size((list_of_hosts[i].total_ping - list_of_hosts[i].success_ping), info_size)
              + same_size(
            str((list_of_hosts[i].total_ping - list_of_hosts[i].success_ping)*100 / list_of_hosts[i].total_ping)[:4] + " %",
            rate_size)
              )
    print("|" + same_size_special(ip_size) + same_size_special(time_size)
          + same_size_special(info_size) + same_size_special(info_size) + same_size_special(info_size)
          + same_size_special(rate_size)

          )


# function for getting max length of string variation of total ping from all hosts
def get_max_size(list_of_hosts, minimum):
    for host in list_of_hosts:
        temp_size = len(str(host.total_ping))
        if temp_size > minimum:
            minimum = temp_size
    return minimum


# help function for presentation
def same_size(info, size):
    string_info = " " + str(info)
    while len(string_info) < size:
        string_info += " "
    string_info += "|"
    return string_info


def same_size_special(size):
    string_info = "_"
    while len(string_info) < size:
        string_info += "_"
    string_info += "|"
    return string_info


#host = Host("8.8.8.8")
#host.total_ping = 1000
#host.success_ping = 999
#host.last_response = time.time()
#list_of_ip = [host]
#host_2 = Host("192.1.120.253")
#host_2.total_ping = 100
#host_2.success_ping = 9
#host.last_response = time.time()
#list_of_ip.append(host_2)
#list_of_ip[0].ping()
#show(list_of_ip)
# print(len(" ICMP                 |"))
# print(len(" 10000 | 9999  | 0.00   |"))
# print(len("Fail Rate"))


