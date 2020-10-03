import ankify
import inspect

def test_parse_notes():
    notes = inspect.cleandoc("""
    # Test Notes
    1. _Test Note 1_
     * answer 1 item 1
    1. _Test Note 2_
     * answer 2 item 1
     * answer 2 item 2
    """)

    assert ankify.parse_notes(notes) == [
            {"title": "Test Note 1",
             "body": " * answer 1 item 1"},
            {"title": "Test Note 2",
             "body": " * answer 2 item 1 * answer 2 item 2"}
    ]

