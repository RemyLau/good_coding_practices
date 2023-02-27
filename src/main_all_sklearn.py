from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def main(test_num: int = 100):
    # Load data
    x_raw, y = load_breast_cancer(return_X_y=True)

    # Transform features
    x = StandardScaler().fit_transform(x_raw)

    # Prepare train/test splits
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_num)

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
