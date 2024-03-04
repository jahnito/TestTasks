import json
import random


with open('task2_part1_roles.json') as f:
    roles = json.load(f)

new_roles = []
roleids = set()

for i in roles:
    if 'roleid' in i:
        roleids.add(i['roleid'])


for i in roles:
    new_role = {}
    if 'name' in i:
        name = i['name'][:-1] + str(int(i['name'][-1]) + 1)
        new_role.update({'name':name})
    if 'order' in i:
        order = i['order'] + 1
        new_role.update({'order':order})
    if 'roleid' in i:
        x = random.randint(10, 100)
        while x in roleids:
            x = random.randint(1, 100)
        roleid = x
        # Исправление ошибки не уникальности, вместо списка использовано множество
        roleids.add(x)
        new_role.update({'roleid':roleid})
    for j in i:
        if j not in ('name', 'order', 'roleid'):
            new_role.update({j:i[j]})
    new_roles.append(new_role)


rol_names = []
for i in new_roles:
    rol_names.append(i['name'])

with open('out_roles.json', 'w') as f:
    json.dump(new_roles, f)

with open('out_rol_names.json', 'w') as f:
    json.dump(rol_names, f)
