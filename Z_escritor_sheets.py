import gspread

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1twOeHF9HuJv6wdwnPt0kXk6lqQdrtp8YGsFDxhXHm9Q')
worksheet = sh.sheet1


def insert_code(phone, code):
    worksheet.append_row([phone, code])


def delete_code(code):
    codes = worksheet.col_values(2)
    while code in codes:
        index = int(codes.index(code))+1
        worksheet.delete_rows(index)
        codes.remove(code)
    print('Código removido com sucesso')



