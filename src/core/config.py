"""
設定管理モジュール

このモジュールは、プロジェクトの設定を管理する機能を提供します。
"""

import os
from typing import Any, Dict

import yaml


class ConfigManager:
    """設定管理クラス"""

    def __init__(self, config_path: str = ".crules/config.yaml"):
        """
        初期化

        Args:
            config_path: 設定ファイルのパス
        """
        self.config_path = config_path
        self.config: Dict[str, Any] = {}

    def load_config(self) -> Dict[str, Any]:
        """
        設定を読み込む

        Returns:
            設定データ
        """
        if not os.path.exists(self.config_path):
            return {}

        with open(self.config_path, "r") as f:
            self.config = yaml.safe_load(f) or {}
        return self.config

    def save_config(self) -> None:
        """設定を保存する"""
        os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        with open(self.config_path, "w") as f:
            yaml.dump(self.config, f)

    def get(self, key: str, default: Any = None) -> Any:
        """
        設定値を取得する

        Args:
            key: 設定キー
            default: デフォルト値

        Returns:
            設定値
        """
        return self.config.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """
        設定値を設定する

        Args:
            key: 設定キー
            value: 設定値
        """
        self.config[key] = value
        self.save_config()
