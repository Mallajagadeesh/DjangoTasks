import pymongo

# Staging database connection details
staging_host = '194.195.112.19'
staging_username = 'devops_admin'
staging_password = 'Devops@1234'
staging_database_name = 'Devarapalle'

# Production database connection details
production_host = '13.126.55.93'
production_port = 27017
production_username = 'devops_admin'
production_password = 'Vivij0019ej'
production_database_name = 'Devarapalle_database_2023'

try:
    # Connect to the staging and production databases
    staging_client = pymongo.MongoClient(staging_host, username=staging_username, password=staging_password)
    production_client = pymongo.MongoClient(production_host, port=production_port, username=production_username, password=production_password)

    staging_db = staging_client[staging_database_name]
    production_db = production_client[production_database_name]

    # List all collections in the staging database
    staging_collections = staging_db.list_collection_names()

    # Transfer all collections from staging to production
    for collection_name in staging_collections:
        staging_collection = staging_db[collection_name]
        data_to_transfer = list(staging_collection.find())

        production_collection = production_db[collection_name]

        try:
            production_collection.insert_many(data_to_transfer)
            print(f"Data inserted into {collection_name} in the production database.")
        except Exception as e:
            print(f"Error inserting data into {collection_name}: {str(e)}")

    print(f"All collections from staging have been transferred to production.")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Close the database connections
    staging_client.close()
    production_client.close()







# ##################################this code use for staging data to transfer to production data ###################
#
# import pymongo
#
# # Staging database connection details
# staging_host = '194.195.112.19'
# staging_username = 'devops_admin'
# staging_password = 'Devops@1234'
# staging_database_name = 'Cheedikada'
#
# # Production database connection details
# production_host = '13.126.55.93'
# production_port = 27017
# production_username = 'devops_admin'
# production_password = 'Vivij0019ej'
# production_database_name = 'Cheeikada_database_2023'
#
#
# # Connect to the staging and production databases
# staging_client = pymongo.MongoClient(staging_host, username=staging_username, password=staging_password)
# production_client = pymongo.MongoClient(production_host, port=production_port, username=production_username, password=production_password)
#
# staging_db = staging_client[staging_database_name]
# production_db = production_client[production_database_name]
#
#
# # List all collections in the staging database
# staging_collections = staging_db.list_collection_names()
#
# # Track the total count of documents added
# total_documents_added = 0
#
# # Transfer all collections from staging to production
# for collection_name in staging_collections:
#     # print('hellowold')
#     staging_collection = staging_db[collection_name]
#     data_to_transfer = list(staging_collection.find())
#     # print(data_to_transfer)
#
#     production_collection = production_db[collection_name]
#     result = production_collection.insert_many(data_to_transfer)
#
#     # Count the number of documents added to the production collection
#     total_documents_added += len(result.inserted_ids)
#
# # Close the database connections
# staging_client.close()
# production_client.close()
#
# # print(f"{total_documents_added} documents have been added to the production collection(s).")





# ##################################this code use for staging data to transfer to production data ###################

# import pymongo
#
# # Staging database connection details
# staging_host = '194.195.112.19'
# staging_username = 'devops_admin'
# staging_password = 'Devops@1234'
# staging_database_name = 'Cheedikada'
#
# # Production database connection details
# production_host = '13.126.55.93'
# production_port = 27017
# production_username = 'devops_admin'
# production_password = 'Vivij0019ej'
# production_database_name = 'Cheeikada_database_2023'
#
# # Connect to the staging and production databases
# staging_client = pymongo.MongoClient(staging_host, username=staging_username, password=staging_password)
# production_client = pymongo.MongoClient(production_host, port=production_port, username=production_username, password=production_password)
#
# staging_db = staging_client[staging_database_name]
# production_db = production_client[production_database_name]
#
# # List all collections in the staging database
# staging_collections = staging_db.list_collection_names()
#
# # Transfer all collections from staging to production
# for collection_name in staging_collections:
#     staging_collection = staging_db[collection_name]
#     data_to_transfer = list(staging_collection.find())
#
#     production_collection = production_db[collection_name]
#     print(production_collection)
#     production_collection.insert_many(data_to_transfer)
#
# # Close the database connections
# staging_client.close()
# production_client.close()
#
# print(f"All collections from staging have been transferred to production.")










# import pymongo
#
# # Staging database connection details
# staging_host = '194.195.112.19'
# staging_username = 'devops_admin'
# staging_password = 'Devops@1234'
# staging_database_name = 'Devarapalle'
#
# # Production database connection details
# production_host = '13.126.55.93'
# production_port = 27017
# production_username = 'devops_admin'
# production_password = 'Vivij0019ej'
# production_database_name = '2024_database'
#
# try:
#     # Connect to the staging and production databases
#     staging_client = pymongo.MongoClient(staging_host, username=staging_username, password=staging_password)
#     production_client = pymongo.MongoClient(production_host, port=production_port, username=production_username, password=production_password)
#
#     staging_db = staging_client[staging_database_name]
#     production_db = production_client[production_database_name]
#
#     # List all collections in the staging database
#     staging_collections = staging_db.list_collection_names()
#
#     # Transfer all collections from staging to production
#     for collection_name in staging_collections:
#         staging_collection = staging_db[collection_name]
#         data_to_transfer = list(staging_collection.find())
#
#         production_collection = production_db[collection_name]
#
#         try:
#             production_collection.insert_many(data_to_transfer)
#             print(f"Data inserted into {collection_name} in the production database.")
#         except Exception as e:
#             print(f"Error inserting data into {collection_name}: {str(e)}")
#
#     # Create a new collection in the production database
#     new_collection_name = 'Devarapalle_database_2023'
#     production_db.create_collection(new_collection_name)
#
#     # Verify that the collection has been created
#     if new_collection_name in production_db.list_collection_names():
#         print(f"Collection '{new_collection_name}' created in the production database.")
#     else:
#         print(f"Failed to create collection '{new_collection_name}' in the production database.")
#
#     print(f"All collections from staging have been transferred to production.")
#
# except Exception as e:
#     print(f"An error occurred: {str(e)}")
#
# finally:
#     # Close the database connections
#     staging_client.close()
#     production_client.close()








# ############################################ This code use are collection data transfer staging to production data#######################
#
# import pymongo
#
# # Staging database connection details
# staging_host = '194.195.112.19'
# staging_username = 'devops_admin'
# staging_password = 'Devops@1234'
# staging_database_name = 'Cheedikada'
# staging_collection_name = 'ADVI_AGRAHARAM'
#
# # Production database connection details
# production_host = '13.126.55.93'
# production_port = 27017
# production_username = 'devops_admin'
# production_password = 'Vivij0019ej'
# production_database_name = 'Cheeikada_database_2023'
# production_collection_name = 'Cheeikada'
#
# # Connect to the staging and production databases
# staging_client = pymongo.MongoClient(staging_host, username=staging_username, password=staging_password)
# production_client = pymongo.MongoClient(production_host, port=production_port, username=production_username, password=production_password)
#
# staging_db = staging_client[staging_database_name]
# production_db = production_client[production_database_name]
#
# # Get the data from the staging collection
# staging_collection = staging_db[staging_collection_name]
# data_to_transfer = list(staging_collection.find())
#
# # Transfer the data to the production collection
# production_collection = production_db[production_collection_name]
# production_collection.insert_many(data_to_transfer)
#
# # Close the database connections
# staging_client.close()
# production_client.close()
#
# print(f"Data from staging has been transferred to production.")
#
#
#


