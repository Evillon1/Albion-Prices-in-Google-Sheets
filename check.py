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
        return requests.get(Albi._url('/{item_index}?locations=Bridgewatch'.format(item_index=item_index))).json()

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
        return sheet.update_cell(coll, roww, '{value}'.format(value=cx))


create.thetford(8, 3, 'T2_HIDE')
create.thetford(8, 4, 'T3_HIDE')
create.thetford(8, 5, 'T4_HIDE')
create.thetford(8, 6, 'T5_HIDE')
create.thetford(8, 7, 'T6_HIDE')
create.thetford(8, 8, 'T7_HIDE')
create.thetford(8, 9, 'T8_HIDE')
create.thetford(10, 3, 'T2_LEATHER')
create.thetford(10, 4, 'T3_LEATHER')
create.thetford(10, 5, 'T4_LEATHER')
create.thetford(10, 6, 'T5_LEATHER')
create.thetford(10, 7, 'T6_LEATHER')
create.thetford(10, 8, 'T7_LEATHER')
create.thetford(10, 9, 'T8_LEATHER')
create.thetford(12, 3, 'T2_ORE')
create.thetford(12, 4, 'T3_ORE')
create.thetford(12, 5, 'T4_ORE')
create.thetford(12, 6, 'T5_ORE')
create.thetford(12, 7, 'T6_ORE')
create.thetford(12, 8, 'T7_ORE')
create.thetford(12, 9, 'T8_ORE')
create.thetford(14, 3, 'T2_METALBAR')
create.thetford(14, 4, 'T3_METALBAR')
create.thetford(14, 5, 'T4_METALBAR')
create.thetford(14, 6, 'T5_METALBAR')
create.thetford(14, 7, 'T6_METALBAR')
create.thetford(14, 8, 'T7_METALBAR')
create.thetford(14, 9, 'T8_METALBAR')


