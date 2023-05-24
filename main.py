import os


with open("ip_list.txt") as file:
    ip_list = file.read().splitlines()


for ip in ip_list:
    response = os.popen(f"ping -n 1 {ip}").read()

    
    if "Esgotado o tempo limite do pedido" in response or "unreachable" in response:
        print(response)
        with open("ip_output.txt", "a") as f:
            f.write(str(ip) + ' link is down' + '\n')
    else:
        print(response)
        with open("ip_output.txt", "a") as f:
            f.write(str(ip) + ' is up ' + '\n')


with open("ip_output.txt") as file:
    output = file.read()
    print(output)


with open("ip_output.txt", "w") as file:
    pass
