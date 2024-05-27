import pyautogui
import time
def solve(num):
    # 将10进制数字转为8位二进制字符串 7 => 00000111
    num1_bin = str(bin(num))[2:].rjust(8, "0")

    for i in range(len(num1_bin)):
        time.sleep(0.1)
        # 这一位是0就不操作
        if num1_bin[i] == "0":
            continue
        # 1这一位是1就用键盘输入数字（1-8分别代表128、64、32、16、8、4、2、1）
        else:
            pyautogui.typewrite(str(i + 1))
# 完成后键盘敲空格来提交
    pyautogui.typewrite(" ")# 获取用户输入，激活游戏窗口后模拟键盘输入，提交答案后再激活控制台窗口，等待用户继续输入
while True:
    num = input('请输入10进制数：')
    position = pyautogui.position()
    # 随便找游戏窗口一个空白位置
    pyautogui.moveTo(200, 200, duration=0.1)
    pyautogui.click()
    time.sleep(0.3)
    solve(int(num))
    # 鼠标移动回原位置
    pyautogui.moveTo(position, duration=0.1)
    pyautogui.click()