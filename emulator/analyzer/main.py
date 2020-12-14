#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import os
import sys
import time
import enum
import warnings


from extract_stamp import extract_stamp
from log_parse import log_parse



def get_execution_durations(binary_prefix):
    assert type(binary_prefix) == str, TypeError

    annot_file_name = "{}.dump.annot".format(binary_prefix)
    (start_stamp, end_stamp) = extract_stamp(annot_file_name)
    print("(start_stamp, end_stamp) = ", (start_stamp, end_stamp))

    log_file_name = "{}.log".format(binary_prefix)
    results = log_parse(log_file_name, start_stamp=start_stamp, end_stamp=end_stamp)
    # print(results)

    execution_durations = []
    for log_dict in results:
        execution_start_time = log_dict["execution_start_time"]
        execution_end_time = log_dict["execution_end_time"]
        duration = execution_end_time - execution_start_time
        execution_durations.append(duration)
    print(execution_durations)


if __name__ == "__main__":
    get_execution_durations(binary_prefix="test")