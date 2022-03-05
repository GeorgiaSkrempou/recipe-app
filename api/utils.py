def list_to_string(my_list, my_key):
    return ",".join(my_list[my_key])

def string_to_list(my_string, my_key):
    return my_string[my_key].split(",")
