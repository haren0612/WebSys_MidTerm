"""
Load environment variables from .env file and set default
values for LOG_LEVEL, HISTORY_SAVE_PATH, and ENABLE_HISTORY_FEATURE.
"""

import os
from dotenv import load_dotenv

load_dotenv()


LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
HISTORY_SAVE_PATH = os.getenv('HISTORY_SAVE_PATH', 'operations_history.csv')
ENABLE_HISTORY_FEATURE = os.getenv('ENABLE_HISTORY_FEATURE', 'False')