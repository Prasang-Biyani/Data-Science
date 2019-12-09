# def add_employee(emp, emp_list=[]):
#     emp_list.append(emp)
#     print(emp_list)


# # print(add_employee.__defaults__)
# # add_employee('Prasang')
# # print(add_employee.__defaults__)
# # add_employee('Suresh')
# # print(add_employee.__defaults__)

# def add_employee_fixed(emp, emp_list=None) -> None:
#     if emp_list is None:
#         emp_list = list()
#     emp_list.append(emp)
#     print(emp_list)

# print(add_employee_fixed.__defaults__)
# add_employee_fixed('Prasang', ['Corey', 'Ramesh'])
# print(add_employee_fixed.__defaults__)
# add_employee_fixed('Suresh')
# print(add_employee_fixed.__defaults__)

import time
from datetime import datetime

def display_time(time_to_print=None):
    if time_to_print is None:
        time_to_print = datetime.now()
    print(time_to_print.strftime('%B %d, %Y %H:%M:%S'))

print(display_time.__defaults__)
display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()
