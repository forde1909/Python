
"""
File utilities, forked from the Comm module of SD-Node, written c. 2017 
Tested with Python >=3.6 

Joseph Forde
Exercise_11
Student number: L00169708
 
By: JOR 
v0.1 26AUG21 
""" 
import ftplib 
# Set the path 
path = '/mirrors/ubuntu-cdimage/releases/22.04/release' 
# What file to download 
filename = 'SHA256SUMS' 
# Make the connection 
ftp = ftplib.FTP("ftp.heanet.ie") 
# Anonymous login 
ftp.login() 
# Change to the correct directory 
ftp.cwd(path) 
# Retrieve the file 
ftp.retrbinary("RETR " + filename, open(filename, 'wb').write) 
# Cleanly exit 
ftp.quit() 

