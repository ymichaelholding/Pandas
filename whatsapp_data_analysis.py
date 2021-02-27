# import the package pandas
import pandas as pd


# get the file contents
def get_file_content():
    file_name = r'D:\Learning\python\pandas\WhatsApp.txt'
    details = open(file_name, encoding="utf8")
    return list(details.readlines())


# Validate the files
def get_dataframe():
    content = get_file_content()
    final = {"Date": [], "Phone": [], "message": []};
    for i in content:
        try:
            date_content = i.split('-')[0].replace(',', '').replace('/', '').replace(':', '').replace(' ', '')
            print(date_content, len(date_content))
            phone_number = str(i.split('-')[1])
            if date_content.isnumeric() == True and len(date_content) == 9:
                print(i)
                # full_content.append(inter)
                final['Date'].append(i.split('-')[0].replace(',', ''))
                final['Phone'].append(str(phone_number).replace("'", '|').split(':')[0])
                final['message'].append(i.split(':')[1])
        except:
            error = 'ee'

    print(len(final['Date']), len(final['Phone']), len(final['message']))
    return final


# top 10 active users bases on the numbers of messages
def get_active_users(dataframe):
    print(dataframe.groupby("Phone")["Phone"].count().nlargest(10))
    return 0


# top 10 active users bases on the numbers of messages
def get_inactive_users(dataframe):
    print(dataframe.groupby("Phone")["Phone"].count().nsmallest(10))
    return 0


# get the top 10 lengthly message
def get_lengthly_message(dataframe):
    dataframe['message_length'] = dataframe['message'].apply(len)
    print(dataframe.sort_values(by='message_length', ascending=False, na_position='last').head(10))
    return 0


def get_max_of_message_day(dataframe):
    print(dataframe.groupby(pd.to_datetime(dataframe['Date'].str[0:8], format="%m/%d/%y", exact=False))[
              'message'].count().sort_values(
        ascending=False).head(5))
    return 0


def main():
    ret_dict = get_dataframe();
    df = pd.DataFrame(ret_dict)
    get_active_users(df)
    get_inactive_users(df)
    get_lengthly_message(df)
    get_max_of_message_day(df)
    print(df.head(5))
    return 0


if __name__ == "__main__":
    main()

