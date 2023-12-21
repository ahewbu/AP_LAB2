from csv_script import run1
from copy_script import run2
from randomname_script import run3
from get_next_script import get_next_element

if __name__ == '__main__':
    run1('annotation1.csv')
    run2('datacopy1', 'annotation.csv')
    run3('datacopy2', 'annotation.csv')
    
    for item in get_next_element('1'):
        print(item)