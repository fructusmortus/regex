import re 
    # time validation function for 23:59 or 1:59 pattern
def is_valid_time(input):
    pattern = re.compile(r'^\d\d?:\d\d$')
    match = pattern.search(input)
    if match:
        return True
    return False

print(is_valid_time("23:59"))
print(is_valid_time("What time is it now? It is 23:59"))