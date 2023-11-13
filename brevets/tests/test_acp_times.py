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

def test_open_1150():
    start_time = arrow.get("2023-11-06T00:00:00")
    expected_open_time = start_time.shift(hours=33, minutes=5)
    assert open_time(1150, 1000, start_time) == expected_open_time

def test_open_200():
    start_time = arrow.get("2023-11-06T00:00:00")
    expected_open_time = start_time.shift(hours=5, minutes=53)
    assert open_time(200, 200, start_time) == expected_open_time

def test_open_50():
    start_time = arrow.get("2023-11-06T00:00:00")
    expected_open_time = start_time.shift(hours=1, minutes=28)
    assert open_time(50, 200, start_time) == expected_open_time

def test_open_150():
    start_time = arrow.get("2023-11-06T00:00:00")
    expected_open_time = start_time.shift(hours=4, minutes=25)
    assert open_time(150, 300, start_time) == expected_open_time

def test_open_450():
    start_time = arrow.get("2023-11-06T00:00:00")
    expected_open_time = start_time.shift(hours=12, minutes=8)
    assert open_time(450, 400, start_time) == expected_open_time

def test_close_50():
    start_time = arrow.get("2023-11-06T00:00:00")
    expected_close_time = start_time.shift(hours=3, minutes=30)
    assert close_time(50, 200, start_time) == expected_close_time

def test_close_150():
    start_time = arrow.get("2023-11-06T00:00:00")
    expected_close_time = start_time.shift(hours=10)
    assert close_time(150, 300, start_time) == expected_close_time

def test_close_400():
    start_time = arrow.get("2023-11-06T00:00:00")
    expected_close_time = start_time.shift(hours=27, minutes=00)
    assert close_time(400, 400, start_time) == expected_close_time

if __name__ == '__main__':
    nose.run()