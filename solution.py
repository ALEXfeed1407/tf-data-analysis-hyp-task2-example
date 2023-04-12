import pandas as pd
import numpy as np


chat_id = 288759659 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    import scipy.stats as st
    alpha = 0.07
    a = st.anderson_ksamp([x, y]).pvalue
    return a < alpha
