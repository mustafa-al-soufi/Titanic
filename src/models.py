from catboost import CatBoostClassifier


def create_model():
    """
    Returns the final CatBoost model.
    """

    return CatBoostClassifier(
        iterations=250,
        depth=4,
        learning_rate=0.01,
        border_count=16,
        l2_leaf_reg=2,
        random_state=42,
        verbose=False,
    )
