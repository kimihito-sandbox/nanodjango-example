# Examples - 追加機能の実装例

このディレクトリには、nanodjangoを使った様々な機能の実装例が含まれています。

## 1. 基本的なWebフォーム (basic_form.py)

```python
from django.db import models
from nanodjango import Django

app = Django()

@app.admin
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

@app.route("/contact", methods=["GET", "POST"])
def contact_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        
        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            return "<h2>お問い合わせありがとうございます！</h2>"
    
    return """
    <form method="post">
        <p>名前: <input type="text" name="name" required></p>
        <p>メール: <input type="email" name="email" required></p>
        <p>メッセージ: <textarea name="message" required></textarea></p>
        <p><button type="submit">送信</button></p>
    </form>
    """
```

## 2. REST API with Pydantic (api_example.py)

```python
from pydantic import BaseModel
from nanodjango import Django

app = Django()

class UserCreate(BaseModel):
    name: str
    email: str
    age: int

class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    age: int

@app.api.post("/users", response=UserResponse)
def create_user(request, user: UserCreate):
    # データベース保存処理
    return {"id": 1, "name": user.name, "email": user.email, "age": user.age}

@app.api.get("/users/{user_id}", response=UserResponse)
def get_user(request, user_id: int):
    return {"id": user_id, "name": "John", "email": "john@example.com", "age": 30}
```

## 3. テンプレートとCSS (template_example.py)

```python
from django.shortcuts import render
from nanodjango import Django

app = Django()

@app.route("/styled")
def styled_page(request):
    context = {
        'title': 'スタイリッシュページ',
        'items': ['項目1', '項目2', '項目3']
    }
    return render(request, 'styled.html', context)
```

対応するテンプレート (`templates/styled.html`):

```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        .item { padding: 10px; border: 1px solid #ddd; margin: 5px 0; }
    </style>
</head>
<body>
    <h1>{{ title }}</h1>
    <ul>
    {% for item in items %}
        <li class="item">{{ item }}</li>
    {% endfor %}
    </ul>
</body>
</html>
```

## 4. ファイルアップロード (upload_example.py)

```python
from django.core.files.storage import default_storage
from nanodjango import Django

app = Django()

@app.route("/upload", methods=["GET", "POST"])
def file_upload(request):
    if request.method == "POST" and request.FILES.get("file"):
        uploaded_file = request.FILES["file"]
        file_path = default_storage.save(uploaded_file.name, uploaded_file)
        return f"<p>ファイル '{uploaded_file.name}' がアップロードされました。</p>"
    
    return """
    <form method="post" enctype="multipart/form-data">
        <p>ファイル選択: <input type="file" name="file" required></p>
        <p><button type="submit">アップロード</button></p>
    </form>
    """
```

## 実行方法

各例は独立したファイルとして保存し、以下のように実行できます：

```bash
python basic_form.py start
python api_example.py start
python template_example.py start
python upload_example.py start
```