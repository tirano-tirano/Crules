# コーディング規約

このドキュメントでは、Crules プロジェクトのコーディング規約について説明します。

## Python バージョン

- プロジェクトは Python 3.9 以上をサポートします
- CI/CD 環境では Python 3.9, 3.10, 3.11 でテストを実行します

## コードフォーマット

### Black

- 行の長さは 88 文字に制限します
- ターゲットバージョンは Python 3.9 です
- 設定は`pyproject.toml`ファイルで管理します

```toml
[tool.black]
line-length = 88
target-version = ['py39']
include = '\.pyi?$'
```

### isort

- Black と互換性のある設定を使用します
- 行の長さは 88 文字に制限します
- 設定は`pyproject.toml`ファイルで管理します

```toml
[tool.isort]
profile = "black"
line_length = 88
```

### flake8

- 行の長さは 88 文字に制限します（Black と一致）
- E203 エラーは無視します（Black と競合するため）
- 設定は`.flake8`ファイルで管理します

```
[flake8]
max-line-length = 88
extend-ignore = E203
# E203: whitespace before ':' is enforced by black
```

## 型アノテーション

- すべての関数とメソッドには型アノテーションを付与します
- 複雑な型は`typing`モジュールを使用します
- 型チェックには`mypy`を使用します

## ドキュメント

- すべての関数とメソッドには docstring を記述します
- docstring は Google スタイルを使用します
- 複雑なロジックにはコメントを追加します

## テスト

- すべての機能にはユニットテストを記述します
- テストカバレッジは 80%以上を維持します
- テストは`pytest`を使用して実行します

## エラー処理

- 適切な例外を発生させ、エラーメッセージを明確にします
- ユーザーに表示するエラーメッセージは日本語で記述します
- デバッグ用のログは英語で記述します

## コミットメッセージ

- コミットメッセージは以下の形式に従います：
  - `feat: 新機能の追加`
  - `fix: バグ修正`
  - `docs: ドキュメントの更新`
  - `style: コードスタイルの修正`
  - `refactor: リファクタリング`
  - `test: テストの追加・修正`
  - `chore: その他の変更`

## CI/CD

- すべてのプッシュとプルリクエストでテストを実行します
- コードフォーマットとリントチェックを実行します
- セキュリティチェックを実行します

## 依存関係

- 依存関係は`requirements.txt`と`requirements-dev.txt`で管理します
- 本番環境用の依存関係は`requirements.txt`に記述します
- 開発環境用の依存関係は`requirements-dev.txt`に記述します

## プロジェクト構造

- モジュールは機能ごとに分割します
- 各モジュールは単一責任の原則に従います
- インターフェースと実装を分離します

## 設定ファイル

- プロジェクトの設定は`pyproject.toml`で管理します
- ツール固有の設定は各ツールの設定ファイルで管理します
- 環境変数は`.env`ファイルで管理します（Git にコミットしない）
