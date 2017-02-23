import numpy as np

y = np.array([1,0,0,0,1,1,0,0,0,0,1])
y_predict = np.array([1,1,0,1,0,1,0,1,0,1,1])

#索引
predict_index_p = (y_predict == 1)  #预测为正类的
predict_index_n = (y_predict == 0)  #预测为负类

index_p = (y==1)  #实际为正类
index_n = (y==0)  #实际为负类

Tp = sum(y[predict_index_p])       #正确预测的正类  （实际为正类 预测为正类）
Tn = sum([1 for x in list(y[predict_index_n]) if x == 0]) #正确预测的负类   (实际为负类 预测为负类)

Fn = sum(y_predict[index_n])       #错误预测的负类  （实际为负类 预测为正类）
Fp = sum(y[predict_index_n])       #错误预测的正类   (实际为正类 预测为负类)

acc = (Tp+Tn)/(Tp+Tn+Fp+Fn)
sn = Tp/(Tp+Fn)
sp = Tn/(Tn+Fp)


print((Tp+Tn)/(Tp+Tn+Fp+Fn))
print(np.mean(y==y_predict))


