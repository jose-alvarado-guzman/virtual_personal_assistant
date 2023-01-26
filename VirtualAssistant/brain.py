"Module use to determine the task to perform"
import re
from typing import List, Optional
from .dialect import Dialect
from .define_subject import get_definition

class Assistant():

    def __init__(self, name : str, mode : Optional[str] = 'speech'):
        self.name = name
        self.mode = mode
        self.dialect = Dialect(name)

    def get_response(self, query: str) -> str:
        query_type = 'dialect'
        define_regex = re.compile(r'\bdefine\b|\bwho is\b|\bwhat is\b')
        medical_regex = re.compile(r'\bbiomedical information\b')
        if define_regex.search(query):
            response = get_definition(query)
        elif medical_regex.search(query):
            response = 'Looking for Biomedical Concept'
        else:
            response = self.dialect.get_response(query)
        return response
