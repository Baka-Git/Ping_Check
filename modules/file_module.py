import time


def show(list_of_hosts, output_file, is_machine):
    ip_size = 17  # 15 + 2, 15 - length of IP Address (with dots) + 2 whitespaces
    time_size = 26  # 24 + 2,  24 - length of timestamp + 2 whitespaces
    info_size = get_max_size(list_of_hosts, 7) + 2  # max length of string version of total amount of ping +2 whitespace
    rate_size = 11  # 9 + 2, length of header "Fail Rate" + 2 whitespaces
    if not is_machine:
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
    for i in range(0, len(list_of_hosts)):
        if list_of_hosts[i].last_response == 0:
            time_response = "No response"
        else:
            time_response = time.ctime(list_of_hosts[i].last_response)
        if not is_machine:
            info += "|" + same_size(list_of_hosts[i].address, ip_size) + \
                same_size(time_response, time_size) + \
                same_size(list_of_hosts[i].total_ping, info_size) + \
                same_size(list_of_hosts[i].total_ping - list_of_hosts[i].fail_ping, info_size) + \
                same_size(list_of_hosts[i].fail_ping, info_size) + \
                same_size(str(list_of_hosts[i].fail_ping
                              * 100 / list_of_hosts[i].total_ping)[:4] + " %", rate_size) + "\n"

        # f.write("\n"+info)
    if not is_machine:
        f = open(output_file, "w")
        f.write(header + info + spoiler)
        f.close()


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



