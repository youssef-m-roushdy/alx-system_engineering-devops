# Resources

Read or watch:

What is a (physical) server - text
What is a (physical) server - video
SSH essentials
SSH Config File
Public Key Authentication for SSH
How Secure Shell Works
SSH Crash Course (Long, but highly informative. Watch this if configuring SSH is still confusing. It may be helpful to watch at x1.25 speed or above.)

# For reference:

Understanding the SSH Encryption and Connection Process
Secure Shell Wiki
IETF RFC 4251 (Description of the SSH Protocol)
Internet Engineering Task Force
Request for Comments

# man or help:

ssh
ssh-keygen
env

# 0. Use a private key

Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/school with the user ubuntu.

Requirements:

Only use ssh single-character flags
You cannot use -l
You do not need to handle the case of a private key protected by a passphrase
sylvain@ubuntu$ ./0-use_a_private_key
ubuntu@server01:~$ exit
Connection to 8.8.8.8 closed.
sylvain@ubuntu$ 