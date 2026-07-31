# 任务1.5：猜数字游戏
import random


def get_xy(guess, target):
    """计算xAyB"""
    a = 0
    b = 0

    # 转换为字符串方便处理
    guess_str = str(guess).zfill(4)
    target_str = str(target).zfill(4)

    # 计算A（位置和数字都正确）
    for i in range(4):
        if guess_str[i] == target_str[i]:
            a += 1

    # 计算B（数字正确但位置不对）
    for i in range(4):
        if guess_str[i] in target_str:
            # 确保不是重复计数
            if guess_str[i] != target_str[i]:
                # 检查这个数字在目标中出现的次数
                if guess_str.count(guess_str[i]) <= target_str.count(guess_str[i]):
                    b += 1

    # 修正B：减去多算的
    # 简单方法：计算所有匹配的数字，减去A就是B
    common = 0
    for digit in set(guess_str):
        common += min(guess_str.count(digit), target_str.count(digit))
    b = common - a

    return a, b


def play_game():
    """猜数字游戏主函数"""
    # 生成随机四位数（0000-9999）
    target = random.randint(0, 9999)
    target_str = str(target).zfill(4)

    print("任务1.5：猜数字游戏")
    print("游戏规则：猜一个4位数（0000-9999），每次反馈xAyB")
    print("A表示数字和位置都对，B表示数字对但位置不对")
    print("目标数字已生成，开始猜吧！")

    attempts = 0
    while True:
        try:
            guess = input("\n请输入你的猜测（4位数字）：").strip()

            # 输入验证
            if not guess.isdigit() or len(guess) != 4:
                print("请输入4位数字！")
                continue

            guess_num = int(guess)
            attempts += 1

            a, b = get_xy(guess_num, target)
            print(f"结果: {a}A{b}B")

            if a == 4:
                print(f"恭喜你猜对了！答案是{target_str}")
                print(f"你总共猜了{attempts}次")
                break

        except ValueError:
            print("输入无效，请重试")


# 运行游戏
play_game()