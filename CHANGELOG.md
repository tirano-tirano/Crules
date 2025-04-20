# Changelog

このプロジェクトの全ての重要な変更はこのファイルに記録されます。

フォーマットは[Keep a Changelog](https://keepachangelog.com/ja/1.0.0/)に基づいており、
バージョニングは[Semantic Versioning](https://semver.org/spec/v2.0.0.html)に従います。

## [Unreleased]

### Added

- ルール管理のための基本ツール
- CLI インターフェース
- テンプレート管理機能
- ファイル操作ユーティリティ
- 設定管理機能

### Changed

- GitHub Actions ワークフローの改善
  - Python 3.1 ジョブの削除
  - flake8 設定の更新
  - カバレッジレポート生成の改善

### Fixed

- CLI テストの修正
- 依存関係の競合解決

### Removed

- Codecov 統合の削除（ローカルカバレッジレポートチェックに移行）

## [0.1.0] - 2024-04-20

### 初期リリース

- 基本機能の実装
  - プロジェクトルールの管理
  - テンプレートベースのルール展開
  - コマンドラインインターフェース
- 主要コンポーネントの実装
  - FileManager: ファイル操作
  - ConfigManager: 設定管理
  - TemplateManager: テンプレート管理
  - CLI: コマンドライン処理
- テストと CI/CD
  - ユニットテスト
  - GitHub Actions による自動化
  - カバレッジレポート
- ドキュメント
  - README
  - API 仕様
  - 使用方法ガイド

[Unreleased]: https://github.com/tirano-tirano/crules/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/tirano-tirano/crules/releases/tag/v0.1.0
