# Ping Check
 Ping Check is tool for monitoring network devices by ping. Ping Check works on Windows and also on Linux.

 The tool takes an input file with the IP addresses of hosts to monitor.
 ``` 
 # Example of Input file
 192.168.88.1
 8.8.8.8
 8.8.4.4
 8.8.7.7
 ```

During and after monitoring the results of monitoring are stored in an output file. The output file can be set to be User Friendly.
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
The second option for the output file is for it to be in machine-friendly in json format.
```
{"8.8.4.4": {"last_response": "Fri May 28 09:27:00 2021", "total_ping": 3, "success": 3, "fail": 0, "fail_rate": 0.0}, "192.168.2.2": {"last_response": "No response", "total_ping": 3, "success": 0, "fail": 3, "fail_rate": 100.0}, "8.8.8.8": {"last_response": "Fri May 28 09:27:04 2021", "total_ping": 3, "success": 3, "fail": 0, "fail_rate": 0.0}, "192.168.88.1": {"last_response": "No response", "total_ping": 3, "success": 0, "fail": 3, "fail_rate": 100.0}}
```
## Usage
Format of the command to use the tool, where ARGUMENTS are settings of the tool:
```
python3 main.py ARGUMENTS
```
### Arguments
#### Input file
This is a required argument in order to give the tool an input file of IP addresses
```
Format: -i PATH_TO_FILE
Example: -i try.txt
```
#### Output file
Optional argument for giving the tool an output file. If no file is given the output file will be set to output.txt or output.json (.json if the `-m` option is set).
```
Format: -o OUTPUT_FILE
Example: -o my_output_file.txt
```
#### Machine-readable format
The next optional argument is used to set the format of the output file. If the argument is used, the output file will be written in json. If the argument is not used, a user friendly output written.
```
Format: -m
Example: -m
```
#### Interval of control
The last optional argument, which indicates after how many seconds the guests are checked again. If the interval is not given, the interval is set to a default of 5 seconds.
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