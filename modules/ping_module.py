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
            process = subprocess.Popen(["ping", "-n", "1", self.address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            communication = process.communicate()[0]
            value = 0
            if 'unreachable' in str(communication) or 'timed' in str(communication):
                value=1
        else:
            value = subprocess.call(["ping", "-c", "1", self.address])
        self.total_ping += 1
        if value != 0:
            self.fail_ping += 1
            return False
        self.last_response = time.time()
        return True

#def ping(host):
  #  process = subprocess.Popen(["ping", "-n", "1",host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
   # streamdata = process.communicate()[0]
    #if 'unreachable' in str(streamdata):
    #    return 1
   # return process.returncode