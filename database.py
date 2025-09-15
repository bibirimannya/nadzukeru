import sqlite3
from datetime import datetime
import os

class Database:
    def __init__(self, db_name='nadzukeru.db'):
        self.db_name = db_name
        # データベースファイルの整合性チェック
        self._check_and_init_db()
    
    def _check_and_init_db(self):
        """データベースファイルをチェックして初期化"""
        try:
            # ファイルが存在する場合、SQLiteデータベースかチェック
            if os.path.exists(self.db_name):
                if not self._is_valid_database():
                    print(f"警告: {self.db_name} は有効なSQLiteデータベースではありません。削除して再作成します。")
                    os.remove(self.db_name)
            
            # データベースを初期化
            self.init_db()
            
        except Exception as e:
            print(f"データベースチェックエラー: {e}")
            # エラーの場合、ファイルを削除して再作成
            if os.path.exists(self.db_name):
                try:
                    os.remove(self.db_name)
                    print(f"{self.db_name} を削除しました")
                except:
                    pass
            self.init_db()
    
    def _is_valid_database(self):
        """SQLiteデータベースファイルかチェック"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            conn.close()
            return True
        except sqlite3.DatabaseError:
            return False
        except Exception:
            return False
    
    def init_db(self):
        """データベースとテーブルを初期化"""
        try:
            # 新しいデータベース接続を作成
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            # SQLite設定の最適化
            cursor.execute('PRAGMA journal_mode = WAL;')
            cursor.execute('PRAGMA synchronous = NORMAL;')
            cursor.execute('PRAGMA temp_store = memory;')
            cursor.execute('PRAGMA mmap_size = 268435456;')  # 256MB
            
            # 診断履歴テーブルの作成
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS diagnosis_history (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    surname TEXT NOT NULL,
                    given_name TEXT NOT NULL,
                    tenkaku INTEGER DEFAULT 0,
                    jinkaku INTEGER DEFAULT 0,
                    chikaku INTEGER DEFAULT 0,
                    gaikaku INTEGER DEFAULT 0,
                    soukaku INTEGER DEFAULT 0,
                    total_fortune TEXT DEFAULT '不明',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # インデックスの作成（パフォーマンス向上）
            cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_created_at 
                ON diagnosis_history(created_at DESC)
            ''')
            
            cursor.execute('''
                CREATE INDEX IF NOT EXISTS idx_name 
                ON diagnosis_history(surname, given_name)
            ''')
            
            conn.commit()
            conn.close()
            
            print(f"データベース '{self.db_name}' を正常に初期化しました")
            
        except Exception as e:
            print(f"データベース初期化エラー: {e}")
            raise e
    
    def save_diagnosis(self, surname, given_name, results):
        """診断結果を保存"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            # results辞書から各値を安全に取得
            def safe_get_score(key):
                item = results.get(key, {})
                if isinstance(item, dict):
                    return item.get('score', 0)
                return 0
            
            tenkaku = safe_get_score('天格')
            jinkaku = safe_get_score('人格')
            chikaku = safe_get_score('地格')
            gaikaku = safe_get_score('外格')
            soukaku = safe_get_score('総格')
            total_fortune = results.get('総合運勢', '不明')
            
            cursor.execute('''
                INSERT INTO diagnosis_history 
                (surname, given_name, tenkaku, jinkaku, chikaku, gaikaku, soukaku, total_fortune)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                surname,
                given_name,
                tenkaku,
                jinkaku,
                chikaku,
                gaikaku,
                soukaku,
                total_fortune
            ))
            
            conn.commit()
            conn.close()
            
            print(f"診断結果を保存しました: {surname} {given_name}")
            
        except Exception as e:
            print(f"診断結果保存エラー: {e}")
            # エラーでも例外は投げない（アプリの継続のため）
    
    def get_recent_diagnoses(self, limit=10):
        """最近の診断履歴を取得"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT surname, given_name, total_fortune, created_at
                FROM diagnosis_history
                ORDER BY created_at DESC
                LIMIT ?
            ''', (limit,))
            
            results = cursor.fetchall()
            conn.close()
            
            return results
            
        except Exception as e:
            print(f"診断履歴取得エラー: {e}")
            return []
    
    def get_diagnosis_count(self):
        """総診断数を取得"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute('SELECT COUNT(*) FROM diagnosis_history')
            count = cursor.fetchone()[0]
            
            conn.close()
            return count
            
        except Exception as e:
            print(f"診断数取得エラー: {e}")
            return 0
    
    def get_diagnosis_by_name(self, surname, given_name):
        """特定の名前の診断履歴を取得"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT * FROM diagnosis_history
                WHERE surname = ? AND given_name = ?
                ORDER BY created_at DESC
            ''', (surname, given_name))
            
            results = cursor.fetchall()
            conn.close()
            
            return results
            
        except Exception as e:
            print(f"名前別診断履歴取得エラー: {e}")
            return []
    
    def reset_database(self):
        """データベースをリセット（開発用）"""
        try:
            if os.path.exists(self.db_name):
                os.remove(self.db_name)
                print(f"データベースファイル {self.db_name} を削除しました")
            
            self.init_db()
            print("データベースをリセットしました")
            
        except Exception as e:
            print(f"データベースリセットエラー: {e}")