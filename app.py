from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from seimei_hantei import calculate_seimei_hantei

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # セッション用のシークレットキー

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        surname = data.get('surname', '').strip()
        given_name = data.get('given_name', '').strip()
        
        if not surname or not given_name:
            return jsonify({'error': '苗字と名前を入力してください'}), 400
        
        # 計算結果をセッションに保存
        result = calculate_seimei_hantei(surname, given_name)
        session['calculation_result'] = {
            'surname': surname,
            'given_name': given_name,
            'result': result
        }
        
        return jsonify({'success': True})
        
    except Exception as e:
        return jsonify({'error': f'計算エラーが発生しました: {str(e)}'}), 500

@app.route('/advertisement')
def advertisement():
    # セッションに計算結果があるかチェック
    if 'calculation_result' not in session:
        return redirect(url_for('index'))
    return render_template('advertisement.html')

@app.route('/result')
def result():
    # セッションから計算結果を取得
    if 'calculation_result' not in session:
        return redirect(url_for('index'))
    
    result_data = session['calculation_result']
    return render_template('result.html', 
                         surname=result_data['surname'],
                         given_name=result_data['given_name'],
                         result=result_data['result'])

if __name__ == '__main__':
    app.run(debug=True)