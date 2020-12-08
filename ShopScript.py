itemList = [{"itemName":"电脑","itemPrice":3000},
            {"itemName":"鼠标","itemPrice":500},
            {"itemName":"游艇","itemPrice":80000},
            {"itemName":"美女","itemPrice":100000},
            ];
shopList = [];
userMoney = 3500;
#userMoney = float(input("请输入您的资产:"));
choose1 = "";
choose2 = "";
itemBuy = "";
totalPrice = 0;
while True:
    print("-------------------现有商品--------------------");
    for i in range(0,len(itemList)):
        print("|   商品名:%s  价格:%d      |" % (itemList[i]["itemName"],itemList[i]["itemPrice"]));
    print("----------------------------------------------------");
    print("请输入您的操作:1-购买 2-结算 3-退出程序");
    choose1 = int(input("输入操作:"));
    print("debug-choose1", choose1)
    if choose1 == 1 :
        itemBuy = input("请输入您要购买的商品:");
        print("debug-itemBuy", itemBuy)
        for i in range(0,len(itemList)):
            if itemList[i]["itemName"] == itemBuy:
                shopList.append(itemList[i]);
                print("以添加进购物车!");
                break;
    elif choose1 == 2 :
        if len(shopList) == 0:
            print("您的购物车位空!");
        else:
            print("--------------------购物车---------------------");
            for i in range(0,len(shopList)):
                print("-商品名:%s  单价:%d" %(shopList[i]["itemName"],shopList[i]["itemPrice"]));
                totalPrice += shopList[i]["itemPrice"];
            print("-一共需要%d元" %(totalPrice));
            print("---------------------------------------------------");
            print("请输入您的操作:1-确认 2-取消")
            choose2 = input("输入操作:");
            if choose1 == "1" or "确认":
                if totalPrice < userMoney:
                    userMoney -= totalPrice;
                    print("购买成功!您的余额:",userMoney);
                else:
                    shopList = [];
                    print("余额不足购买失败,购物车已清空!");
            elif choose1 == "2" or "取消":
                shopList = [];
                print("购物车已清空!");
    elif choose1 == 3 :
        print("程序结束");
        exit();
