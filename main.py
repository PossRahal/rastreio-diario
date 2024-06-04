from flask import Flask, render_template, request, redirect
from Z_pega_satus import info
from Z_messages import send_message
from Z_escritor_sheets import insert_code, delete_code
import gspread

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1twOeHF9HuJv6wdwnPt0kXk6lqQdrtp8YGsFDxhXHm9Q')
worksheet = sh.sheet1

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enviado')
def result():
    code = request.args.get('code')
    phone = request.args.get('phone')
    day = request.args.get('day')
    try:
        result = info(code,1)
        try:
            send_message(phone, result)
        except:
            return redirect('falha/phone')
    except:
        return redirect('/falha/code')
    if day == 'on':
        insert_code(phone, code)
    text=info(code,0)    

    return render_template('enviado.html', code=code, phone=phone,text=text)


@app.route('/parar')
def stop():
    return render_template('parar.html')


@app.route('/removido')
def remove():
    code = request.args.get('codigo')
    codes = worksheet.col_values(2)
    if code in codes:
        delete_code(code)
        print('Código removido com sucesso')
    else:
        return redirect('falha/code2')
    return render_template('removido.html', code=code)


@app.route('/falha/code')
def falha_code():
    return render_template('falha_code.html')


@app.route('/falha/code2')
def falha_code2():
    return render_template('falha_code2.html')


@app.route('/falha/phone')
def falha_phone():
    return render_template('falha_phone.html')


if __name__ == '__main__':
    app.run(debug=True)