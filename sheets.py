import gspread
import requests
from threading import Thread
import json
from albion_api_client import AlbionAPI
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Prices").sheet1  # Open the spreadhseet

data = sheet.get_all_records()  # Get a list of all records

row = sheet.row_values(3)  # Get a specific row
col = sheet.col_values(3)  # Get a specific column
cell = sheet.cell(1, 2).value  # Get the value of a specific cell


class albi(object):
    def _url(endpoint):
        return 'https://www.albion-online-data.com/api/v2/stats/prices' + endpoint

    def mini_price(item_index):
        return requests.get(albi._url('/{item_index}?locations=Thetford'.format(item_index=item_index))).json()

class create(albi):
    def thetford(coll, roww, item_index):
        requests.get(albi._url('/{item_index}?locations=Thetford'.format(item_index=item_index))).json()
        text = albi.mini_price(item_index)
        sheet.update_cell(roww, coll, '{value}'.format(value=text))
        c = sheet.cell(roww, coll).value
        left = "'sell_price_min':"
        leftn = c.find(left)
        right = "'sell_price_min_date':"
        rightn = c.find(right)
        cc = c[leftn:rightn]
        cx = cc[17:-2]
        return sheet.update_cell(roww, coll, '{value}'.format(value=cx))


thread1 = Thread(target=create.thetford, args=(3, 4, 'T2_WOOD'))
thread2 = Thread(target=create.thetford, args=(4, 4, 'T3_WOOD'))
thread3 = Thread(target=create.thetford, args=(5, 4, 'T4_WOOD'))
thread4 = Thread(target=create.thetford, args=(6, 4, 'T5_WOOD'))
thread5 = Thread(target=create.thetford, args=(7, 4, 'T6_WOOD'))
thread6 = Thread(target=create.thetford, args=(8, 4, 'T7_WOOD'))
thread7 = Thread(target=create.thetford, args=(9, 4, 'T8_WOOD'))
thread8 = Thread(target=create.thetford, args=(3, 6, 'T2_PLANKS'))
thread9 = Thread(target=create.thetford, args=(4, 6, 'T3_PLANKS'))
thread0 = Thread(target=create.thetford, args=(5, 6, 'T4_PLANKS'))
thread11 = Thread(target=create.thetford, args=(6, 6, 'T5_PLANKS'))
thread12 = Thread(target=create.thetford, args=(7, 6, 'T6_PLANKS'))
thread13 = Thread(target=create.thetford, args=(8, 6, 'T7_PLANKS'))
thread14 = Thread(target=create.thetford, args=(9, 6, 'T8_PLANKS'))
thread15 = Thread(target=create.thetford, args=(3, 8, 'T2_HIDE'))
thread16 = Thread(target=create.thetford, args=(4, 8, 'T3_HIDE'))
thread17 = Thread(target=create.thetford, args=(5, 8, 'T4_HIDE'))
thread18 = Thread(target=create.thetford, args=(6, 8, 'T5_HIDE'))
thread19 = Thread(target=create.thetford, args=(7, 8, 'T6_HIDE'))
thread20 = Thread(target=create.thetford, args=(8, 8, 'T7_HIDE'))
thread21 = Thread(target=create.thetford, args=(9, 8, 'T8_HIDE'))
thread22 = Thread(target=create.thetford, args=(3, 10, 'T2_LEATHER'))
thread23 = Thread(target=create.thetford, args=(4, 10, 'T3_LEATHER'))
thread24 = Thread(target=create.thetford, args=(5, 10, 'T4_LEATHER'))
thread25 = Thread(target=create.thetford, args=(6, 10, 'T5_LEATHER'))
thread26 = Thread(target=create.thetford, args=(7, 10, 'T6_LEATHER'))
thread27 = Thread(target=create.thetford, args=(8, 10, 'T7_LEATHER'))
thread28 = Thread(target=create.thetford, args=(9, 10, 'T8_LEATHER'))
thread29 = Thread(target=create.thetford, args=(3, 12, 'T2_ORE'))
thread30 = Thread(target=create.thetford, args=(4, 12, 'T3_ORE'))
thread31 = Thread(target=create.thetford, args=(5, 12, 'T4_ORE'))
thread32 = Thread(target=create.thetford, args=(6, 12, 'T5_ORE'))
thread33 = Thread(target=create.thetford, args=(7, 12, 'T6_ORE'))
thread34 = Thread(target=create.thetford, args=(8, 12, 'T7_ORE'))
thread35 = Thread(target=create.thetford, args=(9, 12, 'T8_ORE'))
thread36 = Thread(target=create.thetford, args=(3, 14, 'T2_METALBAR'))
thread37 = Thread(target=create.thetford, args=(4, 14, 'T3_METALBAR'))
thread38 = Thread(target=create.thetford, args=(5, 14, 'T4_METALBAR'))
thread39 = Thread(target=create.thetford, args=(6, 14, 'T5_METALBAR'))
thread40 = Thread(target=create.thetford, args=(7, 14, 'T6_METALBAR'))
thread41 = Thread(target=create.thetford, args=(8, 14, 'T7_METALBAR'))
thread42 = Thread(target=create.thetford, args=(9, 14, 'T8_METALBAR'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread0.start()
thread11.start()
thread12.start()
thread13.start()
thread14.start()
thread15.start()
thread16.start()
thread17.start()
thread18.start()
thread19.start()
thread20.start()
thread21.start()
thread22.start()
thread23.start()
thread24.start()
thread25.start()
thread26.start()
thread27.start()
thread28.start()
thread29.start()
thread30.start()
thread31.start()
thread32.start()
thread33.start()
thread34.start()
thread35.start()
thread36.start()
thread37.start()
thread38.start()
thread39.start()
thread40.start()
thread41.start()
thread42.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()
thread7.join()
thread8.join()
thread9.join()
thread0.join()
thread11.join()
thread12.join()
thread13.join()
thread14.join()
thread15.join()
thread16.join()
thread17.join()
thread18.join()
thread19.join()
thread20.join()
thread21.join()
thread22.join()
thread23.join()
thread24.join()
thread25.join()
thread26.join()
thread27.join()
thread28.join()
thread29.join()
thread30.join()
thread31.join()
thread32.join()
thread33.join()
thread34.join()
thread35.join()
thread36.join()
thread37.join()
thread38.join()
thread39.join()
thread40.join()
thread41.join()
thread42.join()





# https://www.albion-online-data.com/api/v2/stats/view/T3_BAG?locations=Caerleon
numRows = sheet.row_count  # Get the number of rows in the sheet
