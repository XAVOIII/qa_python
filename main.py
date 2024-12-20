import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


def test_add_new_book(collector):
    collector.add_new_book('Book One')
    assert 'Book One' in collector.get_books_genre()


def test_add_new_book_exceeding_length(collector):
    collector.add_new_book('B' * 41)
    assert 'B' * 41 not in collector.get_books_genre()


def test_set_book_genre(collector):
    collector.add_new_book('Book Two')
    collector.set_book_genre('Book Two', 'Фантастика')
    assert collector.get_book_genre('Book Two') == 'Фантастика'


def test_set_book_genre_invalid(collector):
    collector.add_new_book('Book Three')
    collector.set_book_genre('Book Three', 'Неизвестный Жанр')
    assert collector.get_book_genre('Book Three') is None


def test_get_books_with_specific_genre(collector):
    collector.add_new_book('Book Four')
    collector.set_book_genre('Book Four', 'Комедии')
    collector.add_new_book('Book Five')
    collector.set_book_genre('Book Five', 'Фантастика')
    books = collector.get_books_with_specific_genre('Комедии')
    assert books == ['Book Four']


def test_get_books_for_children(collector):
    collector.add_new_book('Book Six')
    collector.set_book_genre('Book Six', 'Комедии')
    collector.add_new_book('Book Seven')
    collector.set_book_genre('Book Seven', 'Ужасы')
    books = collector.get_books_for_children()
    assert books == ['Book Six']


def test_add_book_in_favorites(collector):
    collector.add_new_book('Book Eight')
    collector.set_book_genre('Book Eight', 'Фантастика')
    collector.add_book_in_favorites('Book Eight')
    assert 'Book Eight' in collector.get_list_of_favorites_books()


def test_add_book_in_favorites_not_exist(collector):
    collector.add_book_in_favorites('Book Nine')  # Книги не существует
    assert 'Book Nine' not in collector.get_list_of_favorites_books()


def test_delete_book_from_favorites(collector):
    collector.add_new_book('Book Ten')
    collector.set_book_genre('Book Ten', 'Комедии')
    collector.add_book_in_favorites('Book Ten')
    collector.delete_book_from_favorites('Book Ten')
    assert 'Book Ten' not in collector.get_list_of_favorites_books()


def test_get_list_of_favorites_books(collector):
    collector.add_new_book('Book Eleven')
    collector.set_book_genre('Book Eleven', 'Фантастика')
    collector.add_book_in_favorites('Book Eleven')
    assert collector.get_list_of_favorites_books() == ['Book Eleven']


def test_add_duplicate_favorite(collector):
    collector.add_new_book('Book Twelve')
    collector.set_book_genre('Book Twelve', 'Комедии')
    collector.add_book_in_favorites('Book Twelve')
    # Попробуем добавить книгу снова в избранное
    collector.add_book_in_favorites('Book Twelve')
    assert collector.get_list_of_favorites_books() == ['Book Twelve']  # Должно остаться без изменений