import pandas as pd
import numpy as np


chat_id = 288759659 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    from scipy.stats import ks_2samp
    alpha = 0.07
    stat1, p1 = ks_2samp(x, y)
    return p1 < alpha # Ваш ответ, True или False
