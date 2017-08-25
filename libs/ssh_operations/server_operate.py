import paramiko
from scp import SCPClient
import os, sys
import shutil

sys.path.append(os.path.join(os.path.dirname(__file__), '../../', ''))
import configuration as config

def run():
	k = paramiko.RSAKey.from_private_key_file('/home/alexliu/.ssh/id_rsa')
	paramiko.util.log_to_file("filename.log")
	client = paramiko.SSHClient()
	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	client.connect('10.253.12.244', port=32200, username='alexliu', pkey=k)


	stdin, stdout, stderr = client.exec_command('ls')


	scp = SCPClient(client.get_transport())
	scp.put(config.configuration['name_server'], '~/Z3Top10RankingServer/mkt_name.txt')
	scp.put(config.configuration['ranking_40k'], '~/Z3Top10RankingServer/mkt_40.txt')


	for line in stdout:
		print line.strip('\n')

	stdin, stdout, stderr = client.exec_command('cd ~/Z3Top10RankingServer; python ~/Z3Top10RankingServer/dungeon_test.py')
	for line in stdout:
		print "*" + line.strip('\n')

	scp.close()
	client.close()


if __name__ == '__main__':
	run()