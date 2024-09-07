def get_soundex_code(c,previous_char_value):    
    c = c.upper()
    mapping = {
        'B': '1', 'F': '1', 'P': '1', 'V': '1',
        'C': '2', 'G': '2', 'J': '2', 'K': '2', 'Q': '2', 'S': '2', 'X': '2', 'Z': '2',
        'D': '3', 'T': '3',
        'L': '4',
        'M': '5', 'N': '5',
        'R': '6'
    }
    value = mapping.get(c, '')
    
    if previous_char_value != value:
        return value
    return ''

def check_null_string(name):
    if not name :
        return ""
    return name
    
def pad_with_zero(soundex):    
    return (soundex.ljust(4, '0'))

def remove_invalid_char(name):
    name = name.upper()
    soundex_input = ""
    for i in name[:]:
        if 65<=ord(i) <=90:
            soundex_input +=i
            
    return (check_null_string(soundex_input))

def get_sondexcode(name):
    
    soundex = name[0].upper()
    prev_char = prev_char = get_soundex_code(soundex,'')
    
    for char in name[1:]:        
        soundex += get_soundex_code(char,prev_char)
        prev_char = soundex [-1]
        if len(soundex) > 3:
            break
    
    #pad with zero if necessary     
    soundex = pad_with_zero(soundex)
    return (soundex)

def generate_soundex(name):
    if not name:
        return ""
    name = remove_invalid_char(name)
    if not (name):
        return pad_with_zero(name)
    
    return (get_sondexcode(name))
