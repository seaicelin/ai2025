import torch
import pandas as pd
import os

def test():
    print(os.getcwd())
    train_data = pd.read_csv('covid.train_new.csv').values
    print(train_data)

    x_train,y_train = train_data[:, :-1], train_data[:, -1]
    print(x_train.shape)
    print(y_train.shape)
    pass


if __name__ == '__main__':
    # 获取当前 Python 文件的目录
    current_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_directory)  # 更改工作目录

    test()
    pass