while(True):
    result = 0.0;
    print("------------计算器------------");
    print("       【1】加法运算");
    print("       【2】减法运算");
    print("       【3】乘法运算");
    print("       【4】除法运算");
    print("       【0】程序结束");
    print("------------------------------");

    choice = input("请输入选项【0~4】:");

    if choice in ["1","2","3","4"]:
        num1 = float(input("请输入第一个数:"));
        num2 = float(input("请输入第二个数:"));
        if choice=="1":
            result = num1 + num2;
            print("------------加法------------");
            print(num1," + ",num2," = ",result);
        elif choice == "2":
            result = num1 - num2;
            print("------------减法------------");
            print(num1, " - ", num2, " = ", result);
        elif choice == "3":
            result = num1 * num2;
            print("------------乘法------------");
            print(num1, " * ", num2, " = ", result);
        elif choice == "4":
            result = num1 / num2;
            print("------------除法------------");
            print(num1, " / ", num2, " = ", result);
        print("-----------------------------");
    elif choice == "0":
        exit();
    else:
        print("输入有误,请输入0~4的数字");