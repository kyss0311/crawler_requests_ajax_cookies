def dos(str):
    group = []
    part = []
    for i in str:
        if i == ' ' or i == ',':
            group.append(part)
            part = []
            continue
        part.append(i)
    group.append(part)
    return group

s = input()
att = dos(s)

shop = input()
req = dos(shop)
att_list = []
for i in range(len(req)-1):
    nor = {}
    for ob in (req[i] + req[i + 1]):
        if ob in nor:
            nor[ob] += 1
        else:
            nor[ob] = 1
        if nor[ob] >= 6 and ob not in att_list:
            att_list.append(ob)
    # print(nor)
    for j in range(len(att)):
        num = 0
        for attacker in att[j]:
            if attacker in nor:
                num += nor[attacker]

            if num >= 6:
                for i in att[j]:
                    if i not in att_list:
                        att_list.append(i)

att_list = sorted(att_list)
print('Attacker')
if len(att_list):
    for x in att_list:
        if x == att_list[-1]:
            print(x)
        else:
            print(x, end=' ')
else:
    print()

normal_list = []
for y in s+shop:
    if y not in (att_list + normal_list):
        if y == ' ' or y == ',' or y not in shop:
            continue
        normal_list.append(y)
print('Normal')
for z in sorted(normal_list):
    if z == sorted(normal_list)[-1]:
        print(z)
    else:
        print(z, end=' ')
