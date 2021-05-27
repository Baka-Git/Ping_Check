import time
import json


def show(list_of_hosts, output_file, is_machine):
    list_of_info = []
    for i in range(0, len(list_of_hosts)):
        if list_of_hosts[i].last_response == 0:
            time_response = "No response"
        else:
            time_response = time.ctime(list_of_hosts[i].last_response)
        list_of_info.append([list_of_hosts[i].address, time_response, list_of_hosts[i].total_ping,
                             list_of_hosts[i].total_ping - list_of_hosts[i].fail_ping, list_of_hosts[i].fail_ping,
                             list_of_hosts[i].fail_ping * 100 / list_of_hosts[i].total_ping])
    if is_machine:
        machine_output(list_of_info, output_file)
    else:
        friendly_output(get_max_size(list_of_hosts, 7) + 2, list_of_info, output_file)


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


def friendly_output(max_size, info_list, output_file):
    ip_size = 17  # 15 + 2, 15 - length of IP Address (with dots) + 2 whitespaces
    time_size = 26  # 24 + 2,  24 - length of timestamp + 2 whitespaces
    info_size = max_size  # max length of string version of total amount of ping +2 whitespace
    rate_size = 11  # 9 + 2, length of header "Fail Rate" + 2 whitespaces

    header = " " + (ip_size + time_size + info_size * 4 + rate_size - 3) * "_" + "\n" + "|" + \
             same_size(" ", ip_size) + same_size(" ", time_size) + \
             same_size("ICMP", 3 * (info_size + 1) + rate_size) + "\n" + "|" + same_size("IP Address", ip_size) + \
             same_size("Last Response", time_size) + same_size("Total", info_size) + \
             same_size("Success", info_size) + same_size("Fail", info_size) + same_size("Fail Rate", rate_size) + \
             "\n" + "|" + same_size_special(ip_size) + same_size_special(time_size) + \
             same_size_special(info_size) + same_size_special(info_size) + same_size_special(info_size) + \
             same_size_special(rate_size) + "\n"
    spoiler = "|" + same_size_special(ip_size) + same_size_special(time_size) + same_size_special(info_size) + \
              same_size_special(info_size) + same_size_special(info_size) + same_size_special(rate_size) + "\n"
    info = ""
    # info 0 - address, 1 - timestamp, 2 - total, 3 - success, 4 - fail, 5 - fail_rate
    for information in info_list:
        info += "|" + same_size(information[0], ip_size) + same_size(information[1], time_size) + \
                same_size(information[2], info_size) + same_size(information[3], info_size) + \
                same_size(information[4], info_size) + same_size(str(information[5])[:4] + " %", rate_size) + "\n"
    with open(output_file, "w") as file:
        file.write(header + info + spoiler)


def machine_output(info_list, output_file):
    dictionary_of_hosts = {}
    for info in info_list:
        info_help = {
            "last_response": info[1],
            "total_ping": info[2],
            "success": info[3],
            "fail": info[4],
            "fail_rate": info[5]
        }
        dictionary_of_hosts[info[0]] = info_help

    with open(output_file, "w") as file:
        json.dump(dictionary_of_hosts, file)
