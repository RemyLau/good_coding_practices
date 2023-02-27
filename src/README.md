## Fixing spaghetti XP

Use line breks to give some visual separation of imports and code

```python
import numpy as np
from sklearn.datasets import load_breast_cancer

# We need a line break after the imports (two lines if we are are defining a function)
...
```

Spaces are important! You don't want too many or too little.

```diff
- x,y=load_breast_cancer(return_X_y=True)
- x = (  x - x.mean(0)) / x.std(0)
+ x, y = load_breast_cancer(return_X_y=True)
+ x = (x - x.mean(0)) / x.std(0)
```

Use lowercase only for variable names (and spaces!).

```diff
- RandIdx = np.random.permutation(x.shape[0])
- xt, yt = x[RandIdx[:100]],y[RandIdx[:100]]
- x, y = x[RandIdx[100:]],y[RandIdx[100:]]
+ rand_idx = np.random.permutation(x.shape[0])
+ xt, yt = x[rand_idx[:100]], y[rand_idx[:100]]
+ x, y = x[rand_idx[100:]], y[rand_idx[100:]]
```

Be explicit about imports and move them to top level if possible.

```python
...
# Under most circumstances, imports should be at the top level
# Do not use *; explicitly specify the module/class/function used instead
from sklearn.linear_model import *
...
```

```python
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.linea_model import LogisticRegression
```

Wrap lines if it becomes too long! The letter `l` could be quite confusing to read depending on the font.

```diff
- l = LogisticRegression(penalty="l2",   dual = False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1, class_weight=None, random_state=None, solver="lbfgs", max_iter=100, multi_class="auto", verbose=0, warm_start=False, n_jobs=None, l1_ratio=None)
+ model = LogisticRegression(penalty="l2",   dual = False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1,
+                            class_weight=None, random_state=None, solver="lbfgs", max_iter=100, multi_class="auto",
+                            verbose=0, warm_start=False, n_jobs=None, l1_ratio=None)
```

Use Python features to you advantage, e.g., f-strings.

```diff
- l.fit(x, y)
- print("score = " + str(l.score(xt, yt)))
+ print(f"Test score: {model.score(xt, yt)}")
```
