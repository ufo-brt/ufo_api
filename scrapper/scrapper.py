from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import requests
import lxml.html as lh
import pandas as pd
from datetime import datetime


# This function is used to find the Nth occurrence of a string.

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

# This is to put the location of the file that gets created

csv_filepath = 'C:\\LocalRepos\\Disney_UFOProject\\UFOSightings.csv'

myurl = 'http://www.nuforc.org/webreports/ndxevent.html'

reportbaseurl = 'http://www.nuforc.org/webreports'

# Opening connection, grabbing the page, and closing the connection

uClient = uReq(myurl)
page_html = uClient.read()
uClient.close()

# HTML parsing. Writing formatted HTML to page_soup variable.

page_soup = soup(page_html, "html.parser")


# Looping through the parsed HTML to get a list of all the HTML <A></A> tags.  These are the lines of
# HTML that contain the hyperlinks to the sub/drill-through reports.

my_list = []

for link in page_soup.find_all("a"):
    # print("href: {}".format(link.get("href")))
    my_list.append(link)

# Looping through the list my_list variable containing the A tags records to extract only the
# report URL suffix.  An example is the value ndxe201912.html.

# This can be concatenated with the reportbaseurl variable to get the full URL of each report.

my_url_list = []

for x in my_list:

    x_as_string = str(x)

    substring_start_position = find_nth(x_as_string, '"', 1)
    substring_start_position = substring_start_position + 1

    substring_end_position = find_nth(x_as_string, '"', 2)
    url_suffix = (x_as_string[substring_start_position:substring_end_position])

    individualReportURL = reportbaseurl + '/' + url_suffix

    my_url_list.append(individualReportURL)


# Trimming off the first and last URLS in the last as they only link back to the NUFORC homepage.

my_url_list = my_url_list[1:-1]

print(len(my_url_list))


# Connecting to each report URL, parsing the HTML table, extracting the contents, writing the data to
# a Pandas dataframe, writing dataframe to CSV file, and repeating the process for each report URL.

a = 0

for y in my_url_list:

    a += 1

    print("Iteration number - ", a)

    print(str(y))

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)

    if a == 1:

        # print("inside if statement line 68")

        url = str(y)

        # Create a handle, page, to handle the contents of the website

        page = requests.get(url)

        # Store the contents of the website under doc

        doc = lh.fromstring(page.content)

        # arse data that are stored between <tr>..</tr> of HTML

        tr_elements = doc.xpath('//tr')

        # Create empty list
        col = []
        i = 0

        # For each row, store each first element (header) and an empty list
        for t in tr_elements[0]:
            i += 1
            name = t.text_content()
            # print(i, name)
            col.append((name, []))

        # Since our first row is the header, data is stored on the second row onwards
        for j in range(1, len(tr_elements)):
            # T is our j'th row
            T = tr_elements[j]

            # If row is not of size 10, the //tr data is not from our table
            if len(T) != 7:
                break

            # i is the index of our column
            i = 0

            # Iterate through each element of the row
            for t in T.iterchildren():
                data = t.text_content()
                # Check if row is empty
                if i > 0:
                    # Convert any numerical value to integers
                    try:
                        data = int(data)
                    except:
                        pass
                # Append the data to the empty list of the i'th column
                col[i][1].append(data)
                # Increment i for the next column
                i += 1

        Dict = {title: column for (title, column) in col}

        master_df = pd.DataFrame(Dict)

        master_df.to_csv(csv_filepath, encoding='utf-8')

        # print(master_df.shape[0])

    else:

        # print("inside else statement line 68")

        url = str(y)

        # Create a handle, page, to handle the contents of the website

        page = requests.get(url)

        # Store the contents of the website under doc

        doc = lh.fromstring(page.content)

        # arse data that are stored between <tr>..</tr> of HTML

        tr_elements = doc.xpath('//tr')

        # Create empty list
        col = []
        i = 0

        # For each row, store each first element (header) and an empty list
        for t in tr_elements[0]:
            i += 1
            name = t.text_content()
            # print(i, name)
            col.append((name, []))

        # Since our first row is the header, data is stored on the second row onwards
        for j in range(1, len(tr_elements)):
            # T is our j'th row
            T = tr_elements[j]

            # If row is not of size 10, the //tr data is not from our table
            if len(T) != 7:
                break

            # i is the index of our column
            i = 0

            # Iterate through each element of the row
            for t in T.iterchildren():
                data = t.text_content()
                # Check if row is empty
                if i > 0:
                    # Convert any numerical value to integers
                    try:
                        data = int(data)
                    except:
                        pass
                # Append the data to the empty list of the i'th column
                col[i][1].append(data)
                # Increment i for the next column
                i += 1

        Dict = {title: column for (title, column) in col}

        current_df = pd.DataFrame(Dict)

        # print(current_df.shape[0])

        # master_df = master_df.append(current_df)

        # print("Current dataframe rowcount is ", master_df.shape[0])

        current_df.to_csv(csv_filepath, mode='a', header=False)









