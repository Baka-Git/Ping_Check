# Ping Check
 Ping Check is tool for monitoring network devices by ping. Ping Check works on Windows and also on Linux.

 Tool takes input file with IP addresses of hosts to monitor.
 ``` 
 # Example of Input file
 192.168.88.1
 8.8.8.8
 8.8.4.4
 8.8.7.7
 ```

During and after monitoring are results of monitoring stored in Output file. Output file can be User Friendly.
```
 _______________________________________________________________________________________
|                 |                          | ICMP                                    |
| IP Address      | Last Response            | Total   | Success | Fail    | Fail Rate |
|_________________|__________________________|_________|_________|_________|___________|
| 8.8.7.7         | No response              | 2       | 0       | 2       | 100. %    |
| 8.8.4.4         | Sat May 29 11:58:36 2021 | 2       | 2       | 0       | 0.0 %     |
| 192.168.2.2     | No response              | 2       | 0       | 2       | 100. %    |
| 192.168.88.1    | No response              | 2       | 0       | 2       | 100. %    |
| 8.8.8.8         | Sat May 29 11:58:36 2021 | 2       | 2       | 0       | 0.0 %     |
|_________________|__________________________|_________|_________|_________|___________|
```
Second option is output file for machine in json format.
```
{"8.8.4.4": {"last_response": "Fri May 28 09:27:00 2021", "total_ping": 3, "success": 3, "fail": 0, "fail_rate": 0.0}, "192.168.2.2": {"last_response": "No response", "total_ping": 3, "success": 0, "fail": 3, "fail_rate": 100.0}, "8.8.8.8": {"last_response": "Fri May 28 09:27:04 2021", "total_ping": 3, "success": 3, "fail": 0, "fail_rate": 0.0}, "192.168.88.1": {"last_response": "No response", "total_ping": 3, "success": 0, "fail": 3, "fail_rate": 100.0}}
```
## Usage
Format of command to use tool, where ARGUMENTS are setting of tool:
```
python3 main.py ARGUMENTS
```
### Arguments
#### Input file
Required argument for giving tool input file with IP addresses
```
Format: -i PATH_TO_FILE
Example: -i try.txt
```
#### Output file
Optional argument for giving tool output file. If no file is given output file output.txt or output.json. That depedns on next argument.
```
Format: -o OUTPUT_FILE
Example: -o my_output_file.txt
```
#### Machine format
Next optional argument is format. If argument is used, output file must be json type of file and output will be in json format. If argument is not used, user friendly output is used.
```
Format: -m
Example: -m
```
#### Interval of control
Last optional argument is the interval, which indicates after how many seconds the guests are checked again. If interval is not given, default 5 second interval is used
```
Format: -t INTERVAL_IN_SECONDS
Example: -t 60
```
## Example
```
Command: python3 main.py -i try.txt -o output.json -t 5 -m
Output file:
{"8.8.4.4": {"last_response": "Fri May 28 09:27:00 2021", "total_ping": 3, "success": 3, "fail": 0, "fail_rate": 0.0}, "192.168.2.2": {"last_response": "No response", "total_ping": 3, "success": 0, "fail": 3, "fail_rate": 100.0}, "8.8.8.8": {"last_response": "Fri May 28 09:27:04 2021", "total_ping": 3, "success": 3, "fail": 0, "fail_rate": 0.0}, "192.168.88.1": {"last_response": "No response", "total_ping": 3, "success": 0, "fail": 3, "fail_rate": 100.0}}
```