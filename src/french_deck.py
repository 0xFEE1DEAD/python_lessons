"""
Колода, демонстрация "магических" методов:
    __len__
    __getitem__

Можно узнать длину::

    >>> deck = FrenchDeck()
    >>> len(deck)
    52

Получаем элемент благодаря __getitem__::

    >>> deck[0]
    Card(rank='2', suit='spades')
    >>> deck[-1]
    Card(rank='A', suit='hearts')

Можно пользоваться встроенными функциями из библиотеки python:

    >>> from random import choice
    >>> choice(deck) # doctest: +ELLIPSIS
    Card(rank='...', suit='...')

Допускается итерирование благодаря __getitem__::

    >>> for card in deck: # doctest: +ELLIPSIS
    ...     print(card)
    Card(rank='2', suit='spades')
    Card(rank='2', suit='diamonds')
    Card(rank='2', suit='clubs')
    ...

Будет работать оператор in, но с полным перебором::

    >>> Card('Q', 'hearts') in deck
    True
    >>> Card('#', 'beasts') in deck
    False
"""

from dataclasses import dataclass


# Автор предлагает использовать collections.namedtuple
# Но мне нравится больше dataclass (более явный, эффективнее по памяти)
@dataclass(frozen=True)
class Card:
    rank: str
    suit: str


class FrenchDeck:
    ranks = [str(r) for r in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self) -> int:
        return len(self._cards)

    def __getitem__(self, position: int | slice) -> Card | list[Card]:
        return self._cards[position]
