from uuid import UUID

from chatnoir_api import html_contents, Index, ShortUUID

contents = html_contents(
    "clueweb09-en0051-90-00849",
    Index.ClueWeb09,
)
print(contents)

plain_contents = html_contents(
    "clueweb09-en0051-90-00849",
    Index.ClueWeb09,
    plain=True,
)
print(plain_contents)

contents = html_contents(
    UUID("e635baa8-7341-596a-b3cf-b33c05954361"),
    Index.CommonCrawl1511,
)
print(contents)

plain_contents = html_contents(
    UUID("e635baa8-7341-596a-b3cf-b33c05954361"),
    Index.CommonCrawl1511,
    plain=True,
)
print(plain_contents)

contents = html_contents(
    ShortUUID("6svePe3PXteDeGPk1XqTLA"),
    Index.ClueWeb22,
    base_url="https://chatnoir.web.webis.de/"
)
print(contents)

plain_contents = html_contents(
    ShortUUID("6svePe3PXteDeGPk1XqTLA"),
    Index.ClueWeb22,
    plain=True,
    base_url="https://chatnoir.web.webis.de/"
)
print(plain_contents)
