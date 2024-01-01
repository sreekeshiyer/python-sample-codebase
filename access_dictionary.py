# Issue of trying to access a key in a dictionary that doesn't exist.
def access_dictionary_key(key):
    my_dict = {'name': 'John', 'age': 30}
    try:
        return my_dict[key]
    except KeyError:
        return f"Error: Key '{key}' not found in the dictionary!"

print(access_dictionary_key('address'))
