# Crules

プロジェクトのルール管理を効率的に行うためのツールです。

## 機能

- プロジェクトの初期化
- ルールの管理（追加、削除、一覧表示）
- テンプレートの管理
- 設定の管理

## 必要条件

- Python 3.9 以上

## インストール

```bash
pip install crules
```

## 使用方法

### プロジェクトの初期化

```bash
crules init
```

### ルールの追加

```bash
crules add rule <rule_name>
```

### ルールの一覧表示

```bash
crules list rules
```

### テンプレートの追加

```bash
crules add template <template_name>
```

### テンプレートの一覧表示

```bash
crules list templates
```

## 開発

### 環境構築

```bash
# リポジトリのクローン
git clone https://github.com/yourusername/crules.git
cd crules

# 開発用依存関係のインストール
pip install -e ".[dev]"
```

### テストの実行

```bash
python -m pytest
```

### カバレッジレポートの生成

```bash
pytest --cov=src tests/
```

## ライセンス

MIT License
