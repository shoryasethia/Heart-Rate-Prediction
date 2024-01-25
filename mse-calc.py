import sys
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

rdd=pd.read_csv("results.csv")
res=pd.read_csv(sys.argv[1])
mse2=mean_squared_error(rdd['HR'],res['HR'])
r22=r2_score(rdd['HR'],res['HR'])
print(f"MSE on test data : {mse2}")