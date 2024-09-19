# Some_scripts

## - vpn-control

This bash script allows you to easily start and stop OpenVPN in daemon mode. You can run the script from any directory on your system once it's installed.

### Prerequisites

- OpenVPN must be installed on your system. You can install it using:
  ```bash
  sudo apt install openvpn
  ```
- Move the script to a directory in your PATH (e.g., /usr/local/bin/).

  ```bash
  sudo mv vpn-control.sh /usr/local/bin/vpn-control
  ```
- Ensure the script has executable permissions.

  ```bash
  sudo chmod +x /usr/local/bin/vpn-control
  ```
- Update the script to point to your OpenVPN configuration file by editing the CONFIG_FILE variable at the top of the script.

  ```bash
  sudo vim /usr/local/bin/vpn-control
  ```
  ```vim
  #LINE 24
  CONFIG_FILE="PATH_TO_YOUR_OPENVPN_CONFIG_FILE" # change this to the path of your OpenVPN config file
  ```
- Replace PATH_TO_YOUR_OPENVPN_CONFIG_FILE with the full path to your OpenVPN .ovpn configuration file.

### Usage
You can now use the vpn-control command from any directory to start or stop OpenVPN.

- To start OpenVPN in daemon mode:

  ```bash
  vpn-control start
  ```
- To stop OpenVPN by killing its process:

  ```bash
  vpn-control stop
  ```
