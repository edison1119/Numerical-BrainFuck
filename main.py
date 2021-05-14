command = {'>':'p=(p+1)%69420',
           '<':'p=(p+69419)%69420',
           '[':'while cell[p]:',
           ']':'pass',
           '(':'if cell[p]:',
           ')':'pass',
           '+':'cell[p]+=cell[p+1]or 1',
           '-':'cell[p]-=cell[p+1]or 1',
           '*':'cell[p]*=cell[p+1]or 2',
           '/':'cell[p]/=cell[p+1]or 2',
           '.':'sys.stdout.write(chr(abs(cell[p])))',
           ',':'cell[p]=ord(sys.stdin.read(1)or"\\0")',
           ':':'sys.stdout.write(str(cell[p]))',
           ';':'cell[p]=int(sys.stdin.readline())',
           '%':'cell[p]%=cell[p+1]or 1',
           '_':'cell[p]=int(cell[p])',
           '#':'sys.stdout.write(str(p)+"\\n"+" ".join("{}:{}".format(n,cell[n]) for n in range(69420)))'
           }
import sys
from io import StringIO
def run(text):
    f = open('gener.py', 'w+')
    f.write('import sys\ncell=[0]*69420\np=0\nm')
    if '!' in text:
        sys.stdin=StringIO(text.split('!')[1])
    text = text.split('!')[0]
    s=0
    for n in text:
        f.write(' '*s+str(command.get(n))+'\n')
        if n in'[(':
            s+=1
        elif n in'])':
            s-=1

if __name__ == '__main__':
    run(input())
import gener
