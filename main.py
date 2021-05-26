from modules.ping_module import *
from modules.parse_module import *
from modules.file_module import *
import time


def main():
    args = parse()
    if args is False:
        return False
    list_of_hosts = args[0]
    output_file = args[1]
    interval_to_sleep = args[2]
    is_machine = args[3]
    args = None
    while True:
        for i in range(0, len(list_of_hosts)):
            list_of_hosts[i].ping()
        actual_files(list_of_hosts)
        show(list_of_hosts, output_file, is_machine)
        time.sleep(interval_to_sleep)


main()
