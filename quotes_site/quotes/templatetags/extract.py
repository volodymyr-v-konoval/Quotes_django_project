
from django import template

from ..utils import get_cursor

register = template.Library()


def get_author(id_):
    pg_cursor = get_cursor()
    pg_cursor.execute(f"SELECT fullname FROM quotes_author WHERE id = '{id_}'")
    author = pg_cursor.fetchone()
    if author:
        return author[0]
    return "Anonymous"

register.filter('author', get_author)
