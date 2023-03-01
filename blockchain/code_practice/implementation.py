class Blockchain:

    def __init__(self):

        self.transactions = []
        self.chain = []
        self.nodes = set()
        #Generate random number to be used as node_id
        self.node_id = str(uuid4()).replace('-', '')
        #Create genesis block
        self.create_block(0, '00')

    def register_node(self, node_url):

    def verify_transaction_signature(self, sender_address, signature, transaction):

    def submit_transaction(self, sender_address, recipient_address, value, signature):

    def create_block(self, nonce, previous_hash):

    def hash(self, block):

    def proof_of_work(self):

    def valid_proof(self, transactions, last_hash, nonce, difficulty=MINING_DIFFICULTY):

    def valid_chain(self, chain):

    def resolve_conflicts(self):

app = Flask(__name__)
CORS(app)

blockchain = Blockchain()

@app.route('/')
def index():
    return render_template('./index.html')

@app.route('/configure')
def configure():
    return render_template('./configure.html')

