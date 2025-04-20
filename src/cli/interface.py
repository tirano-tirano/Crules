"""
コマンドインターフェースモジュール

このモジュールは、コマンドラインインターフェースを提供します。
"""

import os
import sys
from typing import Any, Dict, List

from ..core.config import ConfigManager
from ..core.file import FileManager
from ..core.template import TemplateManager


class CommandInterface:
    """コマンドインターフェースクラス"""

    def __init__(self):
        """初期化"""
        self.commands = {}

    def register_command(self, name: str, command: Any) -> None:
        """
        コマンドを登録する

        Args:
            name: コマンド名
            command: コマンドオブジェクト
        """
        self.commands[name] = command

    def execute_command(self, name: str, args: Dict[str, Any]) -> bool:
        """
        コマンドを実行する

        Args:
            name: コマンド名
            args: コマンドの引数

        Returns:
            bool: コマンドの実行結果
        """
        try:
            if name not in self.commands:
                return False
            return self.commands[name].execute(args)
        except Exception:
            return False

    def get_command(self, name: str) -> Any:
        """
        コマンドを取得する

        Args:
            name: コマンド名

        Returns:
            Any: コマンドオブジェクト
        """
        return self.commands[name]

    def get_help(self, name: str) -> str:
        """
        コマンドのヘルプを取得する

        Args:
            name: コマンド名

        Returns:
            str: ヘルプテキスト
        """
        if name not in self.commands:
            return "Command not found"
        return f"Help for command '{name}'"

    def list_commands(self) -> List[str]:
        """
        コマンド一覧を取得する

        Returns:
            List[str]: コマンド名のリスト
        """
        return list(self.commands.keys())

class CLI:
    """CLIクラス"""

    def __init__(self):
        """初期化"""
        self.config_manager = ConfigManager()
        self.file_manager = FileManager()
        self.template_manager = None

    def run_command(self, command: str, **kwargs: Any) -> None:
        """
        コマンドを実行する

        Args:
            command: コマンド名
            **kwargs: コマンドの引数
        """
        if command == "init":
            self._init_command(**kwargs)
        elif command == "deploy":
            self._deploy_command(**kwargs)
        else:
            raise ValueError(f"Unknown command: {command}")

    def _init_command(self, template_name: str, force: bool = False) -> None:
        """
        プロジェクト初期化コマンド

        Args:
            template_name: テンプレート名
            force: 強制上書きフラグ
        """
        # プロジェクトルートを検出
        project_root = self.file_manager.detect_project_root()
        if not project_root:
            raise ValueError("Project root not found")

        # テンプレートディレクトリを設定
        template_dir = os.path.join(project_root, ".crules", "templates", template_name)
        self.template_manager = TemplateManager(template_dir)

        # テンプレートを展開
        self._expand_templates(template_name, force)

    def _deploy_command(self, force: bool = False) -> None:
        """
        テンプレート展開コマンド

        Args:
            force: 強制上書きフラグ
        """
        # プロジェクトルートを検出
        project_root = self.file_manager.detect_project_root()
        if not project_root:
            raise ValueError("Project root not found")

        # 設定を読み込み
        config = self.config_manager.load_config()
        template_name = config.get("template_name")
        if not template_name:
            raise ValueError("Template name not found in config")

        # テンプレートディレクトリを設定
        template_dir = os.path.join(project_root, ".crules", "templates", template_name)
        self.template_manager = TemplateManager(template_dir)

        # テンプレートを展開
        self._expand_templates(template_name, force)

    def _expand_templates(self, template_name: str, force: bool = False) -> None:
        """
        テンプレートを展開する

        Args:
            template_name: テンプレート名
            force: 強制上書きフラグ
        """
        # プロジェクトルートを検出
        project_root = self.file_manager.detect_project_root()
        if not project_root:
            raise ValueError("Project root not found")

        # ルールファイルを展開
        rules_dir = os.path.join(project_root, ".cursor", "rules")
        self.file_manager.create_directory(rules_dir)
        for file in os.listdir(os.path.join(self.template_manager.template_dir, "rules")):
            if file.endswith(".md"):
                src_path = os.path.join(self.template_manager.template_dir, "rules", file)
                dst_path = os.path.join(rules_dir, file.replace(".md", ".mdc"))
                if not os.path.exists(dst_path) or force:
                    self.file_manager.copy_file(src_path, dst_path)

        # ノートファイルを展開
        notes_dir = os.path.join(project_root, ".notes")
        self.file_manager.create_directory(notes_dir)
        for file in os.listdir(os.path.join(self.template_manager.template_dir, "notes")):
            if file.endswith(".md"):
                src_path = os.path.join(self.template_manager.template_dir, "notes", file)
                dst_path = os.path.join(notes_dir, file)
                if not os.path.exists(dst_path) or force:
                    self.file_manager.copy_file(src_path, dst_path)

def main():
    """
    メイン関数

    Returns:
        int: 終了コード
    """
    cli = CLI()
    if len(sys.argv) < 2:
        print("Usage: crules <command> [options]")
        return 1
    
    command = sys.argv[1]
    args = sys.argv[2:]
    
    try:
        cli.run_command(command, *args)
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 