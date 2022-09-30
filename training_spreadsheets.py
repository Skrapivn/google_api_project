# Новый импорт.
import os

from dotenv import load_dotenv
from google.oauth2.service_account import Credentials
from googleapiclient import discovery

SCOPES = [
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive',
]

load_dotenv()

EMAIL_USER = os.environ['EMAIL']

info = {
    'type':  os.environ['TYPE'],
    'project_id':  os.environ['PROJECT_ID'],
    'private_key_id':  os.environ['PRIVATE_KEY_ID'],
    'private_key':  os.environ['PRIVATE_KEY'],
    'client_email':  os.environ['CLIENT_EMAIL'],
    'client_id':  os.environ['CLIENT_ID'],
    'auth_uri':  os.environ['AUTH_URI'],
    'token_uri':  os.environ['TOKEN_URI'],
    'auth_provider_x509_cert_url':  os.environ['AUTH_PROVIDER_X509_CERT_URL'],
    'client_x509_cert_url':  os.environ['CLIENT_X509_CERT_URL']
}


def auth():
    credentials = Credentials.from_service_account_info(
        info=info, scopes=SCOPES)
    service = discovery.build('sheets', 'v4', credentials=credentials)
    return service, credentials

def create_spreadsheet(service):
    # Тело spreadsheet
    spreadsheet_body = {
         # Свойства документа
        'properties': {
            'title': 'Бюджет путешествий',
            'locale': 'ru_RU'
        },
        # Свойства листов документа
        'sheets': [{
            'properties': {
                'sheetType': 'GRID',
                'sheetId': 0,
                'title': 'Отпуск 2077',
                'gridProperties': {
                    'rowCount': 100,
                    'columnCount': 100
                }
             }
         }]
    }
    request = service.spreadsheets().create(body=spreadsheet_body)
    response = request.execute()
    spreadsheetId = response['spreadsheetId']
    print('https://docs.google.com/spreadsheets/d/' + spreadsheetId)
    return spreadsheetId

def set_user_permissions(spreadsheetId, credentials):
    permissions_body={'type': 'user', # Тип учетных данных.
                      'role': 'writer', # Права доступа для учётной записи.
                      'emailAddress': EMAIL_USER} # Ваш личный гугл-аккаунт.
    
    # Создаётся экземпляр класса Resource для Google Drive API.
    drive_service = discovery.build('drive', 'v3', credentials=credentials)
    
    # Формируется и сразу выполняется запрос на выдачу прав вашему аккаунту.
    drive_service.permissions().create(
        fileId=spreadsheetId,
        body=permissions_body,
        fields='id'
    ).execute() 

def spreadsheet_update_values(service, spreadsheetId):
    # Данные для заполнения: выводятся в таблице сверху вниз, слева направо.
    table_values = [
        ['Бюджет путешествий'],
        ['Весь бюджет', '5000'],
        ['Все расходы', '=SUM(E7:E30)'],
        ['Остаток', '=B2-B3'],
        ['Расходы'],
        ['Описание', 'Тип', 'Кол-во', 'Цена', 'Стоимость'],
        ['Перелет', 'Транспорт', '2', '400', '=C7*D7']
    ]
    
    # Тело запроса.
    request_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    # Формирование запроса к Google Sheets API. 
    request = service.spreadsheets().values().update(
        spreadsheetId=spreadsheetId,
        range='Отпуск 2077!A1:F20',
        valueInputOption='USER_ENTERED',
        body=request_body
    )
    # Выполнение запроса.
    request.execute()

# def read_values(service, spreadsheet_id):
#     request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range='Отпуск 2077!A1:F20').execute()
#     print(request.get('values', []))


service, credentials = auth()
spreadsheetId = create_spreadsheet(service)
set_user_permissions(spreadsheetId, credentials)
spreadsheet_update_values(service, spreadsheetId)
# read_values(service, spreadsheetId)
