#!/usr/bin/env python3
__author__ = 'choperlizer'

import bitstamp.client

# public API
bs_client_public = bitstamp.client.public()
ticker = bs_client_public.ticker()
order_book = bs_client_public.order_book()
transactions = bs_client_public.transactions()
conversion_rate_usd_eur = bs_client_public.conversion_rate_usd_eur()

# trading API
bs_client_trading = bitstamp.client.trading(username='', key='', secret='')
account_balance = bs_client_trading.account_balance()
user_transactions = bs_client_trading.user_transactions()


print('BITSTAMP API LIBRARY\n'
      '====================\n'
      '\n'
      '# Commands:\n'
      'ticker\n'
      'order_book (group=True/False)\n'
      'transactions (timedelta_secs=86400)\n'
      'conversion_rate_usd_eur\n'
      'account_balance\n')
print()

print(account_balance)