# Hotel Contact Number Scraper

This Python script scrapes hotel contact details like phone numbers, addresses, and websites of hotels in Indore, Madhya Pradesh, India. 

~Website : https://www.hotelcontactnumber.in

## Requirements

Make sure you have the following packages installed:

- `requests`
- `bs4`
- `html5lib`

To install these packages, run the following command in your terminal:

- pip install requests
- pip install bs4
- pip install html5lib

You can install these packages by running the following command in your terminal:
- pip install requests bs4 html5lib

## How to Use
- Clone this repository or download the script.
- Open the terminal in the same directory where the script is present.
- Run the script using the following command:

> python hotelcontactnumber_scraper.py

- The script will start scraping hotel contact details and will create a text file named hotelcontactnumber_data.txt in the same directory where the script is present.
- The scraped data will be written to the hotelcontactnumber_data.txt file in the following format:

```
Hotel details
Website : https://www.hotelcontactnumber.in/hotels-in-indore-209.html
City : Indore
State : Madhya Pradesh

______________________________________________________________

Page number : 1
S.no : 1
Hotel name : Hotel Ambassador
Website : https://www.hotelcontactnumber.in/hotel-ambassador-indore-1.html
Address :  11/5 Nath Mandir Road, South Tukoganj, Indore - 452001
Phone number : 0731-4008100

______________________________________________________

S.no : 2
Hotel name : Hotel Amar Vilas
Website : https://www.hotelcontactnumber.in/hotel-amar-vilas-indore-2.html
Address :  1-B Chandra Nagar, A.B.Road, Indore - 452001
Phone number : 0731-2528888

______________________________________________________

...

```
- The script will also print a final message indicating the total number of hotels scraped and the number of pages scraped.
- Data of 220 hotels from 22 Scraped.
