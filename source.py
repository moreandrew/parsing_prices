import time
import urllib.request
from bs4 import BeautifulSoup


def get_html(url):
    try:
        response = urllib.request.urlopen(url)
        loaded_text = response.read()
    except urllib.error.URLError:
        loaded_text = 'error'

    return loaded_text


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find('title')
    title = tags.get_text()

    return title


def format_response(text):
    try:
        splitted_string = text.split('от ')  # it means "starting at" in Russian
        price_with_curr = splitted_string[1]
        price_without_curr = price_with_curr.split(' руб')  # It stands for Roubles in Russian
        price = price_without_curr[0].replace(' ', '')
    except IndexError:
        price = '0'

    return price


def main():
    # tracking execution time
    start_time = time.time()

    f = open('input.txt', 'r')
    urls = f.readlines()
    f.close()
    out = open('output.txt', 'w')
    i = 0

    for url in urls:
        raw_text = parse(get_html(url))
        clean_text = format_response(raw_text)

        # getting rid of breaklines
        no_ret = url.replace('\n', '')
        out.write(no_ret + '\t' + clean_text + '\n')

        # making sure we don't get banned
        time.sleep(3)

        i = i + 1
        print(i)
    out.close()

    # end of execution
    duration = time.time() - start_time
    print('duration of execution: {}'.format(duration))


main()
