"""
テンプレート処理モジュール

このモジュールは、テンプレートの処理に関する機能を提供します。
"""

import os
from typing import Any, Dict

from jinja2 import Environment, FileSystemLoader, Template


class TemplateManager:
    """テンプレート処理クラス"""

    def __init__(self, template_dir: str):
        """
        初期化

        Args:
            template_dir: テンプレートディレクトリのパス
        """
        self.template_dir = template_dir
        self.env = Environment(
            loader=FileSystemLoader(template_dir),
            autoescape=True,
        )

    def load_template(self, template_name: str) -> Template:
        """
        テンプレートを読み込む

        Args:
            template_name: テンプレート名

        Returns:
            テンプレートオブジェクト
        """
        return self.env.get_template(template_name)

    def process_template(
        self, template_name: str, context: Dict[str, Any]
    ) -> str:
        """
        テンプレートを処理する

        Args:
            template_name: テンプレート名
            context: テンプレートのコンテキスト

        Returns:
            処理結果
        """
        template = self.load_template(template_name)
        return template.render(**context)

    def expand_template(
        self,
        template_name: str,
        output_path: str,
        context: Dict[str, Any],
    ) -> None:
        """
        テンプレートを展開する

        Args:
            template_name: テンプレート名
            output_path: 出力パス
            context: テンプレートのコンテキスト
        """
        result = self.process_template(template_name, context)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        with open(output_path, "w") as f:
            f.write(result)

    def validate_template(self, template_name: str) -> bool:
        """
        テンプレートを検証する

        Args:
            template_name: テンプレート名

        Returns:
            検証結果
        """
        try:
            self.load_template(template_name)
            return True
        except Exception:
            return False 