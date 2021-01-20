import os
package='helloworld'
repo='https://raw.githubusercontent.com/toto112358/pypack-repo/master/packages'
branch='stable'
url=repo+'/'+branch+'/'+package+'.zst'
print(url)
os.system('mkdir test && cd test')
os.system(f'curl -Os {url} | zstdcat | sh')
