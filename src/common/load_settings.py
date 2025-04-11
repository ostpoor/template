# src/common/load_settings.py
# このファイルは設定ファイルを読み込むプログラムです。
# 主な役割は設定ファイルの読み込みと設定値の取得です。

import configparser

def load_settings(file_path: str):
    config = configparser.RawConfigParser()
    with open(file_path, 'r', encoding='utf-8') as file:
        config.read_file(file)
    return config
