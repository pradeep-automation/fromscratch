import pandas as pd

def get_user_credentials():
    excel_data = pd.read_excel("login.xlsx")
    return excel_data.to_dict(orient='records')


print(get_user_credentials())

