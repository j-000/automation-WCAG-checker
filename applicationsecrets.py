from devsettings import DEVELOPMENT

# # email credentials
MAIL_USERNAME ='allgreencode@gmail.com'
MAIL_PASSWORD = 'AGC2020J#'
MAIL_DEFAULT_SENDER ='allgreencode@gmail.com'

SQLALCHEMY_TRACK_MODIFICATIONS = False 
SECRET_KEY ='sdasiodaifqcXvLHzs6uAEfcFAEdzrwdaifqcXvLHzs6uAEfcFAEdzrwdjafqcXvLHzs6uAEfcFAEdzrwoidsj'
SECURITY_PASSWORD_SALT = 'cXvLHzs6uAEfcFAEdzrwdjafqcXvLHzs6uAcXvLHzs6uAEfcFAEdzrwdjafqcXvLHzs6uAcXv'
#################################################################
''' Database '''
##################################################################
URI = 'supcpdb.cr2bi5gkfxzr.eu-west-2.rds.amazonaws.com'
PORT = '3306'
USER = 'supadmin'
SECRET = 'A2Sowb18!&sdkdqpLAKY2XEFJ383sjbcsdk72'
NAME = 'comphero'

if DEVELOPMENT:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
else:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}'.format(
    user=USER, password=SECRET, host=URI, port=PORT, dbname=NAME)