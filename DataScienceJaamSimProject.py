import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.metrics as met
import scipy.stats as stats


##Step1
# df = pd.read_csv("/Users/nicolashayek/Desktop/datascienceproject1.csv", skiprows=13, delimiter=";")
# print(df)
# # #
# df.to_csv("/Users/nicolashayek/Desktop/datascienceproject1.csv", index=False)

# #step2
df = pd.read_csv("/Users/nicolashayek/Desktop/datascienceproject1.csv", delimiter=",")
print(df)
#
# #step3
df1 = df.rename(columns={'this.SimTime/1[min]': 'simtime',
                            'this.obj': 'production',
                            'this.obj.StateTimes("bag")/1[s]': 'bag',
                            'this.obj.StateTimes("pack")/1[s]': 'pack'})
print(df1)
#
#
df1.to_csv("/Users/nicolashayek/Desktop/datascienceproject1.csv", index=False)

df = pd.read_csv("/Users/nicolashayek/Desktop/datascienceproject1.csv",  delimiter=",")
# print(df.columns)
print(df[df["simtime"].isnull()])
print(df[df["production"].isnull()])
print(df[df["bag"].isnull()])
print(df[df["pack"].isnull()])
# df["pack"] = pd.to_datetime(df["pack"])
# print(df)

# df["pack"] = pd.to_numeric(df["pack"])
# print(df)

# df.drop([18, 22, 28], inplace=True)
# df.dropna(inplace=True)
print(df[df.duplicated()])

print(df.corr())
print(df.describe())
x = df['simtime']
y = df['bag']
plt.scatter(x, y, color = 'green')
plt.grid(axis='x', c='red', ls='--', lw=1.5)
plt.show()

print(stats.linregress(x, y))
slope, intercept, r, p, std_err = stats.linregress(x, y)
def predict(x_val):
    y_val = slope * x_val + intercept
    return y_val
y1 = []
for i in range(len(x)):
    y1.append(slope * x[i] + intercept)
# predicting one particular
x_value = eval(input("Enter the Simtime is:"))
y_value = predict(x_value)
print("The predicted bagtime is", y_value)
# all the graphs+ the predicted.
plt.scatter(x, y)
plt.scatter(x, y1)
plt.plot(x, y1)
plt.plot(x_value, y_value, marker="x", markersize=20, color="red")
plt.show()


print(df.corr())
x = df['simtime']
y = df['bag']
plt.scatter(x, y)
plt.show()

print(stats.linregress(x, y))
slope, intercept, r, p, std_err = stats.linregress(x, y)
#show them as scatter

# train/test division
train_x = x[:4500]
train_y = y[:4500]
test_x = x[4500:]
test_y = y[4500:]
#scatter for train/ scatter for test
plt.scatter(train_x, train_y, color="green")
plt.scatter(test_x, test_y, color="red")
regmodel = np.poly1d(np.polyfit(train_x, train_y, 1))
x1 = np.linspace(0, 5588, 5588)

plt.plot(x1, regmodel(x1))
plt.show()



print(regmodel)
# getting r2 for train and for test
print(met.r2_score(train_y, regmodel(train_x)))
# print(met.r2_score(test_y, regmodel(test_x)))
#predicting the x=6900
print(regmodel(6900))
