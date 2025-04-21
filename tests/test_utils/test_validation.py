"""
バリデーション機能のテスト

このモジュールでは、バリデーション機能のテストを実装します。
"""

import unittest

from src.utils.validation import validate_config, validate_name, validate_path


class TestValidation(unittest.TestCase):
    """バリデーション機能のテストクラス"""

    def test_validate_path(self):
        """パスのバリデーションテスト"""
        # 正常なパス
        self.assertTrue(validate_path("/path/to/file"))
        self.assertTrue(validate_path("path/to/file"))
        self.assertTrue(validate_path("./path/to/file"))
        self.assertTrue(validate_path("../path/to/file"))

        # 異常なパス
        self.assertFalse(validate_path(""))
        self.assertFalse(validate_path(" "))
        self.assertFalse(validate_path("/"))
        self.assertFalse(validate_path("//"))

    def test_validate_name(self):
        """名前のバリデーションテスト"""
        # 正常な名前
        self.assertTrue(validate_name("valid-name"))
        self.assertTrue(validate_name("valid_name"))
        self.assertTrue(validate_name("validName"))
        self.assertTrue(validate_name("valid123"))

        # 異常な名前
        self.assertFalse(validate_name(""))
        self.assertFalse(validate_name(" "))
        self.assertFalse(validate_name("invalid/name"))
        self.assertFalse(validate_name("invalid\\name"))
        self.assertFalse(validate_name("invalid:name"))

    def test_validate_config(self):
        """設定のバリデーションテスト"""
        # 正常な設定
        valid_config = {
            "template_name": "test-template",
            "description": "Test template",
            "version": "1.0.0",
        }
        self.assertTrue(validate_config(valid_config))

        # 異常な設定
        invalid_config = {"description": "Test template", "version": "1.0.0"}
        self.assertFalse(validate_config(invalid_config))
        self.assertFalse(validate_config({}))
        self.assertFalse(validate_config(None))


if __name__ == "__main__":
    unittest.main()
