import httpx

from quote import get_quote_of_the_day


def test_print_error_when_status_code_ge_than_400(respx_mock, capsys):
    respx_mock.get('https://favqs.com/api/qotd') % httpx.Response(404, text='Nothing for you!')
    result = get_quote_of_the_day()
    output = capsys.readouterr().out

    assert result is None
    # fmt: off
    assert output == (
        'Huh, for some reason, we cannot find the quote\n'
        'status code: 404\n'
        'response: Nothing for you!\n'
    )
    # fmt: on


def test_print_error_when_unable_to_connect_to_favqs(respx_mock, capsys):
    respx_mock.get('https://favqs.com/api/qotd').mock(side_effect=httpx.ConnectError('favqs refuses connections!'))
    result = get_quote_of_the_day()
    output = capsys.readouterr().out

    assert result is None
    # fmt: off
    assert output == (
        'unable to get quote, reason:\n'
        'favqs refuses connections!\n'
    )
    # fmt: on


def test_returns_quote_data_when_calling_api(respx_mock):
    fake_response = {
        'qotd_date': '2022-08-10T00:00:00.000+00:00',
        'quote': {
            'author': 'David Deida',
            'author_permalink': 'david-deida',
            'body': 'Chronic dissatisfaction is how you sense that you ' 'are living a lie.',
            'dialogue': False,
            'downvotes_count': 0,
            'favorites_count': 1,
            'id': 63585,
            'private': False,
            'tags': ['life'],
            'upvotes_count': 0,
            'url': 'https://favqs.com/quotes/david-deida/63585-chronic-dissa-',
        },
    }

    respx_mock.get('https://favqs.com/api/qotd') % httpx.Response(200, json=fake_response)
    result = get_quote_of_the_day()

    assert result == {
        'author': fake_response['quote']['author'],
        'body': fake_response['quote']['body'],
        'tags': fake_response['quote']['tags'],
        'url': fake_response['quote']['url'],
    }
