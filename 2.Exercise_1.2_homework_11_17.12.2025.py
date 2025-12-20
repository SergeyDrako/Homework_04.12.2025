PAGES = []
def register_page():
    def decorator(cls):
        PAGES.append(cls)
        return cls
    return decorator

@register_page()
class LoginPage:
    pass

@register_page()
class DashboardPage:
    pass
print([cls.__name__ for cls in PAGES])
