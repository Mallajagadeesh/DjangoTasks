from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient
from collections import OrderedDict
from pymongo import MongoClient
import sys

# Set the default encoding to utf-8
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf8', buffering=1)

endpoint = "https://voter-ocr.cognitiveservices.azure.com/"
key = "9eb8bcf2d9324a5da422f817000925b4"

model_id = "New_voter"
formUrl = "https://voterbucket.blob.core.windows.net/voter/2023-EROLLGEN-S01-27-DraftRoll-Revision1-ENG-183-WI.pdf"

# Create the Document Analysis client
document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

# Begin analyzing the document using the custom model
poller = document_analysis_client.begin_analyze_document_from_url(model_id, formUrl)
result = poller.result()

# Create an ordered dictionary to store the fields and their values in order
fields_output = OrderedDict()

### Connect to MongoDB
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['Different_voters']  # Replace 'my_database' with your desired database name
collection = db['Azure_voter_details']  # Replace 'my_collection' with your desired collection name

# Insert the fields_output dictionary into MongoDB
insert_result = collection.insert_one(dict(fields_output))  # Convert ordered dict to regular dict before insertion

# Close the MongoDB connection
mongo_client.close()

for idx, document in enumerate(result.documents):
    print("--------Analyzing document #{}--------".format(idx + 1))
    print("Document has type {}".format(document.doc_type))
    print("Document has confidence {}".format(document.confidence))
    print("Document was analyzed by model with ID {}".format(result.model_id))

    # Extracting and storing fields in the fields_output dictionary
    for name, field in document.fields.items():
        if field.value:
            field_value = field.value
        else:
            field_value = field.content

        print("......found field of type '{}' with value '{}' and with confidence {}".format(field.value_type, field_value, field.confidence).encode('utf-8'))

        fields_output[name] = field_value

# Insert the fields_output dictionary into MongoDB
collection.insert_one(fields_output)

# Print the fields output in order
print("\nFields Output (Order Wise):")
for key, value in fields_output.items():
    print("{}: {}".format(key, value))








