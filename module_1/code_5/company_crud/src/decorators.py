from src.utils import clear,pause,title

def screen(screen_msg):
    def decorate(func):
        def package(*args, **kwargs):
            clear()
            title(screen_msg)
            return func(*args, **kwargs)
        return package
    return decorate