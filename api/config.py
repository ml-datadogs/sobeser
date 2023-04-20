import os
import json

with open(os.environ['SECRETS_JSON']) as handle:
    SECRETS = json.loads(handle.read())

SERVICE_X_CREDS = {
    'database': SECRETS['DATABASE_CREDENTIALS']
}

