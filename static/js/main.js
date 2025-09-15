document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('seimei-form');
    const calculateBtn = document.getElementById('calculate-btn');
    const btnText = calculateBtn.querySelector('.btn-text');
    const loading = calculateBtn.querySelector('.loading');

    form.addEventListener('submit', async function(e) {
        e.preventDefault();

        const surname = document.getElementById('surname').value.trim();
        const givenName = document.getElementById('given_name').value.trim();

        if (!surname || !givenName) {
            alert('苗字と名前を入力してください');
            return;
        }

        // ローディング状態にする
        calculateBtn.disabled = true;
        btnText.style.display = 'none';
        loading.style.display = 'inline';

        try {
            const response = await fetch('/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    surname: surname,
                    given_name: givenName
                })
            });

            const data = await response.json();

            if (response.ok && data.success) {
                // 広告ページに遷移
                window.location.href = '/advertisement';
            } else {
                alert(data.error || '計算に失敗しました');
            }
        } catch (error) {
            alert('エラーが発生しました: ' + error.message);
        } finally {
            // ローディング状態を解除
            calculateBtn.disabled = false;
            btnText.style.display = 'inline';
            loading.style.display = 'none';
        }
    });
});