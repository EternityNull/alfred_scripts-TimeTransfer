#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import json
from datetime import datetime
from alfred import *

TIMESTAMP_SEC_RE = r'^\d{10}$'  # 1643372599
TIMESTAMP_MSEC_RE = r'^\d{13}$'  # 1643372599000
# 2022-01-28 10:00:00
DATETIME_LONG_STR = r'^[1-9]\d{3}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$'
DATETIME_SHORT_STR = r'^[1-9]\d{13}$'  # 20220128100000


def judge_input(input_arg: str):
    date_now = input_datetime = datetime.now()
    title_to_display = result_to_display = str()

    if re.match(TIMESTAMP_SEC_RE, input_arg):
        input_datetime = datetime.fromtimestamp(float(input_arg))
        result_to_display = input_datetime.strftime("%Y-%m-%d %H:%M:%S")
        title_to_display = "日期时间: %s" % result_to_display

    elif re.match(TIMESTAMP_MSEC_RE, input_arg):
        input_datetime = datetime.fromtimestamp(float(int(input_arg) / 1000))
        result_to_display = input_datetime.strftime("%Y-%m-%d %H:%M:%S")
        title_to_display = "日期时间: %s" % result_to_display

    elif re.match(DATETIME_SHORT_STR, input_arg):
        input_datetime = datetime.strptime(input_arg, "%Y%m%d%H%M%S")
        result_to_display = int(input_datetime.timestamp())
        title_to_display = "时间戳: %s" % result_to_display

    elif re.match(DATETIME_LONG_STR, input_arg):
        input_datetime = datetime.strptime(input_arg, "%Y-%m-%d %H:%M:%S")
        result_to_display = int(input_datetime.timestamp())
        title_to_display = "时间戳: %s" % result_to_display

    else:
        exit(1)

    diff_days = (date_now - input_datetime).days
    diff_secs = (date_now - input_datetime).seconds

    subtitle_to_display = "距离当前时间 [%s] 天 + [%s] 秒" % (
        diff_days, diff_secs)

    return Alfred(title_to_display, subtitle_to_display, result_to_display).__dict__


def judge_now():
    date_now = datetime.now()

    display_list = list()

    # 日期格式 dict
    display_list.append(
        Alfred(
            title=date_now.strftime("%Y-%m-%d %H:%M:%S"),
            subtitle='日期格式',
            arg=date_now.strftime("%Y-%m-%d %H:%M:%S")
        ).__dict__
    )

    # 时间戳格式 dict
    display_list.append(
        Alfred(
            title=int(date_now.timestamp()),
            subtitle='秒级时间戳',
            arg=int(date_now.timestamp())
        ).__dict__
    )

    return display_list


if __name__ == '__main__':
    input_args = sys.argv[1:]

    if len(input_args) > 2:
        exit(1)

    input_arg = ' '.join(input_args)

    alfred_result = list()

    if input_arg == 'now':
        alfred_result.extend(judge_now())
    else:
        alfred_result.append(judge_input(input_arg))

    print(json.dumps({"items": alfred_result}))
