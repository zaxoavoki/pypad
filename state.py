from config import CONFIG


class State:
    # TODO: Use instance properties
    filename = CONFIG['DEFAULT_NAME']

    font_family = CONFIG['DEFAULT_FONT_FAMILY']
    font_size = CONFIG['DEFAULT_FONT_SIZE']

    background_color = CONFIG['DEFAULT_BACKGROUND_COLOR']
    foreground_color = CONFIG['DEFAULT_FOREGROUND_COLOR']
    linenumbering_color = CONFIG['DEFAULT_LINENUMBERINGAREA_BACKGROUND_COLOR']

    show_status_bar = True
    is_modified = False
    is_saved = False

    find_position = CONFIG['DEFAULT_START_POSITION']
    find_word = False
    find_word_regex_counter = 0

    encrypt_method = 'AES'
    generated_key_filename = False
    generated_key = False
