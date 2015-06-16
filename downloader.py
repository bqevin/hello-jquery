import urllib

urllib.urlretrieve("second link", "test.mp3")
--------------------
import urllib2
response = urllib2.urlopen('http://www.example.com/')
html = response.read()
//////////////////////////////////////
import urllib2

url = "http://download.thinkbroadband.com/10MB.zip"

file_name = url.split('/')[-1]
u = urllib2.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 8192
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status,

f.close()
///////////////////////////////////////
rom __future__ import ( division, absolute_import, print_function, unicode_literals )

import sys, os, tempfile, logging

if sys.version_info >= (3,):
    import urllib.request as urllib2
    import urllib.parse as urlparse
else:
    import urllib2
    import urlparse

def download_file(url, desc=None):
    u = urllib2.urlopen(url)

    scheme, netloc, path, query, fragment = urlparse.urlsplit(url)
    filename = os.path.basename(path)
    if not filename:
        filename = 'downloaded.file'
    if desc:
        filename = os.path.join(desc, filename)

    with open(filename, 'wb') as f:
        meta = u.info()
        meta_func = meta.getheaders if hasattr(meta, 'getheaders') else meta.get_all
        meta_length = meta_func("Content-Length")
        file_size = None
        if meta_length:
            file_size = int(meta_length[0])
        print("Downloading: {0} Bytes: {1}".format(url, file_size))

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)

            status = "{0:16}".format(file_size_dl)
            if file_size:
                status += "   [{0:6.2f}%]".format(file_size_dl * 100 / file_size)
            status += chr(13)
            print(status, end="")
        print()

    return filename

url = "http://download.thinkbroadband.com/10MB.zip"
filename = download_file(url)
print(filename)
///////////////////////////////
import requests
import datetime

now = datetime.datetime.now().strftime("%Y%m%d")

folder = 'some path'

url = 'https://gats.pjm-eis.com/gats2/PublicReports/RenewableGeneratorsRegisteredInGATS/'#ExportTo'
payload = {'exportType' : 'CSV',
           'tabNumber' : ''}
doc = requests.post(url, data=payload, stream=True)

output = open(folder+now+'_GATSRegistered.csv','wb')
output.write(doc.content)
output.close()

------------CORRECTION:-----------
payload = {
# Form contents
}
r = requests.post(url, data=payload, stream=True)
with open(filename, 'wb') as output:
    for chunk in r.iter_content():
        output.write(chunk)
/////////////////////////////////////////
