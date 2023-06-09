


# Takes a single string(supposed to be made up of sentences)
# and returns them as a list of strings, each within the length limit
# specified with the parameter
def split_into_lines(text, limit):
    line_list = []
    split_text = text.split()
    line = ''
    for i, word in enumerate(split_text):
        if len(line + word)+1 > limit:
            line_list.append(line)
            split_text = split_text[len(line)+1:]
            line = word
        else:
            line += ' '*int(i!=0) + word
    if len(line) > 0:
        line_list.append(line)
    return line_list

    
# Takes a list of strings and gives each a unique line
# while surrounding them with certain strings
def return_format_lines(line_list, lside, rside, ljust_amount):
    text = ''''''
    if len(line_list) > 0:
        for line in line_list:
            if line == line_list[-1]:
                text += lside+line.ljust(ljust_amount)+rside
            else:
                text += lside+line.ljust(ljust_amount)+rside+'\n'
    else:
        if text == '':
            text = lside+''.ljust(ljust_amount)+rside
    return text


# Returns a string that has been split into lines and boxed.
def box_message(message, width=50):
    return f"""╒{'═'*(width-2)}╕
{return_format_lines(split_into_lines(message, width-4), f"│ ", f" │", width-4)}
╘{'═'*(width-2)}╛"""


# Returns a string that has been split into lines and boxed.
# Takes a list of strings, one for each line
# Requires all strings in message_list to be shorter than width.
def box_messages(message_list, width=50):
    return f"""╒{'═'*(width-2)}╕
{return_format_lines(message_list, f"│ ", f" │", width-4)}
╘{'═'*(width-2)}╛"""
