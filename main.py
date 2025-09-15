from django.db import models
from django.utils import timezone
from nanodjango import Django

app = Django()

@app.admin
class CountLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"Access at {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']

@app.route("/")
def count(request):
    # IPアドレスを記録
    ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
    CountLog.objects.create(ip_address=ip)
    
    total_count = CountLog.objects.count()
    recent_logs = CountLog.objects.all()[:5]
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Nanodjango Counter Example</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f5f5f5; }}
            .container {{ max-width: 600px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            h1 {{ color: #333; text-align: center; }}
            .counter {{ font-size: 2em; text-align: center; margin: 20px 0; color: #007bff; }}
            .recent {{ margin-top: 30px; }}
            .log-item {{ padding: 10px; border-bottom: 1px solid #eee; }}
            .api-example {{ background: #f8f9fa; padding: 15px; border-radius: 5px; margin-top: 20px; }}
            .links {{ text-align: center; margin-top: 20px; }}
            .links a {{ margin: 0 10px; color: #007bff; text-decoration: none; }}
            .links a:hover {{ text-decoration: underline; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Nanodjango チュートリアルサンプル</h1>
            <div class="counter">アクセス数: {total_count}</div>
            
            <div class="recent">
                <h3>📊 最近のアクセス履歴</h3>
                {''.join([f'<div class="log-item">🕒 {log.timestamp.strftime("%Y-%m-%d %H:%M:%S")} - IP: {log.ip_address}</div>' for log in recent_logs])}
            </div>
            
            <div class="api-example">
                <h3>🔌 API使用例</h3>
                <p><strong>カウントを追加:</strong> <code>GET /add</code></p>
                <p><strong>統計情報:</strong> <code>GET /stats</code></p>
                <p><strong>リセット:</strong> <code>POST /reset</code></p>
            </div>
            
            <div class="links">
                <a href="/admin/">📝 Django Admin</a>
                <a href="/add">🔗 API Test</a>
                <a href="/stats">📊 Statistics</a>
            </div>
        </div>
    </body>
    </html>
    """
    return html

@app.api.get("/add")
def add_count(request):
    """カウントを追加してJSON形式で現在の数を返す"""
    ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
    CountLog.objects.create(ip_address=ip)
    return {"count": CountLog.objects.count(), "message": "Count added successfully"}

@app.api.get("/stats")
def get_stats(request):
    """統計情報をJSON形式で返す"""
    total_count = CountLog.objects.count()
    today_count = CountLog.objects.filter(
        timestamp__date=timezone.now().date()
    ).count()
    
    # 時間別アクセス数（過去24時間）
    from django.db.models import Count
    from django.utils import timezone
    from datetime import timedelta
    
    last_24h = timezone.now() - timedelta(hours=24)
    hourly_stats = CountLog.objects.filter(
        timestamp__gte=last_24h
    ).extra({
        'hour': 'strftime("%%H", timestamp)'
    }).values('hour').annotate(count=Count('id')).order_by('hour')
    
    return {
        "total": total_count,
        "today": today_count,
        "last_24_hours": total_count,  # 簡易版
        "hourly_breakdown": list(hourly_stats),
        "message": "Statistics retrieved successfully"
    }

@app.api.post("/reset")
def reset_count(request):
    """カウントをリセット（開発用）"""
    deleted_count = CountLog.objects.count()
    CountLog.objects.all().delete()
    return {
        "message": f"Reset successful. Deleted {deleted_count} records.",
        "count": 0
    }

@app.route("/hello")
def hello(request):
    """サンプルページ"""
    return """
    <html>
    <body style="font-family: Arial; text-align: center; padding: 50px;">
        <h1>👋 Hello from Nanodjango!</h1>
        <p>これはnanodjangoのサンプルページです。</p>
        <a href="/">← メインページに戻る</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
