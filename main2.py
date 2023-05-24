import subprocess

with open("ip_list.txt") as file:
    ip_list = file.read().splitlines()

with open("ip_output.txt", "w") as output_file:
    for ip in ip_list:
        response = subprocess.run(["ping", "-n", "1", ip], capture_output=True, text=True)
        
        if "Esgotado o tempo limite do pedido" in response.stdout or "unreachable" in response.stdout:
            status_message = f"{ip} link is down\n"
        else:
            status_message = f"{ip} is up\n"

        print(response.stdout)
        output_file.write(status_message)

with open("ip_output.txt") as file:
    output = file.read()
    print(output)
