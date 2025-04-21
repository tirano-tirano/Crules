"""
ファイル操作モジュールのテスト

このモジュールは、ファイル操作機能のテストを提供します。
"""

import os
import tempfile
import unittest

from src.core.file import FileManager


class TestFileManager(unittest.TestCase):
    """FileManagerのテストクラス"""

    def setUp(self):
        """テストの準備"""
        self.temp_dir = tempfile.mkdtemp()
        self.file_manager = FileManager()

    def tearDown(self):
        """テストの後処理"""
        if os.path.exists(self.temp_dir):
            for root, dirs, files in os.walk(self.temp_dir, topdown=False):
                for name in files:
                    os.remove(os.path.join(root, name))
                for name in dirs:
                    os.rmdir(os.path.join(root, name))
            os.rmdir(self.temp_dir)

    def test_read_file(self):
        """ファイルを読み込むテスト"""
        test_file = os.path.join(self.temp_dir, "test.txt")
        test_content = "test content"
        with open(test_file, "w") as f:
            f.write(test_content)
        content = self.file_manager.read_file(test_file)
        self.assertEqual(content, test_content)

    def test_write_file(self):
        """ファイルに書き込むテスト"""
        test_file = os.path.join(self.temp_dir, "test.txt")
        test_content = "test content"
        self.file_manager.write_file(test_file, test_content)
        self.assertTrue(os.path.exists(test_file))
        with open(test_file, "r") as f:
            content = f.read()
        self.assertEqual(content, test_content)

    def test_copy_file(self):
        """ファイルをコピーするテスト"""
        src_file = os.path.join(self.temp_dir, "src.txt")
        dst_file = os.path.join(self.temp_dir, "dst.txt")
        test_content = "test content"
        with open(src_file, "w") as f:
            f.write(test_content)
        self.file_manager.copy_file(src_file, dst_file)
        self.assertTrue(os.path.exists(dst_file))
        with open(dst_file, "r") as f:
            content = f.read()
        self.assertEqual(content, test_content)

    def test_create_directory(self):
        """ディレクトリを作成するテスト"""
        test_dir = os.path.join(self.temp_dir, "test_dir")
        self.file_manager.create_directory(test_dir)
        self.assertTrue(os.path.exists(test_dir))
        self.assertTrue(os.path.isdir(test_dir))

    def test_detect_project_root(self):
        """プロジェクトルートを検出するテスト"""
        # テスト用の.crulesディレクトリを作成
        crules_dir = os.path.join(self.temp_dir, ".crules")
        os.makedirs(crules_dir)
        project_root = self.file_manager.detect_project_root(self.temp_dir)
        self.assertEqual(project_root, self.temp_dir)

    def test_detect_project_root_not_found(self):
        """プロジェクトルートが見つからない場合のテスト"""
        project_root = self.file_manager.detect_project_root(self.temp_dir)
        self.assertIsNone(project_root)


if __name__ == "__main__":
    unittest.main()
