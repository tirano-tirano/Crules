# Homebrew Tap for Crules

[![GitHub Actions](https://github.com/tirano-tirano/homebrew-crules/workflows/CI/badge.svg)](https://github.com/tirano-tirano/homebrew-crules/actions)
[![License](https://img.shields.io/github/license/tirano-tirano/crules)](https://github.com/tirano-tirano/crules/blob/main/LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)

このリポジトリは、[Crules](https://github.com/tirano-tirano/crules)の Homebrew タップです。

## インストール方法

```bash
# タップの追加
brew tap tirano-tirano/crules

# パッケージのインストール
brew install crules
```

## 更新方法

```bash
brew update
brew upgrade crules
```

## アンインストール方法

```bash
brew uninstall crules
brew untap tirano-tirano/crules
```

## 必要条件

- Python 3.9 以上
- macOS 10.15 以上

### Python 依存パッケージ

- jinja2 >= 3.0.0
- pyyaml >= 6.0.0
- click >= 8.0.0
- rich >= 13.0.0

これらの依存パッケージは、Homebrew によるインストール時に自動的にインストールされます。

## 機能

Crules は、プロジェクトのルールとノートを効率的に管理するための CLI ツールです。

### 主な機能

1. プロジェクトルールとノートの管理

   - テンプレートベースのルール作成
   - カスタマイズ可能なノート形式
   - バージョン管理との統合

2. テンプレート管理

   - プロジェクト固有のテンプレート作成
   - テンプレートの継承とカスタマイズ
   - 複数テンプレートの同時使用

3. ファイル操作

   - インテリジェントなファイル配置
   - 競合の自動検出と解決
   - バックアップと復元機能

4. プロジェクト管理
   - プロジェクトルートの自動検出
   - 設定ファイルによる柔軟なカスタマイズ
   - 複数プロジェクトの同時管理

## 使用例

### プロジェクトの初期化

```bash
# プロジェクトの初期化
crules init

# カスタムテンプレートを使用した初期化
crules init --template custom-template
```

### ルールの管理

```bash
# ルール一覧の表示
crules list

# 特定のルールの詳細表示
crules show rule-name

# ルールの追加
crules add rule-name

# ルールの更新
crules update rule-name
```

### テンプレートの操作

```bash
# テンプレート一覧の表示
crules template list

# テンプレートの追加
crules template add template-name

# テンプレートの展開
crules deploy template-name
```

## 設定ファイル

Crules は `.crules.yaml` または `.crules.json` を設定ファイルとして使用します。

```yaml
# .crules.yaml の例
project:
  name: "my-project"
  version: "1.0.0"

templates:
  - name: "default"
    path: "./templates/default"
  - name: "custom"
    path: "./templates/custom"

rules:
  ignore_patterns:
    - "*.log"
    - "node_modules/"
  backup:
    enabled: true
    path: "./.crules-backup"
```

## トラブルシューティング

### 1. インストールの問題

インストールに失敗する場合：

```bash
# Homebrewの診断
brew doctor

# キャッシュのクリーンアップ
brew cleanup

# 詳細なログ出力でインストール
brew install --verbose crules
```

### 2. 実行時エラー

よくある問題と解決方法：

a. プロジェクトルートが見つからない

```bash
# プロジェクトディレクトリで実行されているか確認
pwd

# 手動でプロジェクトルートを指定
crules --root /path/to/project <command>
```

b. テンプレートエラー

```bash
# テンプレートの検証
crules template verify template-name

# テンプレートの再インストール
crules template reinstall template-name
```

### 3. 更新の問題

更新に失敗する場合：

```bash
# キャッシュのクリーンアップ
brew cleanup

# Homebrewの更新
brew update

# パッケージの更新
brew upgrade crules
```

## 開発者向け情報

このタップは自動的に更新されます。新しいリリースが公開されると、GitHub Actions によってフォーミュラが自動的に更新されます。

### 手動更新手順

1. SHA256 の更新

   ```bash
   curl -L "https://github.com/tirano-tirano/crules/archive/refs/tags/v{version}.tar.gz" | shasum -a 256
   ```

2. 依存関係の更新
   - `requirements.txt`の変更を確認
   - 必要に応じて Formula の`resource`ブロックを更新

## コントリビューション

プロジェクトへの貢献を歓迎します！以下の手順で貢献できます：

1. このリポジトリをフォークする
2. 新しいブランチを作成する (`git checkout -b feature/amazing-feature`)
3. 変更をコミットする (`git commit -m 'Add some amazing feature'`)
4. ブランチにプッシュする (`git push origin feature/amazing-feature`)
5. プルリクエストを作成する

詳細は[コントリビューションガイドライン](CONTRIBUTING.md)を参照してください。

## 変更履歴

最新の変更履歴は[CHANGELOG.md](CHANGELOG.md)を参照してください。

## ライセンス

このプロジェクトは MIT ライセンスの下で公開されています。詳細は[LICENSE](LICENSE)ファイルを参照してください。
