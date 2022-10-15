from bs4 import BeautifulSoup
import requests



print('Enter your max price')
max_price = int(input('>'))
print('filtering prices')


def find_books():
    html_text = requests.get('http://books.toscrape.com/').text
    soup = BeautifulSoup(html_text,'lxml')
    books = soup.find_all('li',class_= 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
    for index, book in enumerate(books):
        price = book.find('p', class_='price_color').text[2::]
        if float(price) < max_price:
            title = book.h3.text.replace('  ', '')
            availability = book.find('p', class_='instock availability').text.replace(' ', '').replace('\n','')
            with open(f'Books/{index}.txt','w') as f:
                f.write(f'Book Title: {title}\n')
                f.write(f'Availability: {availability} \n')
                f.write(f'Price: ${price} \n')
            print(f'File Saved: {index}')


if __name__ == '__main__':
    find_books()