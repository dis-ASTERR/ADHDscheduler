from pymongo.operations import SearchIndexModel


def create_index(collection, index_name):
    "creates a new index from given collection"
    search_index_model = SearchIndexModel(
        definition={
            "mappings": {
                "dynamic": True
            },
        },
        name=index_name,
    )

    result = collection.create_search_index(model=search_index_model)
    print('Created index!')
    print(result)
    


def view_indexes(collection):
    "views all current indexes in given collection"
    cursor = collection.list_search_indexes()
    for index in cursor:
        print(index)
    return cursor

def edit_index(collection, index_name:str, new_definition):
    "edits a given search index to a given new definition"

    collection.update_search_index(index_name, new_definition)

def delete_index(collection, index_name:str):
    "deletes a given index from given collection"
    collection.drop_search_index(index_name)
