'''Azure table with Python'''
import json
import uuid
from azure.cosmosdb.table.tableservice import TableService

class Main:
    '''class main'''

    @classmethod
    def __init__(cls):
        '''method init'''
        cls.config = json.loads(open("config.json").read())
        cls.table_service = TableService(connection_string=cls.config['connectionString'])

    @classmethod
    def save_traceability(cls, message):
        '''insert message to table azure'''
        Traceability = {
            'PartitionKey': cls.config['partitionKey'],
            'RowKey': str(uuid.uuid4()),
            'Message': message
        }

        cls.table_service.insert_entity(cls.config['nameTable'], Traceability)

if __name__ == '__main__':
  Main().save_traceability('YOUR_MESSAGE')

