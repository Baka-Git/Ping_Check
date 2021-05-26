import platform
import subprocess
import time


class Host:
    def __init__(self, address):
        self.address = address
        self.last_response = 0
        self.total_ping = 0
        self.fail_ping = 0

    def ping(self):
        argument = "-c"
        if platform.system().lower() == "windows":
            argument = "-n"

        value = subprocess.call(["ping", argument, "1", self.address])
        self.total_ping += 1
        if value != 0:
            self.fail_ping += 1
            return False
        self.last_response = time.time()
        return True
