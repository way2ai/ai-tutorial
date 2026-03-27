'''
预测函数
y = wx + b

w控制趋势
b控制位置
'''
def predict(x, w, b):
    return w * x + b

''' 
损失函数
L=1/n​∑(ypred​−ytrue​)**2
w = w - 𝜂∂𝐿/∂𝑤

∂L/∂w:w 变一点点，loss 会怎么变，即导数
η:学习率，你每次走多大一步

1.平方会避免为负数
2.平方会惩罚大错误
'''
def loss(y_pred, y_true):
    return (y_pred - y_true) ** 2

x = 2
y_true = 10
w = 3
b = 4
step = 0.1

for i in range(1000):
    y_pred = predict(x, w, b)
    current_loss = loss(y_pred, y_true)

    new_w = w + step
    new_y_pred = predict(x, new_w, b)
    new_loss = loss(new_y_pred, y_true)

    if new_loss < current_loss:
        w = new_w
    else:
        new_w = w - step
        new_y_pred = predict(x, new_w, b)
        new_loss = loss(new_y_pred, y_true)
        if new_loss < current_loss:
            w = new_w

print(f"w: {w}, b: {b}, loss: {current_loss}")