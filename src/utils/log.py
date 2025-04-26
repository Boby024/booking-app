import logging
import os

class Logger:
    def __init__(self, name: str = 'AppLogger', log_file: str = None, level: int = logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.propagate = False

        if not self.logger.handlers:
            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s'
            )

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

            if log_file:
                os.makedirs(os.path.dirname(log_file), exist_ok=True)
                file_handler = logging.FileHandler(log_file)
                file_handler.setFormatter(formatter)
                self.logger.addHandler(file_handler)

    def debug(self, msg: str):
        self.logger.debug(msg, stacklevel=2)

    def info(self, msg: str):
        self.logger.info(msg, stacklevel=2)

    def warning(self, msg: str):
        self.logger.warning(msg, stacklevel=2)

    def error(self, msg: str):
        self.logger.error(msg, stacklevel=2)

    def critical(self, msg: str):
        self.logger.critical(msg, stacklevel=2)
