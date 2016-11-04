from fuzzywuzzy import process


def test_process_warning(capsys):
    """Check that a string reduced to 0 by processor logs a warning to stderr"""

    query = ':::::::'
    choices = [':::::::']

    _ = process.extractOne(query, choices)

    out, err = capsys.readouterr()

    outstr = ("WARNING:root:Applied processor reduces "
              "input query to empty string, "
              "all comparisons will have score 0. "
              "[Query: ':::::::']\n")

    assert err == outstr
