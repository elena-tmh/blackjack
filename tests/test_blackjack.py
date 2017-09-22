import pytest

from blackjack import Card, Deck


def test_cards():
    pass


def test_deck():
    pass


def test_card_has_suit():
    card = Card('diamond', 2)
    assert hasattr(card, 'suit')


def test_card_has_valid_suit():
    with pytest.raises(ValueError):
        Card('robotrics', 2)

    c = Card('spade', 2)
    assert c.suit == 'spade'


def test_card_has_a_value():
    king_of_spades = Card('spade', 'K')
    queen_of_spades = Card('spade', 'Q')

    assert king_of_spades.value == 'K'
    assert queen_of_spades.value == 'Q'


def test_add_card():
    assert 5 == Card('spade', 2) + Card('spade', 3)
    assert 13 == Card('spade', 'K') + Card('spade', 3)


def test_compare():
    assert True == (Card('spade', 'Q') == Card('spade', 'J'))


def test_greater_than():
    assert True == (Card('spade', 'Q') > Card('spade', 3))

def test_init_deck():
    deck = Deck()

    #assert deck.number_of_cards == 52, not needed as it is doubled, due to the lengght
    assert len(deck.cards) == 52

def test_shuffle_deck():

    deck_a = Deck() # instance of deck
    deck_b = Deck()

    for c_a, c_b in zip(deck_a.cards, deck_b.cards):
        assert c_a.value == c_b.value

    # ok, the decks are identical
    # now let's shuffle them

    deck_b.shuffle()

    randomness = []

    for c_a, c_b in zip(deck_a.cards, deck_b.cards):
        randomness.append(c_a.value != c_b.value)

    assert any(randomness)

def deal_hands():
    pass

def test_proper_rep():
    assert "A of spades" == repr(Card("spade", "A"))