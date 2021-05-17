command = {'>':'p=(p+1)%69420',
           '<':'p=(p+69419)%69420',
           '[':'while c[p]:',
           ']':'pass',
           '(':'if c[p]:',
           ')':'pass',
           '+':'c[p]+=c[p+1]or 1',
           '-':'c[p]-=c[p+1]or 1',
           '*':'c[p]*=c[p+1]or 2',
           '/':'c[p]/=c[p+1]or 2',
           '.':'sys.stdout.write(chr(abs(c[p])%sys.maxunicode))',
           ',':'c[p]=ord(sys.stdin.read(1)or"\\0")',
           ':':'sys.stdout.write(str(c[p]))',
           ';':'c[p]=int(sys.stdin.readline())',
           '%':'c[p]%=c[p+1]or 1',
           '_':'c[p]=int(c[p])',
           '#':'sys.stdout.write(str(p)+"\\n"+" ".join("{}:{}".format(n,c[n]) for n in range(69420)))'
           }
import sys
from io import StringIO
def run(text):
    f = open('gener.py', 'w+')
    f.write('import sys\nc=[0]*69420\np=0\n')
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
    f.write(' '*s+'pass')
if __name__ == '__main__':
    run(input())
import gener
