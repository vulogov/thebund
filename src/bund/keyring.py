##
## Operations with keyring
##
import os
import socket
import hvac
import rsa
from keypair import KeyPair
from message import Message


class KeyRing:
    def __init__(self, namespace="bund",
                name=socket.gethostname(),
                url="http://127.0.0.1:8200",
                token=os.environ["VAULT_AUTH_TOKEN"]):
        self.keys = KeyPair(name)
        self.name = name
        self.namespace = namespace
        self.url  = url
        self.token = token
        self.status = False
        self.connectToVault()
    def connectToVault(self):
        self.client = hvac.Client(url=self.url, token=self.token)
        if not self.client.is_authenticated():
            return False
        k = "%s/keys/%s"%(self.namespace, self.name)
        try:
            d = self.client.secrets.kv.v1.read_secret(k)
            self.keys.importPRI(d['data']['key'])
            self.keys.importPUB(d['data']['pub'])
        except hvac.exceptions.InvalidPath:
            secret = {  'key': self.keys.exportPRI(),
                        'pub': self.keys.exportPUB()
            }
            self.client.secrets.kv.v1.create_or_update_secret(k, secret)
            k = "%s/public/%s"%(self.namespace, self.name)
            self.client.secrets.kv.v1.create_or_update_secret(k, {'pub':secret['pub']})
        self.status = True
        return True
    def __getitem__(self, key):
        k = "%s/public/%s"%(self.namespace, key)
        d = self.client.secrets.kv.v1.read_secret(k)
        return rsa.PublicKey.load_pkcs1(d['data']['pub'])
    def seal(self, msg):
        return msg.seal(self)
    def unseal(self, data):
        msg = Message(_keys=self)
        if msg.unseal(data):
            return msg
        return None


if __name__ == '__main__':
    kr = KeyRing()
    pub = kr[socket.gethostname()]
    print(pub)
