import importlib
import sys
from os.path import dirname, basename, isfile, join
import glob
from jsonschemacodegen import python as pygen
import schema_defs

def main(args):
    generator = pygen.GeneratorFromSchema(args[0])
    for module in schema_defs.__all__:
        mod = getattr(schema_defs, module)
        getattr(mod, "gen_schema")(generator)

if __name__ == '__main__':
    main(sys.argv[1:])