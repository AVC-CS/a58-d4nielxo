import pytest
import re

def regex_test(expected, content):
    pos = 0
    for token in expected:
        res = re.search(token, content[pos:])
        if res is None:
            assert False, f'Expect: {token}'
        pos += res.start() + 1

@pytest.mark.T1
def test_main_1():
    # data1.txt: 3 students: Alice 90 80, Bob 70 60, Carol 100 95
    # Alice sum=170 avg=85, Bob sum=130 avg=65, Carol sum=195 avg=97.5
    content = open('result1.txt').read()
    print(content)
    regex_test([
        r'Total\s+3\s+students',
        r'Student Name:\s*Alice.*score1:\s*90.*score2:\s*80.*Sum:\s*170.*Avg:\s*85',
        r'Student Name:\s*Bob.*score1:\s*70.*score2:\s*60.*Sum:\s*130.*Avg:\s*65',
        r'Student Name:\s*Carol.*score1:\s*100.*score2:\s*95.*Sum:\s*195.*Avg:\s*97\.5',
    ], content)

@pytest.mark.T2
def test_main_2():
    # data2.txt: 5 students: Kathy 100 90, Mary 100 100, Hammond 100 90, Maxine 90 90, Heather 100 90
    content = open('result2.txt').read()
    print(content)
    regex_test([
        r'Total\s+5\s+students',
        r'Student Name:\s*Kathy.*score1:\s*100.*score2:\s*90.*Sum:\s*190.*Avg:\s*95',
        r'Student Name:\s*Mary.*score1:\s*100.*score2:\s*100.*Sum:\s*200.*Avg:\s*100',
        r'Student Name:\s*Hammond.*score1:\s*100.*score2:\s*90.*Sum:\s*190.*Avg:\s*95',
    ], content)

@pytest.mark.T3
def test_main_3():
    # data3.txt: 2 students: Jim 85 75, Kate 95 90
    content = open('result3.txt').read()
    print(content)
    regex_test([
        r'Total\s+2\s+students',
        r'Student Name:\s*Jim.*score1:\s*85.*score2:\s*75.*Sum:\s*160.*Avg:\s*80',
        r'Student Name:\s*Kate.*score1:\s*95.*score2:\s*90.*Sum:\s*185.*Avg:\s*92\.5',
    ], content)

@pytest.mark.T4
def test_main_4():
    # data4.txt: 4 students: Tom 60 70, Lisa 80 85, Dave 75 90, Emma 100 100
    content = open('result4.txt').read()
    print(content)
    regex_test([
        r'Total\s+4\s+students',
        r'Student Name:\s*Tom.*score1:\s*60.*score2:\s*70.*Sum:\s*130.*Avg:\s*65',
        r'Student Name:\s*Lisa.*score1:\s*80.*score2:\s*85.*Sum:\s*165.*Avg:\s*82\.5',
        r'Student Name:\s*Emma.*score1:\s*100.*score2:\s*100.*Sum:\s*200.*Avg:\s*100',
    ], content)
