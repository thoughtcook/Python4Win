# Filename:    odbchelper.py
# Description: The very first program of Python
# Date:        1/2/2013
# Version:     v0.1
# log:         Init
def buildConnectionString(params):
    """Build a connection string from a dictionary of parameters.

       Returns string."""
    return ";\n".join(["%s=%s" % (k, v) for k, v in params.items()])

if __name__== "__main__":
    myParams = {"server":"suse",\
                "database":"master",\
                "uid":"sa",\
                "pwd":"secret"\
                }
    print buildConnectionString(myParams)
