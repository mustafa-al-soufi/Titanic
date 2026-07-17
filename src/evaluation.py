from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


def evaluate_model(model, X_test, y_test):
    """
    Evaluates a trained model.
    """

    predictions = model.predict(X_test)

    print(f"Accuracy: {accuracy_score(y_test, predictions):.4f}")

    print()

    print(classification_report(y_test, predictions))

    print()

    print(confusion_matrix(y_test, predictions))
