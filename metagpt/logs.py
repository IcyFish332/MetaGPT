#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/6/1 12:41
@Author  : alexanderwu
@File    : logs.py
"""

import sys
import os
from datetime import datetime

from loguru import logger as _logger

from metagpt.const import METAGPT_ROOT

# _print_level = "INFO"


# def define_log_level(print_level="INFO", logfile_level="DEBUG", name: str = None):
#     """Adjust the log level to above level"""
#     global _print_level
#     _print_level = print_level

#     current_date = datetime.now()
#     formatted_date = current_date.strftime("%Y%m%d")
#     log_name = f"{name}_{formatted_date}" if name else formatted_date  # name a log with prefix name

#     _logger.remove()
#     _logger.add(sys.stderr, level=print_level)
#     _logger.add(METAGPT_ROOT / f"logs/{log_name}.txt", level=logfile_level)
#     return _logger


# logger = define_log_level()


# def log_llm_stream(msg):
#     _llm_stream_log(msg)


# def set_llm_stream_logfunc(func):
#     global _llm_stream_log
#     _llm_stream_log = func


# def _llm_stream_log(msg):
#     if _print_level in ["INFO"]:
#         print(msg, end="")

from metagpt.configs import LOG_CONFIG

def define_log_level(logfile_level="INFO", name: str = None, output_dir: str = None, debug: bool = False):
    """Define log level"""
    _logger.remove()

    # 设置文件日志
    output_dir = output_dir or LOG_CONFIG["output_dir"]
    
    os.makedirs(output_dir, exist_ok=True)
    
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_name = f"{name}_{current_time}" if name else current_time
    log_file = os.path.join(output_dir, f"{log_name}.log")
    
    file_level = "DEBUG" if debug else logfile_level
    _logger.add(log_file, level=file_level)
    
    return _logger

logger = define_log_level()

def get_logger(name: str = None, output_dir: str = None, debug: bool = False):
    """Get a configured logger"""
    global logger
    logger = define_log_level(name=name, output_dir=output_dir, debug=debug)
    return logger

def log_llm_stream(msg):
    """Log LLM stream"""
    _llm_stream_log(msg)

def set_llm_stream_logfunc(func):
    """Set LLM stream log function"""
    global _llm_stream_log
    _llm_stream_log = func

def _llm_stream_log(msg):
    """Default LLM stream log function"""
    pass

print_level = LOG_CONFIG["print_level"]