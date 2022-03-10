import math
exp = abs(3.0*(4.0/3.0-1)-1)
def machine_epsilon():
    epsilon_machine = 1
    while (1 + epsilon_machine) != 1:
         epsilon =epsilon_machine
         epsilon_machine = epsilon_machine/2
    return epsilon

print(machine_epsilon())

