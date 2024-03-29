
#importing packages

from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_excpetion import NetMikoTimeoutException
from paramiko.ssh_exception import  SSHException
from netmiko.ssh_exception import AuthenticationException

#defining username & password for SSH conenction
username = raw_input('Enter your username:')
password = getpass()


#opening the commands_file and reading commands
with open('commands_file') as f:
    commands_list = f.read().splitlines()

#opening devices_file and reading device devices_list
with open('devices_file') as f:
    devices_list = f.read().splitlines()

#looping on each device and attempting to connect, printing the device attempting to connect to
for devices in devices_list:
    print 'Connecting to device' + devices
    ip_address_of_devices = devices


#defining the device type, ip, username & password to connect to useing ConnectHandler
iosv_l2_s1 = {

        'device_type' : 'cisco_ios',
        'ip': ' (enter the device ip address)'
        'username' : username
        'password' : password

}

# Handling connection exceptions
try :
    net_connect = ConnectHandler(**ios_device)
except (AuthenticationException):
    print 'Authentication failure' + ip_address_of_devices
    continue
except (NetMikoTimeoutException):
    print 'Timeout to device' + ip_address_of_devices
    continue
except (EOFError):
    print 'End of file' + ip_address_of_devices
    continue
except (SSHException):
    print 'SSH error. Please make sure SSH is enabled on your device' + ip_address_of_devices
    continue
except  Exception as unknown_error:
    print 'Unknown error' + unknown_error
    continue


#connecting to device using ConnectHandler and sending configurations to config device from commands_list file

net_connect = ConnectHandler(**iosv_l2_s1)
output = net_connect.send_config_set(commands_list)
print(output)
