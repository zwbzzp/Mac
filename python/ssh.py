#!/usr/bin/env python
# -*- coding: uft-8 -*-

import os,sys
import paramiko
import threading
import platform

curr_ssh = None
curr_prompt = ">>"

#usage
def printUsage():
	print("		!ls						:list sessions.")
	print("		!session id				:connect session.")
	print("		!conn host user password:connect host with user.")
	print("		!exit					:exit.")

#connect
def conn(ip, username, passwd):
	try:
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(ip, 22, username, passwd, timeout=5)
		print("Connect to ", ip, "with ", username)
		global curr_prompt
		curr_prompt = username+"@"+ip+">>"
		return ssh
	except:
		return None

sessions = []
def loadSessions():
	global sessions
	try:
		f = open("sessions")
		sessions = f.readlines()
		f.close()
	except:
		pass


def exe_cmd_local(cmd):
	if(cmd == "!ls"):
		loadSessions()
		global sessions
		i = 0
		print("Sessions:")
		for s in sessions:
			print("[%d] %s" %(i,s))
			i+=1
	else:
		vals = cmd.split(' ')
		if(vals[0] == "!session"):
			id = (int)(vals[1])
			if(id<len(sessions)):
				os_name = platform.system()
				new_console_cmd = ""
				if(os_name == "Linux"):
					new_console_cmd="gnome-terminal -e\"./ssh.py" + sessions[id]+"\""
				elif(os_name == "Windows"):
					new_console_cmd = "start ssh.py " + sessions[id]
				os.system(new_console_cmd)
			else:
				print("Didn't have session ",vals[1])
		elif(vals[0] == "!conn"):
			global curr_ssh
			curr_ssh = conn(vals[1], vals[2], vals[3])
			f = open("sessions", "a")
			line = vals[1] + " " + vals[2] + " " + vals[3] + "\n"
			f.write(line)
			f.close()


def exe_cmd_ssh(ssh, cmd):
	if(ssh == None):
		print("Didn't connect to a server.Use '!conn' to connect please")
		return
	stdin, stdout, stderr = ssh.exec_command(cmd)
	print(stdout.read())
	print(stderr.read())

if __name__ == "__main__":
	loadSessions()
	if(len(sys.argv)==4):
		curr_ssh = conn(sys.argv[1], sys.argv[2], sys.argv[3])
	else:
		printUsage()
	while True:
		cmd = raw_input(curr_prompt)
		if(len(cmd) == 0):
			continue

		if(cmd == "!exit"):
			if(curr_ssh != None):
				curr_ssh.close()
			break
		else:
			if(cmd[0] == '!'):
				exe_cmd_local(cmd)
			else:
				exe_cmd_ssh(curr_ssh,cmd)
		











