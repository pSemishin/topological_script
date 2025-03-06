from typing import List

import pytest

from topological_script import bonds_parser


@pytest.mark.parametrize(
    "script, expected_result",
    [
        ("(H)1(O)1(H)1", [(0, 1), (1, 2)]),
        (
            "(A)2[(A)2[(A)2](A)2](A)2",
            [(0, 1), (1, 2), (1, 8), (2, 3), (3, 4), (3, 6), (4, 5), (6, 7), (8, 9)],
        ),
        (
            "(Na)1(C0)1[(O)1]((C)1([(H)1])2)3(O)1(H)1",
            [
                (0, 1),
                (1, 2),
                (1, 3),
                (3, 4),
                (3, 5),
                (3, 6),
                (6, 7),
                (6, 8),
                (6, 9),
                (9, 10),
                (9, 11),
                (9, 12),
                (12, 13),
            ],
        ),
        ("(C)1{1}(C)4(C)1{1}", [(0, 1), (0, 5), (1, 2), (2, 3), (3, 4), (4, 5)]),
        (
            "(C)1{1}(C)4(C)1{1}[(N)1(C)1[(O)1](C)1[(O)1](O)1(H)1]",
            [
                (0, 1),
                (0, 5),
                (1, 2),
                (2, 3),
                (3, 4),
                (4, 5),
                (5, 6),
                (6, 7),
                (7, 8),
                (7, 9),
                (9, 10),
                (9, 11),
                (11, 12),
            ],
        ),
        (
            "(C)1{1}(C)4(C)1{1}(C)1{2}(C)2[(C)1{3}(C)4(C)1{3}](C)2(C)1{2}",
            [
                (0, 1),
                (0, 5),
                (1, 2),
                (2, 3),
                (3, 4),
                (4, 5),
                (5, 6),
                (6, 7),
                (6, 17),
                (7, 8),
                (8, 9),
                (8, 15),
                (9, 10),
                (9, 14),
                (10, 11),
                (11, 12),
                (12, 13),
                (13, 14),
                (15, 16),
                (16, 17),
            ],
        ),
        (
            "(C)1{1}[(O)1[(O)1](O)1]((C)1[(O)1[(O)1](O)1])4(C)1{1}[(O)1[(O)1](O)1]",
            [
                (0, 1),
                (0, 4),
                (0, 20),
                (1, 2),
                (1, 3),
                (4, 5),
                (4, 8),
                (5, 6),
                (5, 7),
                (8, 9),
                (8, 12),
                (9, 10),
                (9, 11),
                (12, 13),
                (12, 16),
                (13, 14),
                (13, 15),
                (16, 17),
                (16, 20),
                (17, 18),
                (17, 19),
                (20, 21),
                (21, 22),
                (21, 23),
            ],
        ),
    ],
)
def test_bonds_parser(script: str, expected_result: List[str]) -> None:
    assert sorted(bonds_parser(script)) == sorted(expected_result)
