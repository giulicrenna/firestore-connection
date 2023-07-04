from google.cloud import firestore

ACCOUNT_INFO : str = ''
collection : str = ''
document : str = ''


class Firestore():
    def __init__(self,
                 account_info_path: str,
                 collection : str,
                 document : str) -> None:
        
        self.account_info_path = account_info_path
        self.collection = collection
        self.document = document

        self.client : object = firestore.Client.from_service_account_json(ACCOUNT_INFO)
        self.ref = self.client.collection(collection)
        self.doc_ref = self.ref.document(document)

    def get_test(self) -> None:
        doc = self.doc_ref.get()

        if doc.exists:
            print(doc.id, doc.get('first'), doc.to_dict())
    
    