#!/usr/bin/env python
"""
Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.

Please do not use this script in production MOPs
"""

# Netmiko is used to connect to devices via ssh
from netmiko import Netmiko

# getpass is a library that prompt for the user to type the password, avoiding the hardcoding of credentials
from getpass import getpass

# Support libraries for common script functions such as error handling and parameters.
import sys
import os
import traceback

# Device and show commands parameters
deviceIp = ""
deviceType = ""
username = ""
showCommandsFile = "show_commands.txt"

try:
    print("Connecting to " + deviceIp + " (type " + deviceType + ") with username " + username)

    # Connect to device
    net_connect = Netmiko(
        deviceIp,
        username=username,
        password=getpass(),
        device_type=deviceType
    )

    print("Using show commands file " + showCommandsFile + ". Printing results in " + showCommandsFile + "_result.txt")

    # Read show commands file
    with open(showCommandsFile) as pre_checks_file:
        show_commands = [x.strip() for x in pre_checks_file.readlines()]

    # If results file is present, delete it.
    if os.path.isfile(showCommandsFile + "_result.txt"):
        os.remove(showCommandsFile + "_result.txt")

    # Create result file.
    mop_example_pre_checks_result_file = open(showCommandsFile + "_result.txt", "w")

    for command in show_commands:
        # Per each command in show_commands, print it, write in the result file and
        # execute it in the device. Finally, append the output in the result file.
        print(command)
        mop_example_pre_checks_result_file.write(command + "\n")
        output = net_connect.send_command(command)
        print(output)
        mop_example_pre_checks_result_file.write(output + "\n")

    # Close result file
    mop_example_pre_checks_result_file.close()

    print("Finished. Disconnecting session.")

    # Disconnect session
    net_connect.disconnect()

    sys.exit(0)

except Exception as e:
    # Any other errors, default here.
    print(traceback.print_exc())
    print("Something went wrong: " + str(e))
    sys.exit(2)
