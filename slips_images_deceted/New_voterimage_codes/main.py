# from pymongo import MongoClient
#
# # MongoDB connection string
# mongo_uri = "mongodb://localhost:27017"
#
# # Database and collection names
# database_name = "2024_TOTALVOTERDATA"
# collection_name = "Missing_data_added"
#
# # Connect to MongoDB
# client = MongoClient(mongo_uri)
#
# db = client[database_name]
# collection = db[collection_name]
#
# # Query to retrieve all documents from the collection
# documents = collection.find()
#
# # Print the values of each document
# for document in documents:
#     print(document)
#



from pymongo import MongoClient

# MongoDB connection string
mongo_uri = "mongodb://localhost:27017"

# Database and collection names
database_name_1 = "2024_TOTALVOTERDATA"
collection_name_1 = "2024_ivinpro_Madugula"
collection_name_2 = "Missing_data_added"

# Connect to MongoDB
client = MongoClient(mongo_uri)

# Access the specified databases and collections
db_1 = client[database_name_1]
collection_1 = db_1[collection_name_1]
db_2 = client[database_name_1]
collection_2 = db_2[collection_name_2]

# Query to retrieve documents from the second collection
documents_2 = collection_2.find()

# List to store multiple new documents
new_documents = []

# Iterate through each document in the second collection
for document_2 in documents_2:
    # Create a new document with all fields set to null
    new_document = {
        'Voter_SerialNumber': None,
        'VoterId': None,
        'Name': None,
        'Guardian': None,
        'Home': None,
        'Age': None,
        'Gender': None,
        'Assembly_Constituency_No_and_Name': None,
        'Constituency': None,
        'State': None,
        'pdf_name': None,
        'Post_Office': None,
        'Police_Station': None,
        'Mandal': 'Madugula',
        'Revenue_Division': None,
        'District': None,
        'Section_No_and_Name': None,
        'Old_Voterid': None,
        'Polling_Station_Name': None,
        'Caste': None,
        'CommentsForDissident': None,
        'CommentsForJoinParty': None,
        'CommentsForTeamContacted': None,
        'ContactMode': None,
        'ContactNumber': None,
        'ContactedBy': None,
        'CreatedBy': None,
        'CreatedOn': None,
        'CurrentAddress': None,
        'Deleted': None,
        'Dissident': None,
        'Duplicate': None,
        'Expired': None,
        'Habitations_id': None,
        'InformedPerson': None,
        'InformedPersonForDissident': None,
        'InterestToJoinParty': None,
        'IsInfluencer': None,
        'IsVoted': None,
        'Non_Local_Address': None,
        'Otherparty': None,
        'PartyInclination_id': None,
        'PhysicallyChallenged': None,
        'PostelBallot': None,
        'Profession': None,
        'Strength': None,
        'UpdatedOn': None,
        'UserId_id': None,
        'Weakness': None,
        'WorkerId_id': None,
        'influenced_Voters': None,
        'outside_voter': None,
        'inside_voter': None,
        'Polling_Station_Number': None,
        'Relation_Type': 'Father',
        'Polling_Station_Location': None,
        'ivin_id': None,
        'Pin_Code': None,
        'Main_Town_OR_Village': None,
        'FirstName': None,
        'LastName': None
    }

    # Update the new_document with all fields from the current document_2
    new_document.update(document_2)

    # Append the new document to the list
    new_documents.append(new_document)

# Insert multiple documents into the first collection
result = collection_1.insert_many(new_documents)

# Print the result of the insertion
print(f"Inserted {len(result.inserted_ids)} documents")


