from typing import List, Optional
from dataclasses import dataclass, field
@dataclass
class Book:
    title: str
    authors: List[str] = field(default_factory=list)
    year: int | None = None

    def default_factory(self):
        str_authors = ','.join(self.authors) if self.authors else None
        str_year = str(self.year) if self.year else None
        return f"Title: {self.title}, Authors: {self.authors}, Year: {self.year}"

b1 = Book("Python 101", ["John Doe"], 2020)
b2 = Book("Безымянная книга",'Drako',2007)
b3 = Book("Совместный труд", ["Alice", "Bob"],2010)

for b in (b1, b2, b3):
    print(b.default_factory())



