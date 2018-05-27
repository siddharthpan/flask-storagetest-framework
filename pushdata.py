import paramiko
from scp import SCPClient
import os
from time import sleep

paramiko.util.log_to_file('/tmp/paramiko.log')

def pushtestfiles(target):
    ssh = paramiko.SSHClient()
    # ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect(remoteip, username="pi", password = "Rp11022000!")
    privatekeyfile = os.path.expanduser('~/.ssh/id_rsa')
    mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
    ssh.connect(hostname="192.168.1.225", username="pi", pkey=mykey)

    scp = SCPClient(ssh.get_transport())
    scp.put('diskspeed2.py')
    scp.close()

    # host="raspberrypi.local"
    # user="pi"
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    privatekeyfile = os.path.expanduser('~/.ssh/id_rsa')
    # client.load_system_host_keys()
    mykey = paramiko.RSAKey.from_private_key_file(privatekeyfile)
    client.connect(hostname="192.168.1.225", username="pi", pkey=mykey)
    # client.connect(host, username=user)
    stdin, stdout, stderr = client.exec_command('python diskspeed2.py')
    pwd =  stdout.read().splitlines()
    for elem in pwd:
            print (elem)
    scp.close()
    return None


def pushfiles(target):



    # Upload
    if target =='sdcard':
        host = "192.168.1.225"
        port = 22
        transport = paramiko.Transport((host, port))
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Auth

        password = "raspberry"
        username = "pi"
        transport.connect(username=username, password=password)

        # Go!

        sftp = paramiko.SFTPClient.from_transport(transport)

        filepath = '/home/pi/diskspeed2.py'
        localpath = '/home/siddharthpan/Project/FlaskNew/diskspeed2.py'
        sftp.put(localpath, filepath)
        client.connect(hostname="192.168.1.225", username="pi", password="raspberry")
        stdin, stdout, stderr = client.exec_command('python diskspeed2.py sdcard ')
        pwd = stdout.read().splitlines()
        for elem in pwd:
            print(elem)
        sftp.remove("/home/pi/diskspeed2.py")
        sftp.remove("/home/pi/csv1.csv")

        sftp.close()
        transport.close()

    elif target == 'pendrive':
        host = "192.168.1.225"
        port = 22
        transport = paramiko.Transport((host, port))
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Auth

        password = "raspberry"
        username = "pi"
        transport.connect(username=username, password=password)

        # Go!

        sftp = paramiko.SFTPClient.from_transport(transport)

        filepath = '/home/pi/usbdrv/diskspeed2.py'
        localpath = '/home/siddharthpan/Project/FlaskNew/diskspeed2.py'
        sftp.put(localpath, filepath)
        client.connect(hostname="192.168.1.225", username="pi", password="raspberry")
        stdin, stdout, stderr = client.exec_command('cd usbdrv && python diskspeed2.py pendrive')
        pwd = stdout.read().splitlines()
        for elem in pwd:
            print(elem)
        sftp.remove("/home/pi/usbdrv/diskspeed2.py")
        sftp.remove("/home/pi/usbdrv/csv1.csv")

        sftp.close()
        transport.close()

    elif target == 'android':
        host = "192.168.1.177"
        port = 22
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        password = "admin"
        username = "root"

        client.connect(host, port=port, username=username, password=password)

        # Go!

        sftp = client.open_sftp()

        filepath = '/data/data/com.termux/files/home/diskspeed2.py'
        localpath = '/home/siddharthpan/Project/FlaskNew/diskspeed2.py'
        sftp.put(localpath, filepath)

        client.connect(hostname="192.168.1.177", username="root", password="admin")
        client.invoke_shell()
        # stdin, stdout, stderr = client.exec_command('python diskspeed2.py sdcard')
        client.exec_command('am force-stop com.termux')
        sleep(1)
        client.exec_command('am start -n com.termux/com.termux.app.TermuxActivity')
        sleep(5)
        client.exec_command('input text "python diskspeed2.py android"')
        sleep(2)
        stdin, stdout, stderr = client.exec_command('input keyevent 66')
        sleep(18)
        client.exec_command('input text "exit"')
        sleep(1)
        client.exec_command('input keyevent 66')
        sleep(2)
        client.exec_command('input keyevent 66')

        pwd = stdout.read().splitlines()
        for elem in pwd:
            print(elem)
        sftp.remove("/data/data/com.termux/files/home/diskspeed2.py")
        sftp.remove("/data/data/com.termux/files/home/csv1.csv")

        sftp.close()
        client.close()

    # Close

