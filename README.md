# Nanodjango Tutorial Example

このリポジトリは、[nanodjango](https://github.com/radiac/nanodjango)のチュートリアルを実装したサンプルプロジェクトです。nanodjangoは、単一ファイルでDjangoアプリケーションを構築できる軽量なフレームワークです。

## 🚀 プロジェクト概要

このプロジェクトでは、シンプルなページビューカウンターアプリケーションを作成します。主な機能は以下の通りです：

- ページアクセス数をカウントして表示
- Django Adminでのデータ管理
- REST API エンドポイント
- データベースマイグレーション

## 📋 必要な環境

- Python 3.12以上
- pip (Pythonパッケージマネージャー)

## 🛠️ セットアップ手順

### 1. リポジトリのクローン

```bash
git clone https://github.com/kimihito-sandbox/nanodjango-example.git
cd nanodjango-example
```

### 2. 依存関係のインストール

```bash
pip install nanodjango
```

または、プロジェクトファイルから：

```bash
pip install -e .
```

### 3. アプリケーションの起動

```bash
python main.py start
```

初回起動時は、Django管理者アカウントの作成を求められます。適当なユーザー名とパスワードを設定してください。

## 📱 使用方法

### Webページへのアクセス

アプリケーションが起動したら、ブラウザで以下のURLにアクセスできます：

- **メインページ**: `http://localhost:8000/`
  - ページアクセス数を表示
  - アクセスするたびにカウントが増加

- **Django Admin**: `http://localhost:8000/admin/`
  - データベースの管理画面
  - CountLogモデルの確認・操作

### API エンドポイント

- **GET** `/add` - カウントを追加してJSON形式で現在の数を返す

```bash
curl http://localhost:8000/add
# レスポンス例: {"count": 5}
```

## 📄 コード解説

### main.py の構造

```python
from django.db import models
from nanodjango import Django

app = Django()

@app.admin
class CountLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)

@app.route("/")
def count(request):
    CountLog.objects.create()
    return f"<p>Number of requests: {CountLog.objects.count()}</p>"

@app.api.get("/add")
def count(request):
    CountLog.objects.create()
    return {"count": CountLog.objects.count()}

if __name__ == "__main__":
    app.run()
```

#### 主要コンポーネント:

1. **Djangoアプリの初期化**: `app = Django()`
2. **データモデル**: `CountLog` - アクセス時刻を記録
3. **Webルート**: `/` - HTML形式でカウント表示
4. **APIエンドポイント**: `/add` - JSON形式でカウント返却
5. **Admin登録**: `@app.admin` デコレータで管理画面に自動登録

## 🔧 プロジェクト構成

```
nanodjango-example/
├── main.py              # メインアプリケーションファイル
├── pyproject.toml       # プロジェクト設定
├── migrations/          # データベースマイグレーション
│   ├── __init__.py
│   └── 0001_initial.py
├── README.md           # このファイル
└── .python-version     # Python バージョン指定
```

## 🎯 Nanodjangoの特徴

### 従来のDjangoとの違い

1. **単一ファイル**: 複数のファイルに分散せず、1つのファイルで完結
2. **簡単な設定**: 複雑な設定ファイル不要
3. **自動Admin登録**: デコレータ一つで管理画面に登録
4. **組み込みAPI**: django-ninjaを使ったAPI機能が標準装備

### 使用例

```python
# 基本的なWebページ
@app.route("/hello")
def hello(request):
    return "<h1>Hello, World!</h1>"

# API エンドポイント
@app.api.post("/users")
def create_user(request, name: str):
    return {"message": f"User {name} created"}

# モデルの定義と管理画面登録
@app.admin
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
```

## 🚀 発展的な使用方法

### 追加機能の実装例

#### 1. より複雑なAPI

```python
@app.api.get("/stats")
def get_stats(request):
    total_count = CountLog.objects.count()
    today_count = CountLog.objects.filter(
        timestamp__date=timezone.now().date()
    ).count()
    return {
        "total": total_count,
        "today": today_count
    }
```

#### 2. テンプレートの使用

```python
@app.route("/detailed")
def detailed_view(request):
    logs = CountLog.objects.all().order_by('-timestamp')[:10]
    return render(request, 'detailed.html', {'logs': logs})
```

## 🐛 トラブルシューティング

### よくある問題と解決方法

1. **ImportError: No module named 'nanodjango'**
   ```bash
   pip install nanodjango
   ```

2. **ポートが既に使用されている**
   ```bash
   python main.py start 127.0.0.1:8001
   ```

3. **マイグレーションエラー**
   ```bash
   python main.py makemigrations
   python main.py migrate
   ```

4. **静的ファイルの警告**
   - `static/` ディレクトリを作成するか、設定で無効にする

## 📚 参考リンク

- [Nanodjango 公式ドキュメント](https://github.com/radiac/nanodjango)
- [Django 公式ドキュメント](https://docs.djangoproject.com/)
- [Django Ninja ドキュメント](https://django-ninja.rest-framework.com/)

## 📝 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 🤝 コントリビューション

改善提案やバグ報告は、GitHubのIssueまたはPull Requestでお願いします。