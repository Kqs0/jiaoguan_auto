#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2023/9/14 11:15
# @Author : kouqingshan
import logging as logger
import time
import pytest

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

@pytest.fixture(scope="session", autouse=True)
def time_session_scope():
    start = time.time()
    logger.info('start: {}'.format(time.strftime(DATE_FORMAT, time.localtime(start))))

    yield

    finished = time.time()
    logger.info('finished: {}'.format(time.strftime(DATE_FORMAT, time.localtime(finished))))
    logger.info('Total Execution Time: {:.3f}s'.format(finished - start))

@pytest.fixture(autouse=True)
def time_function_scope():
    start = time.time()
    yield
    logger.info(' Execution Time: {:.3f}s'.format(time.time() - start))
