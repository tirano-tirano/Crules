"""
CLIインターフェースのテスト

このモジュールでは、CLIインターフェースのテストを実装します。
"""

import os
import sys
import unittest
from unittest import TestCase
from unittest.mock import MagicMock, call, patch

from src.cli.interface import CLI, CommandInterface, main


class TestCommandInterface(TestCase):
    """CommandInterfaceクラスのテスト"""

    def setUp(self):
        """テストの準備"""
        self.interface = CommandInterface()
        self.mock_command = MagicMock()

    def test_register_command(self):
        """register_commandメソッドのテスト"""
        self.interface.register_command("test", self.mock_command)
        self.assertEqual(self.interface.commands["test"], self.mock_command)

    def test_execute_command(self):
        """execute_commandメソッドのテスト"""
        self.mock_command.execute.return_value = True
        self.interface.register_command("test", self.mock_command)
        result = self.interface.execute_command("test", {"arg": "value"})
        self.assertTrue(result)
        self.mock_command.execute.assert_called_once_with({"arg": "value"})

    def test_execute_command_with_error(self):
        """execute_commandメソッドのエラーケーステスト"""
        self.mock_command.execute.side_effect = Exception("Test error")
        self.interface.register_command("test", self.mock_command)
        result = self.interface.execute_command("test", {})
        self.assertFalse(result)

    def test_get_command(self):
        """get_commandメソッドのテスト"""
        self.interface.register_command("test", self.mock_command)
        command = self.interface.get_command("test")
        self.assertEqual(command, self.mock_command)

    def test_get_help(self):
        """get_helpメソッドのテスト"""
        self.interface.register_command("test", self.mock_command)
        help_text = self.interface.get_help("test")
        self.assertEqual(help_text, "Help for command 'test'")

    def test_list_commands(self):
        """list_commandsメソッドのテスト"""
        self.interface.register_command("test1", self.mock_command)
        self.interface.register_command("test2", self.mock_command)
        commands = self.interface.list_commands()
        self.assertEqual(set(commands), {"test1", "test2"})


