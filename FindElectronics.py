import os
import glob
from bs4 import BeautifulSoup
import requests


def find_electronics(max_price,min_rating,choice):
    # Select from different types of electronics
    html_text = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops').text
    html_text2 = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets').text
    html_text3 = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/phones/touch').text
    if choice == 0:
        soup = BeautifulSoup(html_text,'lxml')
        item = 'computers'
    elif choice == 1:
        soup = BeautifulSoup(html_text2,'lxml')
        item = 'tablets'
    else:
        soup = BeautifulSoup(html_text3,'lxml')
        item = 'phones'
    # Filter through desired attributes
    electronics = soup.find_all('div', class_= 'col-sm-4 col-lg-4 col-md-4')
    for index, electronic in enumerate(electronics):
        price = electronic.div.div.h4.text
        if max_price >= float(price[1::]):
            rating = len(electronic.find_all('span', class_='glyphicon glyphicon-star'))
            if min_rating <= rating:
                name = electronic.find('a').get('title')
                description = electronic.find('p', class_='description').text
                reviews = electronic.find('p', class_='pull-right').text
                with open(f'electronics/{item}/{item[:-1]}{index}.txt','w') as f:
                    f.write(f'name: {name}\n')
                    f.write(f'price: {price}\n')
                    f.write(f'rating: {rating}\n')
                    f.write(f'reviews: {reviews}\n')
                    f.write(f'description: {description}\n')
    print('Files Saved')


if __name__ == '__main__':
    # Deletes previous searches
    files = glob.glob('/electronics/**/*.txt', recursive=True)
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))
    print('Press 0 for computers:\nPress 1 for tablets\nPress 2 for phones')
    choice = int(input('>'))
    print("Enter max price")
    max_price = int(input('>'))
    print('Enter min rating')
    min_rating = int(input('>'))

    if choice == 0:
        find_electronics(max_price,min_rating,0)
    elif choice == 1:
        find_electronics(max_price, min_rating,1)
    else:
        find_electronics(max_price, min_rating, 2)