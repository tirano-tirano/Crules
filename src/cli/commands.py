"""
コマンド実装モジュール

このモジュールは、コマンドの実装を提供します。
"""

import os
from typing import Any, Dict, Optional, cast

from ..core.config import ConfigManager
from ..core.file import FileManager
from ..core.template import TemplateManager


class BaseCommand:
    """基底コマンドクラス"""

    def __init__(
        self,
        config_manager: Optional[ConfigManager] = None,
        file_manager: Optional[FileManager] = None,
        template_manager: Optional[TemplateManager] = None,
    ):
        """
        初期化

        Args:
            config_manager: 設定マネージャー
            file_manager: ファイルマネージャー
            template_manager: テンプレートマネージャー
        """
        self.config_manager = config_manager or ConfigManager()
        self.file_manager = file_manager or FileManager()
        self.template_manager = template_manager

    def execute(self, args: Dict[str, Any]) -> bool:
        """
        コマンドを実行する

        Args:
            args: コマンドの引数

        Returns:
            bool: コマンドの実行結果
        """
        raise NotImplementedError()


class InitCommand(BaseCommand):
    """初期化コマンドクラス"""

    def execute(self, args: Dict[str, Any]) -> bool:
        """
        コマンドを実行する

        Args:
            args: コマンドの引数
                - project_name: プロジェクト名
                - force: 強制上書きフラグ

        Returns:
            bool: コマンドの実行結果
        """
        project_name = cast(str, args.get("project_name"))
        force = bool(args.get("force", False))

        # プロジェクトルートを検出
        project_root = self.file_manager.detect_project_root()
        if not project_root:
            raise ValueError("Project root not found")

        # テンプレートディレクトリを設定
        template_dir = os.path.join(project_root, ".crules", "templates", project_name)
        self.template_manager = self.template_manager or TemplateManager(template_dir)

        # テンプレートを展開
        rules_dir = os.path.join(project_root, ".cursor", "rules")
        self.file_manager.create_directory(rules_dir)
        template_manager = cast(TemplateManager, self.template_manager)
        for file in os.listdir(os.path.join(template_manager.template_dir, "rules")):
            src = os.path.join(template_manager.template_dir, "rules", file)
            dst = os.path.join(rules_dir, file)
            template_manager.expand_template(src, dst, {"force": force})
        return True


class AddCommand(BaseCommand):
    """追加コマンドクラス"""

    def execute(self, args: Dict[str, Any]) -> bool:
        """
        コマンドを実行する

        Args:
            args: コマンドの引数
                - rule_name: ルール名
                - template: テンプレート名
                - force: 強制上書きフラグ

        Returns:
            bool: コマンドの実行結果
        """
        rule_name = cast(str, args.get("rule_name"))
        template = cast(str, args.get("template"))
        force = bool(args.get("force", False))

        # プロジェクトルートを検出
        project_root = self.file_manager.detect_project_root()
        if not project_root:
            raise ValueError("Project root not found")

        # テンプレートを展開
        rules_dir = os.path.join(project_root, ".cursor", "rules")
        self.file_manager.create_directory(rules_dir)
        if not self.template_manager:
            raise ValueError("Template manager is not initialized")
        src = os.path.join(
            project_root, ".crules", "templates", template, "rules", f"{rule_name}.yaml"
        )
        dst = os.path.join(rules_dir, f"{rule_name}.yaml")
        self.template_manager.expand_template(src, dst, {"force": force})
        return True


class ListCommand(BaseCommand):
    """一覧コマンドクラス"""

    def execute(self, args: Dict[str, Any]) -> bool:
        """
        コマンドを実行する

        Args:
            args: コマンドの引数

        Returns:
            bool: コマンドの実行結果
        """
        # プロジェクトルートを検出
        project_root = self.file_manager.detect_project_root()
        if not project_root:
            raise ValueError("Project root not found")

        # ルールファイルを一覧表示
        rules_dir = os.path.join(project_root, ".cursor", "rules")
        files = self.file_manager.listdir(rules_dir)
        for file in files:
            if file.endswith(".yaml"):
                print(f"- {file[:-5]}")
        return True
