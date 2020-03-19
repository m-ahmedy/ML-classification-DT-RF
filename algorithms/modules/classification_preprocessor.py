def preprocessor(dataset, X_index, y_index, feature_scaling = True, test_size = 0.25, random_state = 0):
    """
    Quick utility that wraps preprocessor template to perform importing, splitting and optional feature scaling on the dataset.

    """

    # Importing the libraries
    import os.path as path
    import pandas as pd

    # Importing the dataset
    dirname = path.dirname(__file__)
    filename = path.join(dirname, '..\\datasets\\' + dataset)
    dataset = pd.read_csv(filename)
    X = dataset.iloc[:, X_index].values
    y = dataset.iloc[:, y_index].values

    # Splitting the dataset into the Training set and Test set
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = test_size, random_state = random_state)

    # Feature Scaling
    if feature_scaling :
        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler()
        X_train = sc.fit_transform(X_train)
        X_test = sc.transform(X_test)
    
    return list([X_train, X_test, y_train, y_test])