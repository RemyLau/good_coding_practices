import numpy as np
from sklearn.datasets import load_breast_cancer
x,y=load_breast_cancer(return_X_y=True)
x = (  x - x.mean(0)) / x.std(0)
RandIdx = np.random.permutation(x.shape[0])
xt, yt = x[RandIdx[:100]],y[RandIdx[:100]]
x, y = x[RandIdx[100:]],y[RandIdx[100:]]
from sklearn.linear_model import *
l = LogisticRegression(penalty="l2",   dual = False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver="lbfgs", max_iter=100, multi_class="auto", verbose=0, warm_start=False, n_jobs=None, l1_ratio=None)
l.fit(x, y)
print("score = " + str(l.score(xt, yt)))
