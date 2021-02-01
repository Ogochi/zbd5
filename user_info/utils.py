def input_to_dictionary(input, skip=[]):
    """Method to convert Graphene inputs into dictionary"""
    dictionary = {}
    for key in input:
        if key in skip:
            continue
        
        dictionary[key] = input[key]
    return dictionary