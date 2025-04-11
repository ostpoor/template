# src/common/csv_writer.py
# このファイルは結果をCSVファイルに書き込むプログラムです。
# 主な役割は、結果をCSVファイルに書き込むことです。

import csv
import os

def write_to_csv(csv_file_path, data, headers=None):
    """
    結果をCSVファイルに書き込みます。
    Args:
        csv_file_path (str): CSVファイルのパス。
        data (list): 書き込むデータのリスト。
        headers (list): ヘッダーのリスト（オプション）。
    Returns:
        None
    """
    # フォルダが存在しない場合は作成
    os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)

    file_exists = os.path.isfile(csv_file_path)

    with open(csv_file_path, mode='a', newline='', encoding='CP932', errors='replace') as csv_file:
        csv_writer = csv.writer(csv_file)
        if headers and not file_exists:
            csv_writer.writerow(headers)
        csv_writer.writerow(data)
