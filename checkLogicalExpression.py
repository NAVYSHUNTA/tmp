# ハードウェア実験Iの論理式正誤判定プログラム。
"""
========================================================
                <author:Shunta Nakamura>
========================================================
"""
# 論理式を書くと状態が出力されるので、手元の状態遷移図と一致しているか確認する。もし、一致していれば、その論理式は正しい。
# Q3, Q2, Q1, Q0はそれぞれstate[3], state[2], state[1], state[0]と書く。
# Q1の否定はgetNot()を用いてgetNot(state[1])と書く。
# getDxのreturnにはDxの論理式を書く。例えば、D3の論理式はgetD3に書く。
# andは&、orは|で書く。すなわち、「・」は「&」で、「+」は「|」と書く。
state = [0, 0, 0, 0]

# 否定の定義(編集しなくて良い)
def getNot(data):
    if data:
        return 0
    else:
        return 1

# 論理式D3
def getD3():
    return state[3] & getNot(state[1]) | state[0] & state[1] & getNot(state[3])

# 論理式D2
def getD2():
    return getNot(state[1]) | getNot(state[0])

# 論理式D1
def getD1():
    return state[1] ^ state[0] | getNot(state[1]) & state[3] & state[2]

# 論理式D0
def getD0():
    return state[1] & getNot(state[0]) | state[2] & getNot(state[0])

print(state[::-1])
for i in range(20):
    state[0], state[1], state[2], state[3] = getD0(), getD1(), getD2(), getD3()
    print(state[::-1])
