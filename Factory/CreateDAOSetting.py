from Factory.CreatorDAO import CreatorDAO


def CreateDAO(creator: CreatorDAO, type_db: str):
    return creator.operation_create_object(type_db)
