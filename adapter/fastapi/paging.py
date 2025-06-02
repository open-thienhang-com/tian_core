from typing import List


def paginate(items: List[str], size_page: int, offset: int) -> List[str]:
    """
    Return a paginated slice of the list and the total number of items.
    Handles invalid size_page, offset, and edge cases.
    """
    total = len(items)

    if size_page <= 0:
        return [], total
    if size_page > total:
        size_page = total
    if offset < 0:
        offset = 0
    if offset >= total:
        return [], total

    # Slice the list based on offset and size_page
    page_items = items[offset : offset + size_page]

    return page_items
