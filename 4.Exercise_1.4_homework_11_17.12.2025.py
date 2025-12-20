from enum import Enum
class Environment(Enum):
    DEV = "https://dev.example.com"
    STAGE = "https://stage.example.com"
    PROD = "https://example.com"

def get_base_url(env):
    return env.value
print(get_base_url(Environment.DEV))
print(get_base_url(Environment.PROD))







