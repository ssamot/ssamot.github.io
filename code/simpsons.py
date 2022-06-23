import numpy as np
from sklearn.linear_model import LassoLarsCV, LinearRegression
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import ttest_ind

np.random.seed(0)

observations = 200

def Z_confounder():
    return -1* np.random.random(size=(observations, 1))
def T_treatment(Z):
    T =  np.rint(Z + np.random.random(size = (observations,1)))
    T [T > 1] = 1
    T[T < 0] = 0
    return T
def Y_outcome(Z, T):
    return -T + 5*Z

z = Z_confounder()
t = T_treatment(z)
y = Y_outcome(z, t)

hist_data = {"Confounding feature": z[:,0],
             "Treatment": t[:, 0],
             "Outcome": y[:,0]
             }
df = pd.DataFrame(hist_data)

t_test = ttest_ind(y[t == 1], y[t == 0])
print("Independent t-test p-value %.5f:"%(t_test[1],))
ATE = y[t == 1].mean() - y[t == 0].mean()
print("Difference in means:", ATE)


sns.violinplot(data=hist_data, x = "Treatment", y = "Outcome", colorpallete = "deep")
#plt.show()

X_clf = np.concatenate([z, t], axis = 1)

clf = LassoLarsCV(normalize=False)
clf.fit(X_clf,y[:,0])
y_hat = clf.predict(X_clf)


X_0 = np.concatenate([z,np.zeros(shape = (observations,1))], axis = 1)
X_1 = np.concatenate([z,np.ones(shape = (observations,1))], axis = 1)

clf_0 = LassoLarsCV(normalize=False)
clf_1 = LassoLarsCV(normalize=False)
clf_ignore_confounder = LassoLarsCV(normalize=False)

clf_0.fit(X_clf[(t == 0)[:, 0], :], y[t == 0])
clf_1.fit(X_clf[(t == 1)[:, 0], :], y[t == 1])
clf_ignore_confounder.fit(X_clf[:, 1:2], y)





ATE = (clf.predict(X_1) - clf.predict(X_0))
ATE_sep = (clf_1.predict(X_1) - clf_0.predict(X_0))
ATE_ignore = (clf_ignore_confounder.predict(X_1[:, 1:2]) - clf_ignore_confounder.predict(X_0[:, 1:2]))

#print("T-learner means:",clf_1.predict(X_1).mean(), clf_0.predict(X_0).mean())
#print("T-learner means:",clf_1.predict(X_1).mean(), clf_0.predict(X_0).mean())
#print("Ignoring confounder means:", clf_ignore_confounder.predict(X_1[:, 1:2]).mean(), clf_ignore_confounder.predict(X_0[:, 1:2]).mean(), )


print("ATE S-learner:",ATE.mean())
print("ATE T-learner:",ATE_sep.mean())
print("ATE Ignoring confounder:", ATE_ignore.mean())

plt.savefig("simpviolin.png", bbox_inches='tight')