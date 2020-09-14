def parse_file(hosts_filename: str) -> dict:
    with open('hosts.txt', 'r') as f:
        host_list = [line.strip() for line in f]
        hosts_dic = {host.split('=')[0]: host.split('=')[1] for host in host_list}
        return hosts_dic


def get_Computer_names(computer_nuames_list: list, hosts_dic: dict):
    # [name+'->'+hosts_dic[name] for name in computer_nuames_list if name in hosts_dic]
    for name in computer_nuames_list:
        if name in hosts_dic:
            print(f'{name} -> {hosts_dic[name]}')
        else:
            print(f"{name} doesn't exist")


hsots = parse_file('hosts.txt')
names = get_Computer_names(['work', 'amiel', 'home'], hsots)

"""
Uri's comments:
==============

* You didn't get the input from the command line.
* In Python it's common to use function names in lowercase. You can use "_" to separate between words.
  For example, use "get_computer_names" instead of "get_Computer_names".

"""
