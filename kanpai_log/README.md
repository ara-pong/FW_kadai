Kanpai Log - 最終課題 Django サンプル

このフォルダは課題用に作成した Django Web アプリです。

## 概要
晩酌の支出を記録する Web アプリです。

主な実装内容:
- Django の Model / View / Template を使用した MVC 構造
- `Entry` モデルで日付、店名・銘柄、酒の種類、金額、メモを管理
- 一覧、詳細、登録、編集、削除の CRUD 機能
- 月単位 / 日単位の絞り込み
- つまみ専用の一覧ページと専用登録ページ
- 認証は不要（課題要件に合わせた簡易構成）
- Bootstrap 5 を使ったレイアウト

## 目的
- 課題で求められる Django MVT の利用
- レイアウトが見やすく使いやすい UI
- 管理対象が明確な業務系アプリとしての実装

## 必要条件
- Python 3.11 以上
- Django 4.2 系

## セットアップ
1. このフォルダに移動します。

```powershell
Set-Location 'c:\Users\arapo\FlameWorkLesson\kadai\kanpai_log'
```

2. 仮想環境を作成して有効化します。

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. 依存パッケージをインストールします。

```powershell
python -m pip install -r requirements.txt
```

4. マイグレーションを適用します。

```powershell
python manage.py migrate
```

5. 開発サーバーを起動します。

```powershell
python manage.py runserver
```

## 実行確認
- 一覧ページ: `http://127.0.0.1:8000/`
- つまみ一覧: `http://127.0.0.1:8000/tsumami/`
- つまみ登録: `http://127.0.0.1:8000/entries/tsumami/create/`

## 使い方
- 一覧ページで支出記録を閲覧できます。
- 年のみ / 年＋月 / 年＋月＋日 で絞り込みができます。
- つまみ専用ページでは「つまみ」と記載された記録のみ表示します。
- つまみ登録ページでは `drink_type` を自動的に `other` として扱い、入力欄は表示しません。

## 提出内容
- プログラム一式: `kadai/kanpai_log` フォルダ内のファイル
- README: この `README.md`
- スクリーンショット: アプリの一覧画面、つまみ一覧画面、登録画面などの画面キャプチャ

## 備考
- データは `db.sqlite3` に保存されます。
- 管理画面を利用したい場合は `python manage.py createsuperuser` を実行し、`http://127.0.0.1:8000/admin/` にアクセスしてください。
