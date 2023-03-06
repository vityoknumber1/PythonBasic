#Формування тегів
string_for_hash = input("Введіть текст для генерування хеш-коду: ")

def hash_tag_creator(string_for_hash):

    t = str.title(string_for_hash)
    t1 = t.replace(" ", "").replace("\"", "").replace("\'", "")

    try:
        if len(string_for_hash) == 0 or string_for_hash.isspace() == True or len(t1) == 0:
            raise Exception("exception")
        p = '\"' + '#' + t1 + '\"'
        if len(p) > 140:
            return False
        return p
    except Exception as e:
        print(e)

if hash_tag_creator(string_for_hash) is not None:
    print("Хеш-код: ", hash_tag_creator(string_for_hash))