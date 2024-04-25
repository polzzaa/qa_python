import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.mark.parametrize('name', ['Я', 'Мы', 'Гарри Поттерррррррррррррррррррррррррррр', 'Девушка с татуировкой драконаааааааааааа'])
    def test_add_new_book_in_range(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre_add_genre(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'

    def test_get_book_genre_by_name(self, collection):
        assert collection.get_book_genre('Белоснежка') == 'Мультфильмы'

    def test_get_books_with_specific_genre_list_of_books(self, collection):
        assert collection.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер']

    def test_get_books_genre(self, collection):
        assert len(collection.get_books_genre()) == 5

    def test_get_books_for_children(self, collection):
        assert collection.get_books_with_specific_genre('Ужасы') and collection.get_books_with_specific_genre('Детективы') not in collection.get_books_for_children()

    def test_add_book_in_favorites_add_two_books(self, collection):
        collection.add_book_in_favorites('Гарри Поттер')
        collection.add_book_in_favorites('Сияние')
        assert len(collection.get_list_of_favorites_books()) == 2

    def test_delete_book_from_favorites_by_name(self, collection):
        collection.add_book_in_favorites('Гарри Поттер')
        collection.delete_book_from_favorites('Гарри Поттер')
        assert 'Гарри Поттер' not in collection.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, collection):
        assert collection.get_list_of_favorites_books() == []









