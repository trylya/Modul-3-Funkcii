calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if i.lower() in  string:
         return True
        if i.lower() in list_to_search:
         return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN'])) #Urban~urBan
print(is_contains('cycle', ['recycling', 'cyclic'])) #No matches
print(calls)
