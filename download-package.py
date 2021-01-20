#!/usr/bin/python3
import os
cd = os.chdir
package='helloworld'
repo='https://raw.githubusercontent.com/toto112358/pypack-repo/master/packages'
branch='stable'
url=repo+'/'+branch+'/'+package+'.zst'
print(url)
os.system('mkdir test')
cd('test')
os.system(f'curl {url} | zstdcat | sh')
