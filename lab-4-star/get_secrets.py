import hvac
import os

vault_token = os.getenv('VAULT_TOKEN')
vault_url = 'http://localhost:8200'

client = hvac.Client(url=vault_url, token=vault_token)

secrets = client.secrets.kv.v1.read_secret(path='/data/myapp')
print(secrets['data']['data'])
