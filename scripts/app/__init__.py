import random
import requests
import os

from flask import Flask, jsonify
from dotenv import load_dotenv

from scripts.modules.blockchain.blockchain import Blockchain
from scripts.pubsub import PubSub

app = Flask(__name__)
blockchain = Blockchain()
pubsub = PubSub(blockchain)
load_dotenv()


@app.route('/')
def route_default():
    return 'Welcome to the blockChain'


@app.route('/blockchain')
def route_blockchain():
    return jsonify(blockchain.to_json())


@app.route('/blockchain/mine')
def route_blockchaine_mine():
    transaction_data = 'stubbed_transaction_data'

    blockchain.add_block(transaction_data)

    block = blockchain.chain[-1]
    pubsub.broadcast_block(block)

    return jsonify(block.to_json())


ROOT_PORT = 5000
PORT = ROOT_PORT

if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001, 6000)

    result = requests.get(f'http://localhost:{ROOT_PORT}/blockchain')
    result_blockchain = Blockchain.from_json(result.json())

    try:
        blockchain.replace_chain(result_blockchain.chain)
        print('/n -- Successfully synchronized the local chain')
    except Exception as e:
        print(f'\n -- Error Synchronizing: {e}')


app.run(port=PORT)
