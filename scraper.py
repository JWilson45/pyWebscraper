import urllib.request
from requests import Session
from bs4 import BeautifulSoup as bs
from lxml import html

loginURL = "https://ilearn.marist.edu/sakai-login-tool/container"
homePageURL = "https://ilearn.marist.edu/portal"

with Session() as s:
    site = s.get(loginURL)
    bs_content = bs(site.content, "html.parser")
    token = bs_content.find("input", {"name":"lt"})["value"]
    data = {"username":"<Username>","password":"<Password>", "lt":token, "_eventId": "submit", "submit": "LOGIN"}
    s.post(loginURL,data=data)
    home_page = s.get(homePageURL)
    for isSuccess in bs(home_page.content, "html.parser")):
        if isSuccess.find("span", {""})
    print(home_page.content)



# currentSession = requests.session()
#
# ilearnLogin = "https://login.marist.edu/cas/login;jsessionid=377EC6DAAA9E36B4B58B96CED881D641?service=https%3A%2F%2Filearn.marist.edu%2Fsakai-login-tool%2Fcontainer"
# ilearnSite =  "https://ilearn.marist.edu/portal"
# result = currentSession.get(ilearnLogin)
#
# tree = html.fromstring(result.text)
# loginToken = list(set(tree.xpath("//input[@name='lt']/@value")))[0]
#
# print(loginToken)
#
# payload = {
# 	"username": "<Username>",
# 	"password": "<Password>",
# 	"lt": loginToken,
#     "_eventld": "submit",
#     "submit": "LOGIN"
# }
#
# result = currentSession.post(
# 	ilearnLogin,
# 	data = payload,
# 	headers = dict(referer=ilearnLogin)
# )
#
# result = currentSession.get(
# 	ilearnSite,
# 	headers = dict(referer = ilearnSite)
# )
#
# tree = html.fromstring(result.content)
# text = tree.xpath("//text()")
#
# print(text)
