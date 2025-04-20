"""
テンプレート処理モジュールのテスト

このモジュールは、テンプレート処理機能のテストを提供します。
"""

import os
import tempfile
import unittest

from src.core.template import TemplateManager


class TestTemplateManager(unittest.TestCase):
    """TemplateManagerのテストクラス"""

    def setUp(self):
        """テストの準備"""
        self.temp_dir = tempfile.mkdtemp()
        self.template_dir = os.path.join(self.temp_dir, "templates")
        os.makedirs(self.template_dir)
        self.template_manager = TemplateManager(self.template_dir)

    def tearDown(self):
        """テストの後処理"""
        if os.path.exists(self.temp_dir):
            for root, dirs, files in os.walk(self.temp_dir, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(self.temp_dir)

    def test_load_template(self):
        """テンプレートを読み込むテスト"""
        template_name = "test_template.html"
        template_content = "Hello, {{name}}!"
        template_path = os.path.join(self.template_dir, template_name)
        with open(template_path, "w") as f:
            f.write(template_content)
        template = self.template_manager.load_template(template_name)
        self.assertIsNotNone(template)

    def test_process_template(self):
        """テンプレートを処理するテスト"""
        template_name = "test_template.html"
        template_content = "Hello, {{name}}!"
        template_path = os.path.join(self.template_dir, template_name)
        with open(template_path, "w") as f:
            f.write(template_content)
        context = {"name": "World"}
        result = self.template_manager.process_template(template_name, context)
        self.assertEqual(result, "Hello, World!")

    def test_expand_template(self):
        """テンプレートを展開するテスト"""
        template_name = "test_template.html"
        template_content = "Hello, {{name}}!"
        template_path = os.path.join(self.template_dir, template_name)
        with open(template_path, "w") as f:
            f.write(template_content)
        output_path = os.path.join(self.temp_dir, "output.html")
        context = {"name": "World"}
        self.template_manager.expand_template(template_name, output_path, context)
        self.assertTrue(os.path.exists(output_path))
        with open(output_path, "r") as f:
            content = f.read()
        self.assertEqual(content, "Hello, World!")

    def test_validate_template(self):
        """テンプレートを検証するテスト"""
        template_name = "test_template.html"
        template_content = "Hello, {{name}}!"
        template_path = os.path.join(self.template_dir, template_name)
        with open(template_path, "w") as f:
            f.write(template_content)
        result = self.template_manager.validate_template(template_name)
        self.assertTrue(result)

    def test_validate_template_not_found(self):
        """テンプレートが見つからない場合のテスト"""
        result = self.template_manager.validate_template("non_existent.html")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main() 