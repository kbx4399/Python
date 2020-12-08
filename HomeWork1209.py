#1.有如下值集合[11,22,33,44,55,66,77,88,99,90],
# 将所有大于66的值保存至字典的第一个key中，将小于66值保存至第二个key的值中。
list1 = [11,22,33,44,55,66,77,88,99,90];
list2 = {"k1":[],"k2":[]};
for i in range(0,len(list1)):
    if list1[i] > 66:
        list2["k1"].append(list1[i]);
    elif list1[i] < 66:
        list2["k2"].append(list1[i]);
print("debug-list2",list2);

#2.有两个列表list1 = [11, 22, 33,55,66],list2 = [22, 33, 44,77,55,88],
# 将两个列表元素值相同的值放到字典dict的same键值名中,
# 将list1有list2没有的元素保存在list1Have键值名中,将list2有list1没有的元素保存在list2Have键值名中,
list1 = [11, 22, 33,55,66];
list2 = [22, 33, 44,77,55,88];
dict = {"same":[],"different":[],"list1Have":[],"list2Have":[]}
for i in range(0,len(list1)):
    for j in range(0,len(list2)):
        if list1[i] == list2[j]:
            dict["same"].append(list1[i]);
for i in range(0,len(list1)):
    if list1[i] not in list2:
        dict["list1Have"].append(list1[i]);
for j in range(0,len(list2)):
    if list2[j] not in list1:
        dict["list2Have"].append(list2[j]);
print("debug-list1",list1);
print("debug-list2",list2);
print("debug-dict",dict);