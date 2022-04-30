import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from strategies.run_zipline import run_strategy


def main():
    perf = run_strategy("scalping")
    perf.to_csv("scalping.csv")


if __name__ == '__main__':
    main()
