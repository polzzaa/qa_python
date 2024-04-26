import pytest

from main import BooksCollector
@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture
def collection(collector):
    collector.books_genre = {'Гарри Поттер':'Фантастика', 'Сияние':'Ужасы', 'Девушка с татуировкой дракона':'Детективы','Белоснежка':'Мультфильмы', '12 стульев':'Комедии' }
    return collector