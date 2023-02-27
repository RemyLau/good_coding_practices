import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression


def main(test_num: int = 100):
    # Load data
    x, y = load_breast_cancer(return_X_y=True)

    # Transform features
    x = (x - x.mean(0)) / x.std(0)

    # Prepare train/test splits
    rand_idx = np.random.permutation(x.shape[0])
    test_idx, train_idx = rand_idx[:test_num], rand_idx[test_num:]
    x_train, y_train = x[train_idx], y[train_idx]
    x_test, y_test = x[test_idx], y[test_idx]

    # Train model
    model = LogisticRegression(penalty="l2", dual=False, tol=0.0001, C=1.0, fit_intercept=True, intercept_scaling=1,
                               class_weight=None, random_state=None, solver="lbfgs", max_iter=100, multi_class="auto",
                               verbose=0, warm_start=False, n_jobs=None, l1_ratio=None)
    model.fit(x_train, y_train)

    # Evaluate model predictions
    print(f"Train score: {model.score(x_train, y_train):.3f}")
    print(f"Test score: {model.score(x_test, y_test):.3f}")


if __name__ == "__main__":
    main()
