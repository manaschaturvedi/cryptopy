import json
import requests


def get_price(coin,currency='USD'):
	try:
		if coin == 'BTC':
			url = 'https://blockchain.info/ticker'
			blockchain_data = requests.get(url)
			blockchain_json = json.loads(blockchain_data.text)
			current_price = blockchain_json[currency]['last']
		elif coin == 'ETH':
			url = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,INR'
			eth_data = requests.get(url)
			eth_json = json.loads(eth_data.text)
			current_price = eth_json[currency]
		else:
			return 'Only BTC and ETH prices are being fetched as of this moment.'

		return current_price
	except Exception as e:
		print('Error fetching price:',e)

print get_price('BTC')