import pandas as pd

# 创建一个简单的 DataFrame
data = {'Name': ['Google', 'Runoob', 'Taobao'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# 查看 DataFrame
print(df)

def test():
    apples = pd.Series([1,2,3,4])
    bananas = pd.Series([5,6,7,8])
    df = pd.DataFrame({'apple':apples, 'bananas':bananas})
    print(df)
    pass

if __name__ == '__main__':
    test()