#!  /home/bren/miniconda3/envs/ga/bin/python
# test get_answer decorator
import io
from pdb import set_trace
import sys
sys.path.append('/home/bren/miniconda3/envs/ga/lib/python3.8/site-packages/get_answer_decorator-1.3.0-py3.8.egg')

from get_answer_decorator import get_answer
@get_answer
def answer_yn(answer, answers, default, max_try, **kwargs):
    try:
        answer = answer.upper()
    except Exception as excpt:
        raise excpt
    assert answer in list('YNQ'), f'must be in {list("ynq")} or CR, try again:'
    return answer

def test_yn(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Y'))
    yn = answer_yn('enter', 'ynq', 'Y', max_try=3)
    assert yn == 'Y', 'answer_yn does not respond with "Y"'

@get_answer
def answer_kwarg(answer, answers, default, max_try, **kwargs):
    if 'keyword' not in kwargs:
        print('keyword is required argument')
        return None
    else:
        answer = answer.upper()
        keyword = kwargs['keyword']
    assert answer in list('YNQ'), f'must be in {list("ynq")} or CR, try again:'
    return keyword

def test_kwarg(monkeypatch):
    monkeypatch.setattr('sys.stdin', io.StringIO('Y'))
    ans = answer_kwarg('answer', 'answers', 'default', 3, keyword='foobar')
    assert ans == 'foobar', 'keyword="foobar" required'
