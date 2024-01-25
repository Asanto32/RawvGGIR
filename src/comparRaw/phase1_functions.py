"""Load data"""

#required imports
import sys
sys.path.append('/Users/adam.santorelli/lib/pygt3x/')

import calendar
from datetime import datetime, timedelta
import os
import numpy as np
import pandas as pd
import pygt3x
from pygt3x.reader import FileReader
from typing import Any


def _gt3loader_(filename):
    with FileReader(file_name) as reader:
        df = reader.to_pandas()
    return df

def _timefix_(raw_data,sampling_rate):
    #currently pygt3x does not save the ms data, we make the assumption that datapoints are saved
    # sequentially so that each new data point is one sample away from the previous
    timestamps = raw_data.index.to_numpy()
    time_fix = []
    for i in range(len(timestamps)):
        tmp = (timestamps[0] + ((i)/sampling_rate))*1000
        time_fix.append(tmp)
    time_fix_test = np.asarray(time_fix, dtype='datetime64[ms]')
    raw_data['time'] = time_fix_test
    return raw_data
