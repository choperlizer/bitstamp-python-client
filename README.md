bitstamp-api-lib
======================

Python code to communicate with bitstamp.net API.
Compatible with Python v2, v3.3 and higher.


### Overview ###

In bitstamp.client lib there are two classes. One for public part of API and second for trading part.
Public class doesn't need user credentials, because API commands which this class implements are not bound to bitstamp user account.

Description of API:
https://www.bitstamp.net/api/


### Package requirements ###

* requests


### Activate new API ###

1. Login your Bitstamp Account.
2. Click on Security -> Api Access.
3. Select permissions which you want to have for you access key (If you don't check any box, you will get error message 'No permission found' after each API call)
4. Click 'Generate key' button and don't forget to write down your Secret!
5. Click Activate
6. Goto your Inbox and click on link sent by Bitstamp service
7. Your account is activated Now and you can use API


### Usage example ###

Add username, key & secret in eee-test.py
Run ./eee-test.py

TestCase test/*.client.py
http://docs.python.org/2/library/unittest.html

### Source info ###

Bitstamp API python implementation:
Kamil Madac
github=kmadac
email=kamil.madac@gmail.com

