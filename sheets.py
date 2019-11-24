import gspread
import requests
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
        return requests.get(albi._url('/{item_index}?locations=Caerleon'.format(item_index=item_index))).json()

class create(albi):
    def thetford(coll, roww, item_index):
        requests.get(albi._url('/{item_index}?locations=Thetford'.format(item_index=item_index))).json()
        text = albi.mini_price(item_index)
        sheet.update_cell(coll, roww, '{value}'.format(value=text))
        c = sheet.cell(coll, roww).value
        left = "'sell_price_min':"
        leftn = c.find(left)
        right = "'sell_price_min_date':"
        rightn = c.find(right)
        cc = c[leftn:rightn]
        cx = cc[17:-2]
        return sheet.update_cell(coll, roww, '{value}'.format(value=cx))


create.thetford(4, 3, 'T2_WOOD')
create.thetford(4, 4, 'T3_WOOD')
create.thetford(4, 5, 'T4_WOOD')
create.thetford(4, 6, 'T5_WOOD')
create.thetford(4, 7, 'T6_WOOD')
create.thetford(4, 8, 'T7_WOOD')
create.thetford(4, 9, 'T8_WOOD')
create.thetford(6, 3, 'T2_PLANKS')
create.thetford(6, 4, 'T3_PLANKS')
create.thetford(6, 5, 'T4_PLANKS')
create.thetford(6, 6, 'T5_PLANKS')
create.thetford(6, 7, 'T6_PLANKS')
create.thetford(6, 8, 'T7_PLANKS')
create.thetford(6, 9, 'T8_PLANKS')
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


# https://www.albion-online-data.com/api/v2/stats/view/T3_BAG?locations=Caerleon
numRows = sheet.row_count  # Get the number of rows in the sheet
