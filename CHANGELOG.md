# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2024-04-20

### Added

- 基本的なルール管理ツールの実装
- CLI インターフェースの実装
- テンプレート管理機能の実装
- ファイル操作ユーティリティの実装
- 設定管理機能の実装

### Changed

- GitHub Actions ワークフローの更新：Python 3.1 ジョブの削除と flake8 設定の更新

### Fixed

- CLI テストの修正
- 依存関係の競合の解決

### Removed

- Codecov の統合を削除し、ローカルでのカバレッジレポート確認に変更

## [0.1.0] - 2024-04-20

### Added

- 基本機能の実装
  - プロジェクトルールの管理
  - テンプレートの展開と管理
  - 設定ファイルの処理
- 主要コンポーネントの実装
  - CLI インターフェース
  - ファイル操作
  - 設定管理
  - テンプレート管理
- テストと CI/CD プロセスの実装
  - ユニットテスト
  - GitHub Actions による自動化
  - コードカバレッジの追跡
- ドキュメントの整備
  - README
  - CONTRIBUTING
  - CHANGELOG

[Unreleased]: https://github.com/tirano-tirano/crules/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/tirano-tirano/crules/compare/v0.1.0...v0.2.0
[0.1.0]: https://github.com/tirano-tirano/crules/releases/tag/v0.1.0
