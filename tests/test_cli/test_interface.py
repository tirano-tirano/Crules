"""
CLIインターフェースのテスト

このモジュールでは、CLIインターフェースのテストを実装します。
"""

import unittest
from unittest.mock import patch, MagicMock
from typing import Dict, Any

from src.cli.interface import CommandInterface


class TestCommandInterface(unittest.TestCase):
    """CLIインターフェースのテストクラス"""

    def setUp(self):
        """テストの前準備"""
        self.interface = CommandInterface()
        self.mock_command = MagicMock()
        self.mock_command.execute.return_value = True
        self.interface.commands = {
            "test": self.mock_command
        }

    def test_register_command(self):
        """コマンド登録のテスト"""
        # 新しいコマンドの登録
        new_command = MagicMock()
        self.interface.register_command("new", new_command)
        self.assertIn("new", self.interface.commands)
        self.assertEqual(self.interface.commands["new"], new_command)

        # 既存コマンドの上書き
        updated_command = MagicMock()
        self.interface.register_command("test", updated_command)
        self.assertEqual(self.interface.commands["test"], updated_command)

    def test_execute_command(self):
        """コマンド実行のテスト"""
        # 正常なコマンド実行
        result = self.interface.execute_command("test", {"arg": "value"})
        self.assertTrue(result)
        self.mock_command.execute.assert_called_once_with({"arg": "value"})

        # 存在しないコマンド
        result = self.interface.execute_command("non_existent", {})
        self.assertFalse(result)

    def test_execute_command_with_error(self):
        """エラー発生時のコマンド実行テスト"""
        self.mock_command.execute.side_effect = Exception("Test error")
        result = self.interface.execute_command("test", {})
        self.assertFalse(result)

    def test_get_command(self):
        """コマンド取得のテスト"""
        # 存在するコマンドの取得
        command = self.interface.get_command("test")
        self.assertEqual(command, self.mock_command)

        # 存在しないコマンドの取得
        with self.assertRaises(KeyError):
            self.interface.get_command("nonexistent")

    def test_get_help(self):
        """ヘルプの取得テスト"""
        # 存在するコマンドのヘルプ
        help_text = self.interface.get_help("test")
        self.assertIsInstance(help_text, str)
        self.assertIn("test", help_text)

        # 存在しないコマンドのヘルプ
        help_text = self.interface.get_help("non_existent_command")
        self.assertEqual(help_text, "Command not found")

    def test_list_commands(self):
        """コマンド一覧の取得テスト"""
        # 初期コマンドの確認
        commands = self.interface.list_commands()
        self.assertIsInstance(commands, list)
        self.assertIn("test", commands)

        # コマンドを追加して再確認
        self.interface.register_command("new", MagicMock())
        commands = self.interface.list_commands()
        self.assertIn("test", commands)
        self.assertIn("new", commands)


if __name__ == "__main__":
    unittest.main() 