"""
Nose tests for acp_times.py

Write your tests HERE AND ONLY HERE.
"""
import collections.abc

import sys
sys.path.append("..")
from acp_times import open_time, close_time


import nose    # Testing framework
import logging
import arrow


logging.basicConfig(format='%(levelname)s:%(message)s',
                    level=logging.WARNING)
log = logging.getLogger(__name__)

def test_open_100():
    start_time = arrow.get("2023-11-06T00:00:00")
    expected_open_time = start_time.shift(hours=2, minutes=56)
    assert open_time(100, 200, start_time) == expected_open_time

def test_open_200():
    start_time = arrow.get("2023-11-06T00:00:00")
    expected_open_time = start_time.shift(hours=5, minutes=53)
    assert open_time(200, 200, start_time) == expected_open_time

if __name__ == '__main__':
    nose.run()