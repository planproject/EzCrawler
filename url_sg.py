from urllib import request


#sg url https://bbs.sgamer.com/forum-283-1.html

# resp = request.urlopen(r)
# print(resp.read().decode("utf-8"))

sg_url = "https://bbs.sgamer.com/forum-283-1.html"
req = request.Request(sg_url)
req.add_header("User-Agent:", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36")

resp = request.urlopen(req)
resp = request.urlopen(req)
print(resp.read().decode("utf-8"))