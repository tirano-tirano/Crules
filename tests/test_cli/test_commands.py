"""
CLIコマンドのテスト

このモジュールでは、CLIコマンドのテストを実装します。
"""

import unittest
from unittest.mock import MagicMock, PropertyMock, patch

from src.cli.commands import AddCommand, InitCommand, ListCommand


class TestInitCommand(unittest.TestCase):
    """初期化コマンドのテストクラス"""

    def setUp(self):
        """テストの前準備"""
        self.mock_file = MagicMock()
        self.mock_config = MagicMock()
        self.mock_template = MagicMock()
        type(self.mock_template).template_dir = PropertyMock(
            return_value="/test/templates"
        )
        self.command = InitCommand(
            config_manager=self.mock_config,
            file_manager=self.mock_file,
            template_manager=self.mock_template,
        )

    def test_execute(self):
        """コマンド実行のテスト"""
        # 正常な実行
        self.mock_file.detect_project_root.return_value = "/test/project"
        self.mock_file.listdir.return_value = ["test_rule.yaml"]
        args = {"project_name": "test-project"}
        result = self.command.execute(args)
        self.assertTrue(result)
        self.mock_file.create_directory.assert_called()

        # プロジェクトルートが見つからない場合
        self.mock_file.detect_project_root.return_value = None
        with self.assertRaises(ValueError):
            self.command.execute(args)


class TestAddCommand(unittest.TestCase):
    """追加コマンドのテストクラス"""

    def setUp(self):
        """テストの前準備"""
        self.mock_file = MagicMock()
        self.mock_template = MagicMock()
        self.command = AddCommand(
            file_manager=self.mock_file, template_manager=self.mock_template
        )

    def test_execute(self):
        """コマンド実行のテスト"""
        # 正常な実行
        self.mock_file.detect_project_root.return_value = "/test/project"
        args = {"rule_name": "test-rule", "template": "basic"}
        result = self.command.execute(args)
        self.assertTrue(result)
        self.mock_template.expand_template.assert_called()

        # プロジェクトルートが見つからない場合
        self.mock_file.detect_project_root.return_value = None
        with self.assertRaises(ValueError):
            self.command.execute(args)


class TestListCommand(unittest.TestCase):
    """一覧コマンドのテストクラス"""

    def setUp(self):
        """テストの前準備"""
        self.mock_file = MagicMock()
        self.command = ListCommand(file_manager=self.mock_file)

    def test_execute(self):
        """コマンド実行のテスト"""
        # 正常な実行
        self.mock_file.detect_project_root.return_value = "/test/project"
        self.mock_file.listdir.return_value = ["rule1.yaml", "rule2.yaml"]
        result = self.command.execute({})
        self.assertTrue(result)
        self.mock_file.detect_project_root.assert_called_once()
        self.mock_file.listdir.assert_called_once()

        # プロジェクトルートが見つからない場合
        self.mock_file.detect_project_root.return_value = None
        with self.assertRaises(ValueError):
            self.command.execute({})


if __name__ == "__main__":
    unittest.main()
