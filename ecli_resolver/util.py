from werkzeug.routing import BaseConverter
#from collections import namedtuple
from dataclasses import dataclass

#ECLI = namedtuple('ECLI',['ecli','cc','court','year','number'])

@dataclass
class ECLIItem:
    """Class for working with ECLI's"""
    ecli : str
    cc : str
    court : str
    year : int
    number : str

    def __str__(self):
        return f"ECLI:{self.cc}:{self.court}:{self.year}:{self.number}"

class ECLIConverter(BaseConverter):

    def to_python(self, value):
        values = value.split(':')
        ecli = ECLIItem(*values)
        return ecli

    def to_url(self, ecli):
        return ':'.join(BaseConverter.to_url(value)
                        for value in list(ecli))


class NoResolverError(Exception):
    pass
