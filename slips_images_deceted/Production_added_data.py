from pymongo import MongoClient

# Updated MongoDB connection string
mongo_uri = "mongodb://devops_admin:Vivij0019ej@13.126.55.93/?authMechanism=DEFAULT"

# Database and collection names
database_name_1 = "IVINPRO"
collection_name_1 = "Voter_Master_List"
collection_name_2 = "voter_master_list_tally_08012024"

# Connect to MongoDB
client = MongoClient(mongo_uri)

# Access the specified databases and collections
db_1 = client[database_name_1]
collection_1 = db_1[collection_name_1]
db_2 = client[database_name_1]
collection_2 = db_2[collection_name_2]

# Specify the desired ivin_id to start from
desired_ivin_id = 265472

# Find the last document in the first collection and get its 'ivin_id'
last_document_in_collection_1 = collection_1.find_one(sort=[('ivin_id', -1)])
last_ivin_id = last_document_in_collection_1['ivin_id'] if last_document_in_collection_1 else 0

# Update last_ivin_id to the desired_ivin_id if it is less than the desired_ivin_id
if last_ivin_id < desired_ivin_id:
    last_ivin_id = desired_ivin_id - 1

# Query to retrieve documents from the second collection
documents_2 = collection_2.find()

# List to store multiple new documents
new_documents = []

# Iterate through each document in the second collection
for document_2 in documents_2:
    # Increment 'ivin_id' for the new document
    last_ivin_id += 1

    # Create a new document with the incremented 'ivin_id'
    new_document = {
        'ivin_id': last_ivin_id,
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
