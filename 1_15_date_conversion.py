# Write a Program to convert date from yyyy-mm-dd format to dd-mm-yyyy format.

def ddmmyyyy(date):
    """
    This function takes a string 'date' in the format "yyyy-mm-dd" and returns  
    another string 'new_date' in the format "dd-mm-yyyy".
    """
    date=str(date)
    year=int(date[:4])
    month=int(date[5:7])
    day=int(date[8:10])
    print(f"{day}{date[4]}{month}{date[7]}{year}")

ddmmyyyy('2024/10/22')

map(str,input().split('-',maxsplit=10))