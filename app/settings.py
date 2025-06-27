
from decouple import config,UndefinedValueError


try:
    OPENAI_API_KEY = config('OPENAI_API_KEY')
except UndefinedValueError:
    raise RuntimeError('Missing environment variable: OPENAI_API_KEY')

PERSIST_DIRECTORY = config('PERSIST_DIRECTORY', 'vector-db')
