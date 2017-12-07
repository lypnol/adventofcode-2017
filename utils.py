from shutil import which

def is_tool(name):
    return which(name) is not None

def tool_for_lang(lang):
    if lang == 'py':
        return 'python'
    elif lang == 'js':
        return 'node'
    elif lang == 'go':
        return 'go'
    elif lang == 'rb':
        return 'ruby'
    return lang