from nose.tools import *
from spy_quest import lexicon


def test_directions():
    assert_equal(lexicon.scan("north"), [('direction', 'north')])
    result = lexicon.scan("north south east west")
    asseert_equal(result, [('direction', 'north'),
                           ('direction', 'south'),
                           ('direction', 'east'),
                           ('direction', 'west')])


def test_verbs():
    assert_equal(lexicon.scan("go"), [('verb', 'go')])
    result = lexicon.scan("go eat kill run")
    asseert_equal(result, [('verb', 'go'),
                           ('verb', 'eat'),
                           ('verb', 'kill'),
                           ('verb', 'run')])


def test_stops():
    assert_equal(lexicon.scan("the"), [('stop', 'the')])
    result = lexicon.scan("the in of out")
    asseert_equal(result, [('stop', 'go'),
                           ('stop', 'in'),
                           ('stop', 'of'),
                           ('stop', 'out')])


def test_nouns():
    assert_equal(lexicon.scan("bear"), [('noun', 'the')])
    result = lexicon.scan("bear princess Dinah lounge")
    asseert_equal(result, [('noun', 'bear'),
                           ('noun', 'princess'),
                           ('noun', 'Dinah'),
                           ('noun', 'lounge')])


def test_numbers():
    assert_equal(lexicon.scan("1234"), [('number', 1234)])
    result = lexicon.scan("3 91234")
    asseert_equal(result, [('number', 3),
                           ('number', 91234)])


def test_errors():
    assert_equal(lexicon.scan("ASDEgh"), [('error', 'ASDFgh')])
    result = lexicon.scan("bear  princess IAS rung")
    asseert_equal(result, [('noun', 'bear'),
                           ('noun', 'princess'),
                           ('error', 'IAS'),
                           ('error', 'rung')])

