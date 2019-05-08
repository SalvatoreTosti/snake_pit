from distutils.core import setup
setup(
  name = 'snakePit',         # How you named your package folder (MyLib)
  packages = ['snakePit'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        
  description = 'Customizable multi-processing system.',
  author = 'Salvatore Tosti',                   
  author_email = 'your.email@domain.com',
  url = 'https://github.com/SalvatoreTosti/snake_pit',   
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    
  keywords = ['Multiprocessing', 'multi', 'processing', 'multithreading', 'threading'],   
  classifiers=[
    'Development Status :: 3 - Alpha',    
    'Intended Audience :: Developers',  
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
  ],
)