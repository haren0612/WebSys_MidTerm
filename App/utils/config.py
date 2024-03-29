import os


LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
HISTORY_SAVE_PATH = os.getenv('HISTORY_SAVE_PATH', 'operations_history.csv')
ENABLE_HISTORY_FEATURE = os.getenv('ENABLE_HISTORY_FEATURE', 'False') == 'True'