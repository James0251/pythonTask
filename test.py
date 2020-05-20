from pssh.clients import ParallelSSHClient
import json

f = open('file.json', "r")
json_data = json.load(f)
hosts = list()
for value in json_data['servers']:
    hosts.append(value['host'])
for host in hosts:
    host_array = [host]
    client = ParallelSSHClient(host_array, user=value['login'], password=value['password'])
    file = open('command.txt', 'r')
    print("Результат выполнения комманд для сервера %s" % host)
    for line in file:
        output = client.run_command(line)
        # for host, host_output in output.items():
        stdout = list(output[host]['stdout'])
        print("%s is %s" % (line.rstrip(), stdout,))
    print()
