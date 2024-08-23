import os

# 项目根目录
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 默认输出目录
DEFAULT_OUTPUT_DIR = os.path.join(PROJECT_ROOT, "results")

# 日志配置
LOG_CONFIG = {
    "output_dir": os.environ.get("METAGPT_LOG_DIR", DEFAULT_OUTPUT_DIR),
    "print_level": "INFO",
    "logfile_level": "DEBUG",
}