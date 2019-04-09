import webbrowser
#
# webbrowser.open("https://www.python.org/")
# # previously we saw help function how it shows description. help() actually uses webbrowser
#
# # help(help())
#
# for i in range(10):
#     print(1, 2, 3, 4, 5, 6, sep='; ')
#
# for i in range(10):
#     print(i, end=' ')  # removes the by default new line

help(webbrowser)

chrome = webbrowser.get(using='chrome')
chrome.open_new("https://www.python.org/")