#!/bin/bash

######################################################################
# README
#
# ------
#
# This script is used to start and stop OpenVPN in daemon mode.
# It is useful when you want to start OpenVPN in the background
# and stop it when you are done.
# AFTER CHANGING THE CONFIG_FILE VARIABLE, MAKE SURE TO MAKE THIS SCRIPT EXECUTABLE
# BY RUNNING `chmod +x vpn-control.sh` IN THE TERMINAL.
# ADDITIONALLY, YOU CAN MOVE THIS SCRIPT TO /usr/local/bin/ TO RUN IT FROM ANYWHERE.
# BY RUNNING `sudo mv vpn-control.sh /usr/local/bin/vpn-control`, YOU CAN RUN THIS SCRIPT
#
# TO START OPENVPN, RUN `vpn-control start`.
# TO STOP OPENVPN, RUN `vpn-control stop`.
#
# ------
######################################################################


# Path to your OpenVPN config file
CONFIG_FILE="PATH_TO_YOUR_OPENVPN_CONFIG_FILE" # change this to the path of your OpenVPN config file

# Function to start OpenVPN
start_vpn() {
    echo "Starting OpenVPN in daemon mode..."
    sudo openvpn --config "$CONFIG_FILE" --daemon
    echo "OpenVPN started."
}

# Function to stop OpenVPN
stop_vpn() {
    echo "Stopping OpenVPN..."
    # Find OpenVPN PID
    VPN_PID=$(ps aux | grep '[o]penvpn' | awk '{print $2}')

    if [ -z "$VPN_PID" ]; then
        echo "OpenVPN is not running."
    else
        sudo kill "$VPN_PID"
        echo "OpenVPN stopped."
    fi
}

# Check the argument passed to the script
case "$1" in
    start)
        start_vpn
        ;;
    stop)
        stop_vpn
        ;;
    *)
        echo "Usage: $0 {start|stop}"
        exit 1
        ;;
esac

