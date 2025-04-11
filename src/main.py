# src/main.py
# このファイルは軽油や作動油の発注作業を効率化するためのメインプログラムです。
# 主な役割は設定ファイルの読み込みとログ設定です。

import os
import logging
from common.load_settings import load_settings
from common.logger import setup_logging

def initialize_settings_and_logging(settings_file_path):
    """
    設定ファイルの読み込みとログ設定を行う関数。
    
    Args:
        settings_file_path (str): 設定ファイルのパス。
    
    Raises:
        FileNotFoundError: 設定ファイルが見つからない場合に発生。
    """
    # 設定ファイルの読み込み
    if not os.path.exists(settings_file_path):
        raise FileNotFoundError(f"設定ファイルが見つかりません: {settings_file_path}")
    
    config = load_settings(settings_file_path)
    
    # ログ設定
    log_file_path = config['log']['log_file_path']
    log_level = getattr(logging, config['log']['log_level'].upper(), logging.INFO)
    setup_logging(log_file_path, log_level)
    
    # ログ設定完了メッセージ
    logging.info("ログ設定が完了しました。")

def main():
    # 設定ファイルのパス
    settings_file_path = './config/settings.ini'
    
    # 設定とログの初期化
    initialize_settings_and_logging(settings_file_path)

if __name__ == "__main__":
    main()
