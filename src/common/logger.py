# src/common/logger.py
# このファイルは、ログ設定と標準出力・標準エラー出力のリダイレクトを提供します。
# 主な役割は、ログファイルの設定、特定のエラーメッセージのフィルタリング、標準出力・標準エラー出力のリダイレクトです。

import sys
import os
import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_file, log_level=logging.INFO, log_to_console=True, encoding='utf-8'):
    """
    ログ設定を行う。ログディレクトリが存在しない場合は作成し、
    ログファイルにエラーメッセージを書き込む。
    log_to_consoleがTrueの場合、ターミナルにもエラーメッセージを出力する。
    """
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    logger = logging.getLogger()
    logger.setLevel(log_level)
    logger.handlers = []
    
    rotating_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=5, encoding=encoding)
    rotating_handler.setLevel(log_level)
    rotating_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
    logger.addHandler(rotating_handler)
    
    # コンソール出力設定
    if log_to_console:
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(logging.ERROR) # コンソールにはERRORレベル以上のみ出力
        stream_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
        logger.addHandler(stream_handler)
    
    # ログ開始時の区切り線を出力
    with open(log_file, 'a', encoding=encoding) as f:
        f.write("="*150 + "\n")
    
    logging.info(f"Logging setup completed. Log file: {log_file}, Log level: {log_level}, Log to console: {log_to_console}, Encoding: {encoding}")

