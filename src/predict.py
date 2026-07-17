import pandas as pd


def create_submission(model, X_submission, passenger_ids, filename):
    """
    Creates a Kaggle submission file.
    """

    predictions = model.predict(X_submission)

    submission = pd.DataFrame({"PassengerId": passenger_ids, "Survived": predictions})

    submission.to_csv(filename, index=False)

    return submission
