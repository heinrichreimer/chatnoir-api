from chatnoir.api.v1 import search_page, search_phrases_page

api_key: str = input("API key: ")

top_5_results_search = search_page(
    api_key, "python library",
    start=0,
    size=5
)
print(top_5_results_search)

top_5_results_search_phrases = search_phrases_page(
    api_key, "python library",
    minimal=False,
    start=0,
    size=5
)
print(top_5_results_search_phrases)

top_5_results_search_phrases_minimal = search_phrases_page(
    api_key, "python library",
    minimal=True,
    start=0,
    size=5
)
print(top_5_results_search_phrases_minimal)
