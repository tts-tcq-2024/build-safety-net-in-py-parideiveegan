def check_null_string(name):
    if not name :
        return ""
    return name
    
def pad_with_zero(soundex):
    
    return (soundex.ljust(4, '0'))

def remove_invalid_char(name):
    # to handel invalid characters ex. " !*,Pa"
    name = name.upper()
    soundex_input = ""
    for char in name[:]:
        if 65<=ord(char) <=90:
            soundex_input += char
            
    return (check_null_string(soundex_input))

def remove_consecutive_dupilcates(name):
    #removing consecutive ex. PPRRai
    resized_input = name[0]
    for char in name[1:]:
        if char != resized_input[-1]:
            resized_input += char
    return (resized_input)        

# retruns empty string if char is eqal to H,Y,W 
def check_char_HYW(char,name,vowels,index,mapping):
    previous_char_value = mapping.get(name[index-1],'0')
    next_char_value = mapping.get(name[index+1],'0')
    if char in vowels:
        if previous_char_value == next_char_value:
            return " "
        return ""
    return char
# Remove same latters seprated by H,Y,W    
def remove_same_letters_sepratedbyHYW(name):
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    vowels = ["H","Y", "W"]
    char = ""
    refactored_string = name[0]
    index = 1
    while index <= len(name)-2:
        char = name[index]
        char = check_char_HYW(char,name,vowels,index,mapping)
        refactored_string +=char
        if char == " " :
            index+=1
        index+=1
    refactored_string += name[-1]
    return refactored_string
    
def check_char_value(char,name,mapping,index):
    char_value = mapping.get(name[index],'0')
    previous_char_value = mapping.get(name[index-1],'0')
    if char_value == previous_char_value:
        return ''
    return char_value
    
def get_sondexcode(name):
    #get the soundex code after the refactor
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    
    soundex = name[0]
    index = 1
    char = ''
    while index <= len(name)-1:
        char = name[index]
        soundex += check_char_value(char,name,mapping,index)
        index +=1
        if len(soundex) > 3:
            break
        
    #pad with zero if nessecary     
    soundex = pad_with_zero(soundex)
    return (soundex)

def generate_soundex(name):
    if not name:
        return ""
    name = remove_invalid_char(name)
    
    if not (name):
        return pad_with_zero(name)
    name = remove_consecutive_dupilcates(name)
    name = remove_same_letters_sepratedbyHYW(name)
    return (get_sondexcode(name))
