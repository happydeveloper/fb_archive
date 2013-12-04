from setuptools import setup

setup(name='YourAppName', version='1.0',
      description='OpenShift Python-2.7 Community Cartridge based application',
      author='Sean Moon', author_email='daeseonmoon@gmail.com',
      url='http://www.python.org/sigs/distutils-sig/',

      #  Uncomment one or more lines below in the install_requires section
      #  for the specific client drivers/modules your application needs.
      install_requires=['greenlet', 'gevent', 'Flask','pymongo','Flask-Pymongo'
                        #  'MySQL-python',
                        #  'pymongo',
                        #  'psycopg2',
      ],
     )
