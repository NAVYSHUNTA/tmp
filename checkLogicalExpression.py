# ハードウェア実験Iの論理式正誤判定プログラム。
"""
========================================================
                <author:Shunta Nakamura>
========================================================
"""
# 論理式を書くと状態が出力されるので、手元の状態遷移図と一致しているか確認する。もし、一致していれば、その論理式は正しい。
# Q3, Q2, Q1, Q0はそれぞれstate[3], state[2], state[1], state[0]と書く。
# Q1の否定はgetNot()を用いてgetNot(state[1])と書く。
# getQxのreturnにはQxの論理式を書く。例えば、Q3の論理式はgetQ3に書く。
# andは&、orは|で書く。すなわち、「・」は「&」で、「+」は「|」と書く。
state = [0, 0, 0, 0]

# 否定の定義(編集しなくて良い)
def getNot(data):
    if data:
        return 0
    else:
        return 1

# 論理式Q3
def getQ3():
    return state[3] & getNot(state[1]) | state[0] & state[1] & getNot(state[3])

# 論理式Q2
def getQ2():
    return getNot(state[1]) | getNot(state[0])

# 論理式Q1
def getQ1():
    return state[1] ^ state[0] | getNot(state[1]) & state[3] & state[2]

# 論理式Q0
def getQ0():
    return state[1] & getNot(state[0]) | state[2] & getNot(state[0])

print(state[::-1])
for i in range(20):
    state[0], state[1], state[2], state[3] = getQ0(), getQ1(), getQ2(), getQ3()
    print(state[::-1])
