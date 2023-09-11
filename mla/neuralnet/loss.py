from ..metrics import logloss

categorical_crossentropy = logloss


def get_loss(name):
    """Returns loss function by the name."""
    try:
        return globals()[name]
    except KeyError:
        raise ValueError("Invalid metric function.")
