from shutil import which

def is_tool(name):
    return which(name) is not None