class TestCLI(TestCase):
    """CLIクラスのテスト"""

    def setUp(self):
        """テストの準備"""
        self.cli = CLI()
        self.mock_file_manager = MagicMock()
        self.mock_config_manager = MagicMock()
        self.mock_template_manager = MagicMock()

        # モックの設定
        self.cli.file_manager = self.mock_file_manager
        self.cli.config_manager = self.mock_config_manager
        self.cli.template_manager = self.mock_template_manager

        # テンプレートディレクトリの構造をモック
        self.template_dir = MagicMock()
        self.template_dir.rules = ["rule1.md", "rule2.md"]
        self.template_dir.notes = ["note1.md", "note2.md"]
        self.mock_template_manager.template_dir = self.template_dir

        # プロジェクトルートの設定
        self.project_root = "/test/project"
        self.mock_file_manager.detect_project_root.return_value = self.project_root

    def test_run_command(self):
        """run_commandメソッドのテスト"""
        # initコマンドのテスト
        self.cli._init_command = MagicMock()
        self.cli.run_command("init", template_name="test", force=True)
        self.cli._init_command.assert_called_once_with(template_name="test", force=True)

        # deployコマンドのテスト
        self.cli._deploy_command = MagicMock()
        self.cli.run_command("deploy", force=True)
        self.cli._deploy_command.assert_called_once_with(force=True)

    def test_run_command_error(self):
        """run_commandメソッドのエラーケーステスト"""
        with self.assertRaises(ValueError):
            self.cli.run_command("unknown")

    @patch("os.path.join")
    @patch("os.listdir")
    def test_init_command(self, mock_listdir, mock_join):
        """_init_commandメソッドのテスト"""
        # パスの結合をモック
        template_path = os.path.join(
            self.project_root, ".crules", "templates", "test_template"
        )
        rules_path = os.path.join(self.project_root, ".cursor", "rules")
        notes_path = os.path.join(self.project_root, ".notes")
        template_rules_path = os.path.join(template_path, "rules")
        template_notes_path = os.path.join(template_path, "notes")
        src_rule_path = os.path.join(template_rules_path, "rule1.md")
        dst_rule_path = os.path.join(rules_path, "rule1.md")
        src_note_path = os.path.join(template_notes_path, "note1.md")
        dst_note_path = os.path.join(notes_path, "note1.md")
        mock_join.side_effect = [
            template_path,
            rules_path,
            template_rules_path,
            src_rule_path,
            dst_rule_path,
            notes_path,
            template_notes_path,
            src_note_path,
            dst_note_path,
        ]

        # ファイル一覧のモック
        mock_listdir.side_effect = [["rule1.md"], ["note1.md"]]

        # テンプレートマネージャーのモック
        with patch("src.cli.interface.TemplateManager") as mock_template_manager_class:
            mock_template_manager = MagicMock()
            mock_template_manager_class.return_value = mock_template_manager

            # コマンド実行
            self.cli._init_command("test_template", force=True)

            # 検証
            self.mock_file_manager.detect_project_root.assert_has_calls(
                [call(), call()]
            )
            mock_template_manager_class.assert_called_once_with(template_path)
            self.assertEqual(self.cli.template_manager, mock_template_manager)

    @patch("os.path.join")
    @patch("os.listdir")
    def test_deploy_command(self, mock_listdir, mock_join):
        """_deploy_commandメソッドのテスト"""
        # 設定のモック
        self.mock_config_manager.load_config.return_value = {
            "template_name": "test_template"
        }

        # パスの結合をモック
        template_path = os.path.join(
            self.project_root, ".crules", "templates", "test_template"
        )
        rules_path = os.path.join(self.project_root, ".cursor", "rules")
        notes_path = os.path.join(self.project_root, ".notes")
        template_rules_path = os.path.join(template_path, "rules")
        template_notes_path = os.path.join(template_path, "notes")
        src_rule_path = os.path.join(template_rules_path, "rule1.md")
        dst_rule_path = os.path.join(rules_path, "rule1.md")
        src_note_path = os.path.join(template_notes_path, "note1.md")
        dst_note_path = os.path.join(notes_path, "note1.md")
        mock_join.side_effect = [
            template_path,
            rules_path,
            template_rules_path,
            src_rule_path,
            dst_rule_path,
            notes_path,
            template_notes_path,
            src_note_path,
            dst_note_path,
        ]

        # ファイル一覧のモック
        mock_listdir.side_effect = [["rule1.md"], ["note1.md"]]

        # テンプレートマネージャーのモック
        with patch("src.cli.interface.TemplateManager") as mock_template_manager_class:
            mock_template_manager = MagicMock()
            mock_template_manager_class.return_value = mock_template_manager

            # コマンド実行
            self.cli._deploy_command(force=True)

            # 検証
            self.mock_file_manager.detect_project_root.assert_has_calls(
                [call(), call()]
            )
            self.mock_config_manager.load_config.assert_called_once()
            mock_template_manager_class.assert_called_once_with(template_path)
            self.assertEqual(self.cli.template_manager, mock_template_manager)

    @patch("os.path.join")
    @patch("os.listdir")
    def test_expand_templates(self, mock_listdir, mock_join):
        """_expand_templatesメソッドのテスト"""
        # パスの結合をモック
        rules_path = os.path.join(self.project_root, ".cursor", "rules")
        notes_path = os.path.join(self.project_root, ".notes")
        template_rules_path = os.path.join(self.template_dir, "rules")
        template_notes_path = os.path.join(self.template_dir, "notes")
        src_rule_path = os.path.join(template_rules_path, "rule1.md")
        dst_rule_path = os.path.join(rules_path, "rule1.md")
        src_note_path = os.path.join(template_notes_path, "note1.md")
        dst_note_path = os.path.join(notes_path, "note1.md")
        mock_join.side_effect = [
            rules_path,
            template_rules_path,
            src_rule_path,
            dst_rule_path,
            notes_path,
            template_notes_path,
            src_note_path,
            dst_note_path,
        ]

        # ファイル一覧のモック
        mock_listdir.side_effect = [["rule1.md"], ["note1.md"]]

        # コマンド実行
        self.cli._expand_templates("test_template", force=True)

        # 検証
        self.mock_file_manager.detect_project_root.assert_called_once()
        self.mock_file_manager.create_directory.assert_any_call(rules_path)
        self.mock_file_manager.create_directory.assert_any_call(notes_path)


class TestMain(TestCase):
    """main関数のテスト"""

    def setUp(self):
        """テストの準備"""
        self.original_argv = sys.argv

    def tearDown(self):
        """テストの後処理"""
        sys.argv = self.original_argv

    def test_main_success(self):
        """main関数の成功ケーステスト"""
        sys.argv = ["crules", "init", "--template", "test"]
        with patch("src.cli.interface.CLI") as mock_cli_class:
            mock_cli = MagicMock()
            mock_cli_class.return_value = mock_cli
            result = main()
            self.assertEqual(result, 0)
            mock_cli.run_command.assert_called_once_with("init", "--template", "test")

    def test_main_error(self):
        """main関数のエラーケーステスト"""
        sys.argv = ["crules", "init", "--template", "test"]
        with patch("src.cli.interface.CLI") as mock_cli_class:
            mock_cli = MagicMock()
            mock_cli_class.return_value = mock_cli
            mock_cli.run_command.side_effect = Exception("Test error")
            result = main()
            self.assertEqual(result, 1)

    def test_main_no_args(self):
        """main関数の引数なしケーステスト"""
        sys.argv = ["crules"]
        result = main()
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
