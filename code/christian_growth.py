import pandas as pd
import pylab as plt
from tqdm import trange
import numpy as np
import cma
from sklearn.metrics import \
    mean_absolute_percentage_error, \
    mean_squared_error, \
    mean_absolute_error, \
    mean_pinball_loss

np.set_printoptions(suppress=True)
np.set_printoptions(precision=2)

#data_file = "Stark.csv"
data_file = "Ehrman.csv"

def growth(a, r, X):
    return a * np.power(1 + r, X)

def training_loop_cma(model, x, y, initial_year, n=500):
    optimizer = cma.CMAEvolutionStrategy(x0=np.zeros(2), sigma0=1.3,
                                         inopts={"popsize":10,
                                                 "bounds": [[0,0], [None,None]],
                                                 "verbose":-100
                                                 }
                                         )
    with trange(n) as t:
        for i in t:
            solutions = []
            asked = optimizer.ask()
            for a,r in asked:
                y_hat = model(y[0], r, x - initial_year)
                error = mean_absolute_error(y,y_hat)
                solutions.append(error)

            t.set_description('Iter %i, loss %.3f, perc loss %.4f' % (i, error,r))
            optimizer.tell(asked, solutions)
    best = y[0], optimizer.best.x[1]
    return best


df = pd.read_csv(data_file)


df[df.columns[1]] = df.apply(lambda x: f"{int(x[df.columns[1]]):,}" , axis=1)
df[df.columns[2]] = df.apply(lambda x: f"{int(x[df.columns[2]]):,}" , axis=1)
df[df.columns[3]] = df.apply(lambda x: f"{int(x[df.columns[3]]):,}" , axis=1)

print(df.to_markdown(index=False))

df = df[[df.columns[0], df.columns[1]]]

best = training_loop_cma(growth, x = df["year"].to_numpy(), initial_year= df["year"].min(), y=df[df.columns[1]])

space = np.arange(df["year"].min(),df["year"].max(),0.1)
df_new = pd.DataFrame({'year':space,
              df.columns[1]:growth(best[0], best[1], space - df["year"].min())
              })

df = df.merge(df_new, on="year", how = "outer")
print(df)

long_df = pd.melt(df, id_vars=['year'], value_vars=[df.columns[1], df.columns[2]])
plt.scatter(x=df["year"], y=df[df.columns[1]], color = "r", label = "%s's estimates"%(data_file[:-4]))
plt.scatter(x=df["year"], y=df[df.columns[2]],
            color = "b", alpha = 0.5,
            s = 1,
            label = "$f(x) = %d (1 + %.4f)^x$"%(df[df.columns[1]][0], best[1] ))

plt.xlabel("Year")
plt.ylabel("Number of Christians")
plt.legend()

plt.savefig("./%s_cgrowth.png"%(data_file[:-4]),dpi=500,bbox_inches='tight', pad_inches=0)



