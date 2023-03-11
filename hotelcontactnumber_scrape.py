## Installing requirements
# pip install requests
# pip install bs4
# pip install html5lib

import requests
from bs4 import BeautifulSoup
Hotel_no = 1
Page_no = 1
f = open('hotelcontactnumber_data.txt', 'w')
f.write('Hotel details\n')
f.write('Website : https://www.hotelcontactnumber.in/hotels-in-indore-209.html\n')
f.write('City : Indore\n')
f.write('State : Madhya Pradesh\n')
f.write('\n______________________________________________________________\n\n')

for pg_no in range(1,23):
    print('Page number : ',Page_no)
    f.write('Page number : {}\n'.format(Page_no))
    Page_no+=1

    ## Step 1: Get HTML
    url = 'https://www.hotelcontactnumber.in/hotels-in-indore-209.html/pag='
    r = requests.get(url+str(pg_no)+'/')
    htmlcontent = r.content

    ## Step 2: Parse the HTML
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    all_hotel = soup.find_all('div', class_ = "city_title")
    for hotels in all_hotel:
        hotel_name = hotels.h3.text
        hotel_url = hotels.find('a', href=True)
        print('S.no : ',Hotel_no)
        f.write('S.no : {}\n'.format(Hotel_no))
        Hotel_no+=1
        print('Hotel name : ',hotel_name)
        f.write('Hotel name : {}\n'.format(hotel_name))
        print('Website : ',hotel_url.get('href'))
        f.write('Website : {}\n'.format(hotel_url.get('href')))
        url = hotel_url.get('href')
        r = requests.get(url)
        htmlcontent = r.content
        soup = BeautifulSoup(htmlcontent, 'html.parser')
        contact_info = soup.find('div', class_ = 'table_address')
        address = contact_info.find_all('td')
        left = contact_info.find_all('td',class_ = 'table_space_td_left')
        right = contact_info.find_all('td',class_ = 'table_space_td_right')
        for list in range(len(left)):
            print(left[list].text, " : ", right[list].text)
            f.write(left[list].text)
            f.write(" : ")
            f.write(right[list].text)
            f.write('\n')
        print('Phone number : ', contact_info.find('td', class_='table_space_td_right1').text)
        f.write('Phone number : ')
        f.write(contact_info.find('td', class_='table_space_td_right1').text)
        f.write('\n')
        print('\n______________________________________________________\n')
        f.write('\n______________________________________________________________\n\n')
final_message = "Data of "+str(Hotel_no-1)+" hotels from "+str(Page_no-1)+' Scraped.'
f.write(final_message)
f.close()
print(final_message)