import typer
import ssg.parsers 
import sys


from ssg.site import Site

def main(source = "content",dest = "dist"):
    config = {'source': source, 'dest': dest, 'parsers': [ssg.parsers.ResourceParser()]}
    Site(**config).build()


@staticmethod
def error(message):
    sys.stderr.write("\x1b[1;31m{}\n").format(message)




#if __name__ == "__main__":
typer.run(main)
