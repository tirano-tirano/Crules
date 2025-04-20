"""
パス操作モジュール

このモジュールは、パス操作に関する機能を提供します。
"""

import os
from typing import Optional


def normalize_path(path: str) -> str:
    """
    パスを正規化する

    Args:
        path: パス

    Returns:
        正規化されたパス
    """
    return os.path.normpath(path)


def resolve_path(path: str, base_path: Optional[str] = None) -> str:
    """
    パスを解決する

    Args:
        path: パス
        base_path: 基準パス

    Returns:
        解決されたパス
    """
    if base_path is None:
        base_path = os.getcwd()
    return os.path.join(base_path, path)


def is_subpath(path: str, base_path: str) -> bool:
    """
    パスが基準パスのサブパスかどうかを判定する

    Args:
        path: パス
        base_path: 基準パス

    Returns:
        サブパスかどうか
    """
    path = normalize_path(path)
    base_path = normalize_path(base_path)
    return path.startswith(base_path) 