"""
検証モジュール

このモジュールは、パス、名前、設定などの検証機能を提供します。
"""

import os
import re
from typing import Any, Dict


def validate_path(path: str) -> bool:
    """
    パスを検証する

    Args:
        path: 検証するパス

    Returns:
        bool: 検証結果
    """
    if not path or path.isspace():
        return False
    try:
        normalized = os.path.normpath(path)
        return bool(normalized) and normalized != "/" and normalized != "//" and "\0" not in normalized
    except Exception:
        return False


def validate_name(name: str) -> bool:
    """
    名前を検証する

    Args:
        name: 検証する名前

    Returns:
        bool: 検証結果
    """
    if not name or name.isspace():
        return False
    pattern = r"^[a-zA-Z0-9_-]+$"
    return bool(re.match(pattern, name))


def validate_config(config: Dict[str, Any]) -> bool:
    """
    設定を検証する

    Args:
        config: 検証する設定

    Returns:
        bool: 検証結果
    """
    if not config or not isinstance(config, dict):
        return False
    return "template_name" in config 