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
    content = open('result1.txt').read()
    print(content)
    regex_test([
        r'Alice', r'170', r'85',
        r'Bob', r'130', r'65',
        r'Carol', r'195', r'97\.5',
    ], content)

@pytest.mark.T2
def test_main_2():
    # data2.txt: 5 students: Kathy 100 90, Mary 100 100, Hammond 100 90, Maxine 90 90, Heather 100 90
    content = open('result2.txt').read()
    print(content)
    regex_test([
        r'Kathy', r'190', r'95',
        r'Mary', r'200', r'100',
        r'Hammond', r'190', r'95',
    ], content)

@pytest.mark.T3
def test_main_3():
    # data3.txt: 2 students: Jim 85 75, Kate 95 90
    content = open('result3.txt').read()
    print(content)
    regex_test([
        r'Jim', r'160', r'80',
        r'Kate', r'185', r'92\.5',
    ], content)

@pytest.mark.T4
def test_main_4():
    # data4.txt: 4 students: Tom 60 70, Lisa 80 85, Dave 75 90, Emma 100 100
    content = open('result4.txt').read()
    print(content)
    regex_test([
        r'Tom', r'130', r'65',
        r'Lisa', r'165', r'82\.5',
        r'Dave', r'165', r'82\.5',
        r'Emma', r'200', r'100',
    ], content)
