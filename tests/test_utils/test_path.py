"""
パス操作モジュールのテスト

このモジュールは、パス操作機能のテストを提供します。
"""

import os
import unittest
from typing import Optional

from src.utils.path import normalize_path, resolve_path, is_subpath


class TestPathUtils(unittest.TestCase):
    """パス操作ユーティリティのテストクラス"""

    def test_normalize_path(self):
        """パスを正規化するテスト"""
        # 相対パスの正規化
        self.assertEqual(normalize_path("a/b/../c"), "a/c")
        self.assertEqual(normalize_path("./a/b/./c"), "a/b/c")
        
        # 絶対パスの正規化
        abs_path = os.path.abspath("a/b/c")
        self.assertEqual(normalize_path(abs_path), abs_path)

    def test_resolve_path(self):
        """パスを解決するテスト"""
        # 基準パスなしの場合（カレントディレクトリを使用）
        rel_path = "a/b/c"
        expected = os.path.join(os.getcwd(), rel_path)
        self.assertEqual(resolve_path(rel_path), expected)
        
        # 基準パスありの場合
        base_path = "/base/path"
        expected = os.path.join(base_path, rel_path)
        self.assertEqual(resolve_path(rel_path, base_path), expected)

    def test_is_subpath(self):
        """サブパス判定のテスト"""
        # 相対パスの場合
        self.assertTrue(is_subpath("a/b/c", "a/b"))
        self.assertFalse(is_subpath("a/b/c", "a/d"))
        
        # 絶対パスの場合
        base = os.path.abspath("a/b")
        sub = os.path.abspath("a/b/c")
        other = os.path.abspath("a/d")
        self.assertTrue(is_subpath(sub, base))
        self.assertFalse(is_subpath(other, base))
        
        # 同じパスの場合
        self.assertTrue(is_subpath("a/b", "a/b"))
        
        # 親パスの場合
        self.assertFalse(is_subpath("a/b", "a/b/c"))


if __name__ == "__main__":
    unittest.main() 