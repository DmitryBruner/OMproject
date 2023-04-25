import urllib.request
import requests
import csv

names = []
urls = []
with open('test.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        split_row = row[0].split(';')
        names.append(split_row[0])
        urls.append(split_row[1])

print(names)
print(urls)

img_url = 'https://eda.yandex.ru/images/3808326/1b1c7de759594d7f5cf5bd9af57f5a93.jpg'

def download(name='', url=''):
    try:
        response = requests.get(url=url)
        with open(f'img/{name}.jpeg', 'wb') as file:
            file.write((response.content))

        return 'Img successfuly downloaded!'
    except Exception as ex:
        return 'Upps...'

def main():
    for x in range(0, len(names)):
        print(download(names[x],urls[x]))


if __name__ == '__main__':
    main()
