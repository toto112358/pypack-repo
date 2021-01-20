#!/usr/bin/python3
#!/usr/bin/python3
import os
package='helloworld'
repo='https://raw.githubusercontent.com/toto112358/pypack-repo/master/packages'
branch='stable'
url=repo+'/'+branch+'/'+package+'.zst'
print(url)
os.system('mkdir test')
os.system(f'cd test && curl {url} | zstdcat | sh')
