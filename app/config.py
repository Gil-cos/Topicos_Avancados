import os

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


# 'postgres://fatec:fatec@postgres:5432/pi'
# SQLALCHEMY_DATABASE_URI = 'postgres://umecukbhukghpw:ab54f571331b41ff9fbf760434d3c944d342d90a8727dc4693a4960fdce036de@ec2-52-44-55-63.compute-1.amazonaws.com:5432/d9428qgpam0o6u'