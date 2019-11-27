import gspread
import requests
from threading import Thread
from oauth2client.service_account import ServiceAccountCredentials


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
        return requests.get(Albi._url('/{item_index}?locations=Highland Cross'.format(item_index=item_index))).json()

class create(Albi):
    def thetford(coll, roww, item_index):
        requests.get(Albi._url('/{item_index}?locations=Highland Cross'.format(item_index=item_index))).json()
        text = Albi.mini_price(item_index)
        sheet.update_cell(coll, roww, '{value}'.format(value=text))
        c = sheet.cell(coll, roww).value
        left = "'sell_price_min':"
        leftn = c.find(left)
        right = "'sell_price_min_date':"
        rightn = c.find(right)
        cc = c[leftn:rightn]
        cx = cc[17:-2]
        sheet.update_cell(coll, roww, '{value}'.format(value=cx))
        #wood


class set(object):

    def res(self, num):
        col = 3
        i = 1
        while i < 8:
            i += 1
            create.thetford(num, col, 'T{fi}_{self}'.format(fi=i, self=self))
            col += 1


thread1 = Thread(target=set.res, args=('WOOD', 139))
thread2 = Thread(target=set.res, args=('PLANKS', 141))
thread3 = Thread(target=set.res, args=('HIDE', 143))
thread4 = Thread(target=set.res, args=('LEATHER', 145))
thread5 = Thread(target=set.res, args=('ORE', 147))
thread6 = Thread(target=set.res, args=('METALBAR', 149))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
#  Да я вообще ни слова бля не понял :D ©Doomination
