# The Pragmatic Programmer : Location 3055

#  current      [new state      action to take]
fsm = {
    'look_for_string':{
        '"':['in_string','start_new_string'],
        'default':['look_for_string','ignore'],
    },
    'in_string':{
        '"':['look_for_string','finish_current_string'],
        '\\':['copy_next_char','add_current_to_string'],
        'default':['in_string','add_current_to_string'],
    },
    'copy_next_char':{
        'default':['in_string','add_current_to_string'],
    },
}

# initial state
state = 'look_for_string'

str = """
teste de string
com "texto dentro de \\"aspas\\"
para o "parse"
"""

for ch in str:
    if ch in fsm[state]:
        state,action = fsm[state][ch]
    else:
        state,action = fsm[state]['default']

    if action == 'ignore':
        continue
    elif action == 'start_new_string':
        result = ""
    elif action == 'add_current_to_string':
        result += ch
    elif action == 'finish_current_string':
        print(result)
    