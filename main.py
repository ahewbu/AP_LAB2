from script1 import run1
from script2 import run2
from script3 import run3
from script4 import get_next_element

if __name__ == '__main__':
    run1('responses', 'annotation1.csv')
    run2('datasetcopy1', 'annotation.csv')
    run3('annotation.csv', 'datasetcopy2')
    
    for item in get_next_element('1'):
        print(item)