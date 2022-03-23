from datetime import datetime


def get_timesetting():
    return datetime.now().strftime("%d-%m-%Y-%H:%M:%S")[:-3]