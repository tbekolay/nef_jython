
from ca.nengo.math.impl import AbstractFunction


# keep the functions outside of the class, since they can't be serialized in the
#  current version of Jython

transientFunctions={}

class PythonFunction(AbstractFunction):
    serialVersionUID=1
    def __init__(self,func,dimensions=1,time=False):
        AbstractFunction.__init__(self,dimensions)
        transientFunctions[self]=func
        self.time=time
    def map(self,x):
        if self in transientFunctions:
            if self.time: x=x[0]
            return transientFunctions[self](x)        
        else:
            raise Exception('Python Functions are not kept when saving/loading networks')

