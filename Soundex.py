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

def convert_to_soundex(name):
    soundex = name[0].upper()
    prev_char = ''
    
    for char in name[1:]:        
        soundex += get_soundex_code(char,prev_char)
        prev_char = soundex [-1]
        if len(soundex) > 3:
            break
   
    # Pad with zeros if necessary
    soundex = soundex.ljust(4, '0')
    return (soundex)

def generate_soundex(name):
    if not name:
        return ""

    return (convert_to_soundex(name))
