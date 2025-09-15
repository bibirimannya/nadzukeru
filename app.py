from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from seimei_hantei import calculate_seimei_hantei

app = Flask(__name__)
app.secret_key = 'nadzukeru-secret-key-2024'

# データベース初期化（エラーハンドリング付き）
db = None
try:
    from database import Database
    db = Database()
    print("データベース初期化完了")
except Exception as e:
    print(f"データベース初期化失敗: {e}")
    print("データベース機能なしで起動します")

@app.route('/')
def index():
    """メインページ"""
    total_count = 0
    if db:
        try:
            total_count = db.get_diagnosis_count()
        except:
            total_count = 0
    
    return render_template('index.html', total_diagnoses=total_count)

@app.route('/calculate', methods=['POST'])
def calculate():
    """姓名判断計算処理"""
    try:
        data = request.get_json()
        surname = data.get('surname', '').strip()
        given_name = data.get('given_name', '').strip()
        
        if not surname or not given_name:
            return jsonify({'error': '苗字と名前を入力してください'}), 400
        
        # 姓名判断計算実行
        result = calculate_seimei_hantei(surname, given_name)
        
        # 計算結果をセッションに保存
        session['calculation_result'] = {
            'surname': surname,
            'given_name': given_name,
            'result': result
        }
        
        return jsonify({'success': True})
        
    except Exception as e:
        print(f"計算エラー: {e}")
        return jsonify({'error': f'計算エラーが発生しました: {str(e)}'}), 500

@app.route('/advertisement')
def advertisement():
    """広告表示ページ"""
    if 'calculation_result' not in session:
        return redirect(url_for('index'))
    return render_template('advertisement.html')

@app.route('/result')
def result():
    """結果表示ページ"""
    if 'calculation_result' not in session:
        return redirect(url_for('index'))
    
    result_data = session['calculation_result']
    
    # データベースに保存（エラーでも継続）
    if db:
        try:
            db.save_diagnosis(
                result_data['surname'], 
                result_data['given_name'], 
                result_data['result']
            )
        except Exception as e:
            print(f"データベース保存エラー: {e}")
    
    return render_template('result.html', 
                         surname=result_data['surname'],
                         given_name=result_data['given_name'],
                         result=result_data['result'])

if __name__ == '__main__':
    app.run(debug=True)