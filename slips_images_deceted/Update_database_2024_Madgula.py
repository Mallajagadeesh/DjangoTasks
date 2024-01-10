######################## This code purpose of all data added in one collection #####################

# from pymongo import MongoClient
#
# # MongoDB connection string
# mongo_uri = "mongodb://localhost:27017"
#
# # Database and collection names
# database_name_1 = "2024_TOTALVOTERDATA"
# collection_name_1 = "2024_ivinpro_Madugula"
# collection_name_2 = "missing_data"
#
# # Connect to MongoDB
# client = MongoClient(mongo_uri)
#
# # Access the specified databases and collections
# db_1 = client[database_name_1]
# collection_1 = db_1[collection_name_1]
# db_2 = client[database_name_1]
# collection_2 = db_2[collection_name_2]
#
# # Query to retrieve documents from the second collection
# documents_2 = collection_2.find()
#
# # List to store multiple new documents
# new_documents = []
#
# # Iterate through each document in the second collection
# for document_2 in documents_2:
#     # Create a new document with all fields set to null
#     new_document = {
#         'Voter_SerialNumber': None,
#         'VoterId': None,
#         'Name': None,
#         'Guardian': None,
#         'Home': None,
#         'Age': None,
#         'Gender': None,
#         'Assembly_Constituency_No_and_Name': None,
#         'Constituency': None,
#         'State': None,
#         'pdf_name': None,
#         'Post_Office': None,
#         'Police_Station': None,
#         'Mandal': 'Madugula',
#         'Revenue_Division': None,
#         'District': None,
#         'Section_No_and_Name': None,
#         'Old_Voterid': None,
#         'Polling_Station_Name': None,
#         'Caste': None,
#         'CommentsForDissident': None,
#         'CommentsForJoinParty': None,
#         'CommentsForTeamContacted': None,
#         'ContactMode': None,
#         'ContactNumber': None,
#         'ContactedBy': None,
#         'CreatedBy': None,
#         'CreatedOn': None,
#         'CurrentAddress': None,
#         'Deleted': None,
#         'Dissident': None,
#         'Duplicate': None,
#         'Expired': None,
#         'Habitations_id': None,
#         'InformedPerson': None,
#         'InformedPersonForDissident': None,
#         'InterestToJoinParty': None,
#         'IsInfluencer': None,
#         'IsVoted': None,
#         'Non_Local_Address': None,
#         'Otherparty': None,
#         'PartyInclination_id': None,
#         'PhysicallyChallenged': None,
#         'PostelBallot': None,
#         'Profession': None,
#         'Strength': None,
#         'UpdatedOn': None,
#         'UserId_id': None,
#         'Weakness': None,
#         'WorkerId_id': None,
#         'influenced_Voters': None,
#         'outside_voter': None,
#         'inside_voter': None,
#         'Polling_Station_Number': None,
#         'Relation_Type': 'Father',
#         'Polling_Station_Location': None,
#         'ivin_id': None,
#         'Pin_Code': None,
#         'Main_Town_OR_Village': None,
#         'FirstName': None,
#         'LastName': None
#     }
#
#     # Update the new_document with all fields from the current document_2
#     new_document.update(document_2)
#
#     # Append the new document to the list
#     new_documents.append(new_document)
#
# # Insert multiple documents into the first collection
# result = collection_1.insert_many(new_documents)
#
# # Print the result of the insertion
# print(f"Inserted {len(result.inserted_ids)} documents")


################## THis code Ivinid added this code #############
# from pymongo import MongoClient
#
# # MongoDB connection string
# mongo_uri = "mongodb://localhost:27017"
#
# # Database and collection names
# database_name_1 = "2024_TOTALVOTERDATA"
# collection_name_1 = "2024_ivinpro_Madugula"
# collection_name_2 = "missing_data"
#
# # Connect to MongoDB
# client = MongoClient(mongo_uri)
#
# # Access the specified databases and collections
# db_1 = client[database_name_1]
# collection_1 = db_1[collection_name_1]
# db_2 = client[database_name_1]
# collection_2 = db_2[collection_name_2]
#
# # Specify the desired ivin_id to start from
# desired_ivin_id = 265472
#
# # Find the last document in the first collection and get its 'ivin_id'
# last_document_in_collection_1 = collection_1.find_one(sort=[('ivin_id', -1)])
# last_ivin_id = last_document_in_collection_1['ivin_id'] if last_document_in_collection_1 else 0
#
# # Update last_ivin_id to the desired_ivin_id if it is less than the desired_ivin_id
# if last_ivin_id < desired_ivin_id:
#     last_ivin_id = desired_ivin_id - 1
#
# # Query to retrieve documents from the second collection
# documents_2 = collection_2.find()
#
# # List to store multiple new documents
# new_documents = []
#
# # Iterate through each document in the second collection
# for document_2 in documents_2:
#     # Increment 'ivin_id' for the new document
#     last_ivin_id += 1
#
#     # Create a new document with the incremented 'ivin_id'
#     new_document = {
#         'ivin_id': last_ivin_id,
#         'Voter_SerialNumber': None,
#         'VoterId': None,
#         'Name': None,
#         'Guardian': None,
#         'Home': None,
#         'Age': None,
#         'Gender': None,
#         'Assembly_Constituency_No_and_Name': None,
#         'Constituency': None,
#         'State': None,
#         'pdf_name': None,
#         'Post_Office': None,
#         'Police_Station': None,
#         'Mandal': 'Madugula',
#         'Revenue_Division': None,
#         'District': None,
#         'Section_No_and_Name': None,
#         'Old_Voterid': None,
#         'Polling_Station_Name': None,
#         'Caste': None,
#         'CommentsForDissident': None,
#         'CommentsForJoinParty': None,
#         'CommentsForTeamContacted': None,
#         'ContactMode': None,
#         'ContactNumber': None,
#         'ContactedBy': None,
#         'CreatedBy': None,
#         'CreatedOn': None,
#         'CurrentAddress': None,
#         'Deleted': None,
#         'Dissident': None,
#         'Duplicate': None,
#         'Expired': None,
#         'Habitations_id': None,
#         'InformedPerson': None,
#         'InformedPersonForDissident': None,
#         'InterestToJoinParty': None,
#         'IsInfluencer': None,
#         'IsVoted': None,
#         'Non_Local_Address': None,
#         'Otherparty': None,
#         'PartyInclination_id': None,
#         'PhysicallyChallenged': None,
#         'PostelBallot': None,
#         'Profession': None,
#         'Strength': None,
#         'UpdatedOn': None,
#         'UserId_id': None,
#         'Weakness': None,
#         'WorkerId_id': None,
#         'influenced_Voters': None,
#         'outside_voter': None,
#         'inside_voter': None,
#         'Polling_Station_Number': None,
#         'Relation_Type': 'Father',
#         'Polling_Station_Location': None,
#         'Pin_Code': None,
#         'Main_Town_OR_Village': None,
#         'FirstName': None,
#         'LastName': None
#     }
#
#     # Update the new_document with all fields from the current document_2
#     new_document.update(document_2)
#
#     # Append the new document to the list
#     new_documents.append(new_document)
#
# # Insert multiple documents into the first collection
# result = collection_1.insert_many(new_documents)
#
# # Print the result of the insertion
# print(f"Inserted {len(result.inserted_ids)} documents")




