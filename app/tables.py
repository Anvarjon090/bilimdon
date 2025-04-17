from piccolo.table import Table
from piccolo.columns import Varchar, Integer

class Book(Table):
    title = Varchar()
    year = Integer()
