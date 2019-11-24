import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials
from threading import Thread

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Prices").sheet1  # Open the spreadhseet

#-------------------------------------------------------------------------------------------------------------#

class Albi(object):
    def _url(endpoint):
        return 'https://www.albion-online-data.com/api/v2/stats/prices' + endpoint
    def mini_price(item_index):
        return requests.get(Albi._url('/{item_index}?locations=Swamp Cross'.format(item_index=item_index))).json()

class create(Albi):
    def thetford(coll, roww, item_index):
        requests.get(Albi._url('/{item_index}?locations=Thetford'.format(item_index=item_index))).json()
        text = Albi.mini_price(item_index)
        sheet.update_cell(coll, roww, '{value}'.format(value=text))
        c = sheet.cell(coll, roww).value
        left = "'sell_price_min':"
        leftn = c.find(left)
        right = "'sell_price_min_date':"
        rightn = c.find(right)
        cc = c[leftn:rightn]
        cx = cc[17:-2]
        return sheet.update_cell(roww, coll, '{value}'.format(value=cx))

class check(object):
    def che():
        create.thetford(4, 3, 'T2_WOOD')
        create.thetford(4, 4, 'T3_WOOD')
        create.thetford(4, 5, 'T4_WOOD')
        return create.thetford(4, 6, 'T5_WOOD')

    def cche():
        create.thetford(6, 3, 'T2_PLANKS')
        create.thetford(6, 4, 'T2_PLANKS')
        create.thetford(6, 5, 'T2_PLANKS')
        return create.thetford(6, 6, 'T2_PLANKS')


thread1 = Thread(target=check.che())
thread2 = Thread(target=check.cche())

thread1.start()
thread2.start()
thread1.join()
thread2.join()