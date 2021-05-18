import time


def calculate_points(time_since_correct, wrong_streak):
    '''
    Calculate points acquired by getting a card correct.
    :param time_since_correct: Seconds since last correct answering.
    :param wrong_streak: Number of wrong answerings since the last correct.
    :return: Score gained. 
    '''
    score = max((0, time_since_correct / 2500))
    score = min(10, score)
    for _ in range(wrong_streak): score **= (1/3)
    return score


def calculate_loss(wrong_streak):
    '''
    Calculate points lossed by getting a card incorrect.
    :param wrong_streak: Number of wrong answerings since last correct.
    :return: Score lost.
    '''
    return max(0, min(3.5, wrong_streak * 1.3))  # looks like a relu