########################### This code use of manually update data use this code ########################
# from pymongo import MongoClient
#
# # MongoDB connection string
# mongo_uri = "mongodb://localhost:27017"
#
# # Database and collection names
# database_name = "2024_TOTALVOTERDATA"
# collection_name = "2024_ivinpro_Madugula"
#
# # Connect to MongoDB
# client = MongoClient(mongo_uri)
#
# # Access the specified database and collection
# db = client[database_name]
# collection = db[collection_name]
#
# # New voter ID
# new_voter_id = 'T00JAgan'
#
# # Create a new document with all fields set to null
# new_document = {
#     'Voter_SerialNumber': None,
#     'VoterId': new_voter_id,
#     'Name': None,
#     'Guardian': None,
#     'Home': None,
#     'Age': None,
#     'Gender': None,
#     'Assembly_Constituency_No_and_Name': None,
#     'Constituency': None,
#     'State': None,
#     'pdf_name': None,
#     'Post_Office': None,
#     'Police_Station': None,
#     'Mandal': None,
#     'Revenue_Division': None,
#     'District': None,
#     'Section_No_and_Name': None,
#     'Old_Voterid': None,
#     'Polling_Station_Name': None,
#     'Caste': None,
#     'CommentsForDissident': None,
#     'CommentsForJoinParty': None,
#     'CommentsForTeamContacted': None,
#     'ContactMode': None,
#     'ContactNumber': None,
#     'ContactedBy': None,
#     'CreatedBy': None,
#     'CreatedOn': None,
#     'CurrentAddress': None,
#     'Deleted': None,
#     'Dissident': None,
#     'Duplicate': None,
#     'Expired': None,
#     'Habitations_id': None,
#     'InformedPerson': None,
#     'InformedPersonForDissident': None,
#     'InterestToJoinParty': None,
#     'IsInfluencer': None,
#     'IsVoted': None,
#     'Non_Local_Address': None,
#     'Otherparty': None,
#     'PartyInclination_id': None,
#     'PhysicallyChallenged': None,
#     'PostelBallot': None,
#     'Profession': None,
#     'Strength': None,
#     'UpdatedOn': None,
#     'UserId_id': None,
#     'Weakness': None,
#     'WorkerId_id': None,
#     'influenced_Voters': None,
#     'outside_voter': None,
#     'inside_voter': None,
#     'Polling_Station_Number': None,
#     'Relation_Type': None,
#     'Polling_Station_Location': None,
#     'ivin_id': None,
#     'Pin_Code': '531002',
#     'Main_Town_OR_Village': None,
#     'FirstName': None,
#     'LastName': None
# }
#
# # Insert the new document
# result = collection.insert_one(new_document)
#
# # Print the result of the insertion
# print(f"Inserted document with ID: {result.inserted_id}")






################# This code use ivinid highest count ###########
from pymongo import MongoClient

# MongoDB connection string
mongo_uri = "mongodb://localhost:27017"

# Database and collection names
database_name = "2024_TOTALVOTERDATA"
collection_name = "total_voter_data"

# Connect to MongoDB
client = MongoClient(mongo_uri)

db = client[database_name]
collection = db[collection_name]

# Query to retrieve all documents from the collection
documents = collection.find()

# Initialize variable to store the maximum ivin_id
max_ivin_id = None

# Iterate through each document to find the maximum ivin_id
for document in documents:
    ivin_id = document.get('ivin_id')

    # Check if ivin_id is not None and update max_ivin_id if it's the new maximum
    if ivin_id is not None:
        if max_ivin_id is None or ivin_id > max_ivin_id:
            max_ivin_id = ivin_id

# Print the highest ivin_id
print(f"The highest ivin_id is: {max_ivin_id}")

