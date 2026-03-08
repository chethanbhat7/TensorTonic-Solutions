import numpy as np

def dropout(x, p=0.5, rng=None):
    x = np.array(x, dtype=float)

    if rng is None:
        rng = np.random.default_rng()

    r = rng.random(x.shape)

    mask = (r < (1 - p)).astype(float) * (1/(1-p))

    output = x * mask

    return output, mask