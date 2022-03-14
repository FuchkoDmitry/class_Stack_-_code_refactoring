import pytest
from main import balance


test_values = [('(((([{}]))))', 'Сбалансированно'),
               ('[([])((([[[]]])))]{()}', 'Сбалансированно'),
               ('{{[()]}}', 'Сбалансированно'),
               ('}{}', 'Несбалансированно'),
               ('{{[(])]}}', 'Несбалансированно'),
               ('[[{())}]', 'Несбалансированно')
               ]


@pytest.mark.parametrize('brackets_string, result', test_values)
def test_balance(brackets_string, result):
    assert balance(brackets_string) == result
