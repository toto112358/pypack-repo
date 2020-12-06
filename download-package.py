import requests
file_name='hello-world'
package=file_name
repo='https://raw.githubusercontent.com/toto112358/pypack-repo/master/packages'
branch='stable'
url=repo+'/'+branch+'/'+package
out_file='testing'
r=requests.get(url)
print(url)
with open(out_file, "wb") as code:
        code.write(r.content)
