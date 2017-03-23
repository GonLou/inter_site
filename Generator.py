import csv


html5_start = """
<!DOCTYPE HTML>
<html lang = "en">
<head>
  <title>
"""
html5_after_title = """
  </title>
  <meta charset = "UTF-8" />
</head>
<body>
  <h2>
"""
html5_after_header = """
</h2>
  <ul>
"""
html5_end = """
  </ul>
</body>
</html>
"""
siteslist = []


def write_to_html(c, t):
    with open(t+'.html', 'w') as f:
        s = str(c)
        f.write(s)
        f.closed
    return 0


with open("sites.txt") as sites:
    sitesreader = csv.reader(sites, delimiter=',', quotechar='|')
    for total, row in enumerate(sitesreader):
        siteslist.append(row[0])

for i in range(0, total):
    compose = ""
    title = ""
    li_list = ""
    compose += html5_start
    for j, s in enumerate(siteslist):
        if j == i:
            compose += s
            compose += html5_after_title
            title = s.replace(".", "_")
            print(title)
        else:
            li_list += "<li><a href="+title+".html>" + s + "</a></li>"
    compose += title
    compose += html5_after_header
    compose += li_list
    compose += html5_end
    write_to_html(compose, title)
    print("%d file(s) written out of %d" % (i+1, total))
