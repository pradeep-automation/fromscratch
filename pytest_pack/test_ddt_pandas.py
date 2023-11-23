import pytest
import pandas as pd


def get_user_credentials():
    excel_data = pd.read_excel("login.xlsx")
    return excel_data.to_dict(orient='records')

def set_status(usr, pwd, status):
    df = pd.read_excel("login.xlsx")

    # Find the index to update based on the user credentials
    index = df[(df['Username'] == usr) & (df['Password'] == pwd)].index

    # Update the 'Status' column with the login status for the respective user credentials
    df.loc[index, 'Status'] = status

    # Write the updated DataFrame back to the Excel file
    df.to_excel("login.xlsx", index=False)


@pytest.fixture(params=get_user_credentials())
def user_credentials(request):
    return request.param


def simulate_login(username, password):
    # Simulating login based on credentials
    # Replace this with your actual login logic
    if username == "user1" and password == "pass1":
        return "Passed"
    else:
        return "Failed"


def test_login(user_credentials):
    user = user_credentials["Username"]
    password = user_credentials["Password"]
    print(f"logging with the credentials::: {user} and {password}")
    status = simulate_login(user, password)
    # res = {"Status": status}
    # df = pd.DataFrame(data = res)
    # # write data to the excel file
    # df.to_excel(startrow=2, startcol=3, index=False, columns=status)
    # Load the Excel file
    set_status(user, password, status)



