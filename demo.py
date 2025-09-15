#!/usr/bin/env python3
"""
Nanodjango アプリケーションのデモスクリプト
基本的な機能説明とテスト手順を提供します
"""

def demo_info():
    """Nanodjangoアプリケーションの情報とテスト方法を表示"""
    print("🚀 Nanodjango Tutorial - デモ情報")
    print("=" * 50)
    
    print("\n📝 このプロジェクトについて:")
    print("   - Nanodjangoを使ったシンプルなカウンターアプリ")
    print("   - ページアクセス数をカウントして表示")
    print("   - REST API エンドポイント付き")
    print("   - Django Admin 管理画面")
    
    print("\n🛠️ セットアップ手順:")
    print("   1. pip install nanodjango")
    print("   2. python main.py start")
    print("   3. ブラウザで http://localhost:8000 にアクセス")
    
    print("\n📱 利用可能なURL:")
    print("   🏠 http://localhost:8000/          - メインページ")
    print("   📝 http://localhost:8000/admin/    - Django Admin")
    print("   👋 http://localhost:8000/hello     - サンプルページ")
    
    print("\n🔌 API エンドポイント:")
    print("   GET  /add     - カウント追加")
    print("   GET  /stats   - 統計情報取得")
    print("   POST /reset   - カウントリセット")
    
    print("\n💡 テスト方法:")
    print("   1. サーバー起動: python main.py start")
    print("   2. APIテスト:   python test_api.py")
    print("   3. ブラウザでWebページ確認")
    
    print("\n📚 学習ポイント:")
    print("   ✅ 単一ファイルでのDjangoアプリ構築")
    print("   ✅ @app.admin デコレータでの管理画面登録")
    print("   ✅ @app.route でのURL定義")
    print("   ✅ @app.api でのREST API作成")
    print("   ✅ Django ORMでのデータベース操作")
    
    print("\n🎯 nanodjangoの特徴:")
    print("   - 従来のDjangoと比べて設定が簡単")
    print("   - プロトタイピングに最適")
    print("   - 本格的なDjango機能も利用可能")
    print("   - API開発がシンプル")
    
    print("\n📖 詳細情報:")
    print("   - README.md     : 詳細な説明")
    print("   - EXAMPLES.md   : 追加実装例")
    print("   - main.py       : メインアプリケーション")
    print("   - test_api.py   : API テストスクリプト")
    
    print("\n🚀 今すぐ試してみよう!")
    print("   python main.py start")

if __name__ == "__main__":
    demo_info()