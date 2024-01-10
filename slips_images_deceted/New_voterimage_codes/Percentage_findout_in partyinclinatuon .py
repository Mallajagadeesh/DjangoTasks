# ####################### This code give party name get the percentage will come ##############
# from pymongo import MongoClient
#
# # Connection string for MongoDB
# connection_string = "mongodb://localhost:27017"
#
# # Connect to MongoDB
# client = MongoClient(connection_string)
#
# # Specify the database and collection for party
# party_collection_name = "party"
# database_name = "2024_TOTALVOTERDATA"
# party_database = client[database_name]
# party_collection = party_database[party_collection_name]
#
# # Specify the database and collection for voter master
# voter_collection_name = "Voter_master"
# voter_collection = party_database[voter_collection_name]
#
# desired_party_name = "Telugu Desam Party"  # Replace with the party name you're interested in
#
# # Search for documents with the specified party name in party collection
# party_cursor = party_collection.find({"PartyName": desired_party_name})
#
# for party_document in party_cursor:
#     party_name = party_document.get("PartyName")
#
#     # if party_name is not None:
#         # print(f"PartyName: {party_name}")
#
# # Search for documents with the specified PartyInclination_id in voter master collection
# query_criteria = {
#     "PartyInclination_id": party_document.get("PID"),  # Assuming PID is present in party collection
#     "IsVoted": True,
#     "outsidevoter": True,
#     "insidevoter": True
# }
#
# # Count the documents based on the criteria in voter master collection
# total_count = voter_collection.count_documents(query_criteria)
#
# # Count the documents based on "PartyInclination_id" only in voter master collection
# party_count = voter_collection.count_documents({"PartyInclination_id": party_document.get("PID")})
#
# # Calculate the percentage
# percentage = (total_count / float(party_count)) * 100 if party_count != 0 else 0
#
# # Print the results
# print(f"{desired_party_name} total Percentage: {percentage}%")



from pymongo import MongoClient

# Connection string for MongoDB
connection_string = "mongodb://localhost:27017"

# Connect to MongoDB
client = MongoClient(connection_string)

# Specify the database and collection for party
party_collection_name = "party"
database_name = "2024_TOTALVOTERDATA"
party_database = client[database_name]
party_collection = party_database[party_collection_name]

# Specify the database and collection for voter master
voter_collection_name = "Voter_master"
voter_collection = party_database[voter_collection_name]

desired_party_name = "Telugu Desam Party"  # Replace with the party name you're interested in

# Search for documents with the specified party name in party collection
party_cursor = party_collection.find({"PartyName": desired_party_name})

party_name = None
for party_document in party_cursor:
    party_name = party_document.get("PartyName")

# Check if party name was found in the party collection
if party_name is not None:
    # Search for documents with the specified PartyInclination_id in voter master collection
    query_criteria = {
        "PartyInclination_id": party_document.get("PID"),  # Assuming PID is present in party collection
        "IsVoted": True,
        "outsidevoter": True,
        "insidevoter": True
    }

    # Count the documents based on the criteria in voter master collection
    total_count = voter_collection.count_documents(query_criteria)

    # Count the documents based on "PartyInclination_id" only in voter master collection
    party_count = voter_collection.count_documents({"PartyInclination_id": party_document.get("PID")})

    # Calculate the percentage
    percentage = (total_count / float(party_count)) * 100 if party_count != 0 else 0

    # Determine the tendency
    if percentage >= 50:
        tendency = "Leading"
    else:
        tendency = "Trailing"

    # Print the results
    print(f"{desired_party_name} total Percentage: {percentage}%")
    print(f"Tendency: {tendency}")
else:
    print(f"PartyName '{desired_party_name}' not found in the party collection.")