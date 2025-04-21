"""
ファイル操作モジュール

このモジュールは、ファイル操作に関する機能を提供します。
"""

import os
import shutil
from typing import List, Optional


class FileManager:
    """ファイル操作クラス"""

    @staticmethod
    def read_file(file_path: str) -> str:
        """
        ファイルを読み込む

        Args:
            file_path: ファイルパス

        Returns:
            ファイルの内容
        """
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def write_file(file_path: str, content: str) -> None:
        """
        ファイルに書き込む

        Args:
            file_path: ファイルパス
            content: 書き込む内容
        """
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            f.write(content)

    @staticmethod
    def copy_file(src_path: str, dst_path: str) -> None:
        """
        ファイルをコピーする

        Args:
            src_path: コピー元のパス
            dst_path: コピー先のパス
        """
        os.makedirs(os.path.dirname(dst_path), exist_ok=True)
        shutil.copy2(src_path, dst_path)

    @staticmethod
    def create_directory(dir_path: str) -> None:
        """
        ディレクトリを作成する

        Args:
            dir_path: ディレクトリパス
        """
        os.makedirs(dir_path, exist_ok=True)

    @staticmethod
    def listdir(dir_path: str) -> List[str]:
        """
        ディレクトリの内容を一覧表示する

        Args:
            dir_path: ディレクトリパス

        Returns:
            ディレクトリの内容のリスト
        """
        return os.listdir(dir_path)

    @staticmethod
    def detect_project_root(start_path: str = ".") -> Optional[str]:
        """
        プロジェクトルートを検出する

        Args:
            start_path: 検索開始パス

        Returns:
            プロジェクトルートのパス。見つからない場合はNone
        """
        current_path = os.path.abspath(start_path)
        while current_path != os.path.dirname(current_path):
            if os.path.exists(os.path.join(current_path, ".crules")):
                return current_path
            current_path = os.path.dirname(current_path)
        return None
