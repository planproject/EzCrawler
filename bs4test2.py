import urllib3

def use_urllib():
    url_ip = 'https://bbs.sgamer.com/forum-283-1.html'
    response = urllib3.urlopen(url_ip)
    print("headers:")
    print(response.info())
    print(join([line for line in response.readlines()]))

if __name__ == '__main__':
    print('simple url')
    use_urllib()