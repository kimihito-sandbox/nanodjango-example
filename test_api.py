#!/usr/bin/env python3
"""
簡単なテストスクリプト - API エンドポイントの動作確認用
"""

import requests
import time
import json

BASE_URL = "http://localhost:8000"

def test_api():
    print("🧪 Nanodjango API テスト開始")
    
    try:
        # メインページのテスト
        print("\n1. メインページのテスト...")
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("✅ メインページ: OK")
        else:
            print(f"❌ メインページ: エラー {response.status_code}")
    
        # Add API のテスト
        print("\n2. Add API のテスト...")
        response = requests.get(f"{BASE_URL}/add")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Add API: OK - Count: {data.get('count')}")
        else:
            print(f"❌ Add API: エラー {response.status_code}")
    
        # Stats API のテスト
        print("\n3. Stats API のテスト...")
        response = requests.get(f"{BASE_URL}/stats")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Stats API: OK")
            print(f"   Total: {data.get('total')}")
            print(f"   Today: {data.get('today')}")
        else:
            print(f"❌ Stats API: エラー {response.status_code}")
    
        # 複数回アクセスのテスト
        print("\n4. 複数回アクセステスト...")
        for i in range(3):
            response = requests.get(f"{BASE_URL}/add")
            if response.status_code == 200:
                data = response.json()
                print(f"   アクセス {i+1}: Count = {data.get('count')}")
            time.sleep(0.5)
    
        print("\n🎉 テスト完了!")
        
    except requests.exceptions.ConnectionError:
        print("❌ サーバーに接続できません。")
        print("   python main.py start でサーバーを起動してから再実行してください。")
    except Exception as e:
        print(f"❌ エラーが発生しました: {e}")

if __name__ == "__main__":
    test_api()