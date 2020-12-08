import random
number = random.randint(1,100);
count = 0;
print("猜数字游戏开始");
while count < 5:
    guess = int(input("请输入一个数(1~10):"));
    if guess > number:
        print("猜大了");
        count+=1;
    elif guess < number:
        print("猜小了");
        count += 1;
    else:
        print("猜对了,游戏结束");
        break;
else:
    print("猜错5次了,游戏结束");
