def input_to_dictionary(input, skip=[]):
    """Method to convert Graphene inputs into dictionary"""
    dictionary = {}
    for key in input:
        if key in skip:
            continue
        # Convert GraphQL global id to database id
        if key[-2:] == 'id':
            input[key] = from_global_id(input[key])[1]
        dictionary[key] = input[key]
    return dictionary