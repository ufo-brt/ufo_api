#************************************************************************************
#Web Scrapper for getting information of this site from this site http://www.nuforc.org
# in order to get all information possible of UFo sightings.
#************************************************************************************

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd


URL_CONSTANT='http://www.nuforc.org'
def request_info(url):
# Opening connection, grabbing the page, and closing the connection
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    # HTML parsing. Writing formatted HTML to page_soup variable.
    page_soup = soup(page_html, "html.parser")
    return uClient,page_soup

def urls_list_request(urls_list):
    df = pd.DataFrame()
    list_dataframes=[]
    for x in urls_list:
        list_dataframes.append(pd.read_html(x)[0])

    df=pd.concat(list_dataframes)
    return df
# This function is used to find the Nth occurrence of a string.
def close_url_connection(u_client):
    u_client.close()

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start
# Looping through the parsed HTML to get a list of all the HTML <A></A> tags.  These are the lines of
# HTML that contain the hyperlinks to the sub/drill-through reports.
def get_html_tag(html_tag,page_soup_obj):
    my_list = []
    for link in page_soup_obj.find_all(html_tag):
    #for link in page_soup_obj.find_all("a"):
        # print("href: {}".format(link.get("href")))
        my_list.append(link) 
    return my_list 

def formatting_urls(url,urls_list):
    my_url_list = []
    for x in urls_list:
        x_as_string = str(x)
        substring_start_position = find_nth(x_as_string, '"', 1)
        substring_start_position = substring_start_position + 1
        substring_end_position = find_nth(x_as_string, '"', 2)
        url_suffix = (x_as_string[substring_start_position:substring_end_position])
        individualReportURL = f"{url}/webreports/{url_suffix}"
        my_url_list.append(individualReportURL)
    print(len(my_url_list))
    return my_url_list[1:-1]

if __name__=='__main__':
    base_url=f'{URL_CONSTANT}/webreports/ndxevent.html'
    uClient,page_soup_obj=request_info(base_url)
    close_url_connection(uClient)
    urls_list=formatting_urls(URL_CONSTANT,get_html_tag('a',page_soup_obj))
    df=urls_list_request(urls_list)
    df.to_csv('ufos.csv')
    print(df.head())
    



# Connecting to each report URL, parsing the HTML table, extracting the contents, writing the data to
# a Pandas dataframe, writing dataframe to CSV file, and repeating the process for each report URL.

# a = 0

# for y in my_url_list:

#     a += 1

#     print("Iteration number - ", a)

#     print(str(y))

#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#     print("Current Time =", current_time)

#     if a == 1:

#         # print("inside if statement line 68")

#         url = str(y)

#         # Create a handle, page, to handle the contents of the website

#         page = requests.get(url)

#         # Store the contents of the website under doc

#         doc = lh.fromstring(page.content)

#         # arse data that are stored between <tr>..</tr> of HTML

#         tr_elements = doc.xpath('//tr')

#         # Create empty list
#         col = []
#         i = 0

#         # For each row, store each first element (header) and an empty list
#         for t in tr_elements[0]:
#             i += 1
#             name = t.text_content()
#             # print(i, name)
#             col.append((name, []))

#         # Since our first row is the header, data is stored on the second row onwards
#         for j in range(1, len(tr_elements)):
#             # T is our j'th row
#             T = tr_elements[j]

#             # If row is not of size 10, the //tr data is not from our table
#             if len(T) != 7:
#                 break

#             # i is the index of our column
#             i = 0

#             # Iterate through each element of the row
#             for t in T.iterchildren():
#                 data = t.text_content()
#                 # Check if row is empty
#                 if i > 0:
#                     # Convert any numerical value to integers
#                     try:
#                         data = int(data)
#                     except:
#                         pass
#                 # Append the data to the empty list of the i'th column
#                 col[i][1].append(data)
#                 # Increment i for the next column
#                 i += 1

#         Dict = {title: column for (title, column) in col}

#         master_df = pd.DataFrame(Dict)

#         master_df.to_csv(csv_filepath, encoding='utf-8')

#         # print(master_df.shape[0])

#     else:

#         # print("inside else statement line 68")

#         url = str(y)

#         # Create a handle, page, to handle the contents of the website

#         page = requests.get(url)

#         # Store the contents of the website under doc

#         doc = lh.fromstring(page.content)

#         # arse data that are stored between <tr>..</tr> of HTML

#         tr_elements = doc.xpath('//tr')

#         # Create empty list
#         col = []
#         i = 0

#         # For each row, store each first element (header) and an empty list
#         for t in tr_elements[0]:
#             i += 1
#             name = t.text_content()
#             # print(i, name)
#             col.append((name, []))

#         # Since our first row is the header, data is stored on the second row onwards
#         for j in range(1, len(tr_elements)):
#             # T is our j'th row
#             T = tr_elements[j]

#             # If row is not of size 10, the //tr data is not from our table
#             if len(T) != 7:
#                 break

#             # i is the index of our column
#             i = 0

#             # Iterate through each element of the row
#             for t in T.iterchildren():
#                 data = t.text_content()
#                 # Check if row is empty
#                 if i > 0:
#                     # Convert any numerical value to integers
#                     try:
#                         data = int(data)
#                     except:
#                         pass
#                 # Append the data to the empty list of the i'th column
#                 col[i][1].append(data)
#                 # Increment i for the next column
#                 i += 1

#         Dict = {title: column for (title, column) in col}

#         current_df = pd.DataFrame(Dict)

#         # print(current_df.shape[0])

#         # master_df = master_df.append(current_df)

#         # print("Current dataframe rowcount is ", master_df.shape[0])

#         current_df.to_csv(csv_filepath, mode='a', header=False)









