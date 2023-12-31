"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def get_int_vlan_map(config_filename):
    access_ports_dict = {}
    trunk_ports_dict = {}
    with open(config_filename, 'r', encoding='utf-8') as read_file:
        for elem in read_file:
            line = elem.strip()
            if line.startswith('interface'):
                intrf = line.split()[1]
            elif "trunk allowed" in line:
                trunk_ports_dict[intrf] = list(map(int, line.split()[-1].split(",")))
            elif "access vlan" in line:
                access_ports_dict[intrf] = int(line.split()[-1])
    return access_ports_dict, trunk_ports_dict


file_name = 'config_sw1.txt'

get_int_vlan_map(file_name)
