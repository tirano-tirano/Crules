"""
設定管理モジュールのテスト

このモジュールは、設定管理機能のテストを提供します。
"""

import os
import tempfile
import unittest

from src.core.config import ConfigManager


class TestConfigManager(unittest.TestCase):
    """ConfigManagerのテストクラス"""

    def setUp(self):
        """テストの準備"""
        self.temp_dir = tempfile.mkdtemp()
        self.config_path = os.path.join(self.temp_dir, "config.yaml")
        self.config_manager = ConfigManager(self.config_path)

    def tearDown(self):
        """テストの後処理"""
        if os.path.exists(self.config_path):
            os.remove(self.config_path)
        os.rmdir(self.temp_dir)

    def test_load_config_empty(self):
        """空の設定を読み込むテスト"""
        config = self.config_manager.load_config()
        self.assertEqual(config, {})

    def test_save_config(self):
        """設定を保存するテスト"""
        test_config = {"template_name": "test_template"}
        self.config_manager.config = test_config
        self.config_manager.save_config()
        self.assertTrue(os.path.exists(self.config_path))

    def test_get_config(self):
        """設定値を取得するテスト"""
        test_config = {"template_name": "test_template"}
        self.config_manager.config = test_config
        value = self.config_manager.get("template_name")
        self.assertEqual(value, "test_template")

    def test_get_config_default(self):
        """設定値のデフォルト値を取得するテスト"""
        value = self.config_manager.get("non_existent", "default")
        self.assertEqual(value, "default")

    def test_set_config(self):
        """設定値を設定するテスト"""
        self.config_manager.set("template_name", "test_template")
        self.assertEqual(self.config_manager.config["template_name"], "test_template")
        self.assertTrue(os.path.exists(self.config_path))


if __name__ == "__main__":
    unittest.main()
