from typing import Type, Union, Set, overload, Literal

from chatnoir_api.lazy import LazyResultSequence
from chatnoir_api.model import Index
from chatnoir_api.model.result import (
    MinimalResult,
    ExplainedMinimalResult,
    Result,
    ExplainedResult,
    Meta,
    ExtendedMeta,
    Results,
)
from chatnoir_api.defaults import (
    DEFAULT_API_KEY,
    DEFAULT_START,
    DEFAULT_SIZE,
    DEFAULT_INDEX,
    DEFAULT_MINIMAL,
    DEFAULT_EXPLAIN,
    DEFAULT_RETRIES,
    DEFAULT_BACKOFF_SECONDS,
    DEFAULT_EXTENDED_META,
)
from chatnoir_api.v1.model import (
    MinimalSearchResponse,
    ExplainedMinimalSearchResponse,
    SearchResponse,
    ExplainedSearchResponse,
    ExtendedMetaMinimalSearchResponse,
    ExplainedExtendedMetaMinimalSearchResponse,
    ExtendedMetaSearchResponse,
    ExplainedExtendedMetaSearchResponse,
    Request,
)
from chatnoir_api.v1.requests import request_page


@overload
def search(
    query: str,
    index: Union[Index, Set[Index]] = ...,
    minimal: Literal[False] = ...,
    explain: Literal[False] = ...,
    extended_meta: Literal[False] = ...,
    page_size: int = ...,
    retries: int = ...,
    backoff_seconds: float = ...,
    api_key: str = ...,
) -> Results[Meta, Result]: ...


@overload
def search(
    query: str,
    index: Union[Index, Set[Index]] = ...,
    minimal: Literal[False] = ...,
    explain: Literal[False] = ...,
    extended_meta: Literal[True] = ...,
    page_size: int = ...,
    retries: int = ...,
    backoff_seconds: float = ...,
    api_key: str = ...,
) -> Results[ExtendedMeta, Result]: ...


@overload
def search(
    query: str,
    index: Union[Index, Set[Index]] = ...,
    minimal: Literal[False] = ...,
    explain: Literal[True] = ...,
    extended_meta: Literal[False] = ...,
    page_size: int = ...,
    retries: int = ...,
    backoff_seconds: float = ...,
    api_key: str = ...,
) -> Results[Meta, ExplainedResult]: ...


@overload
def search(
    query: str,
    index: Union[Index, Set[Index]] = ...,
    minimal: Literal[False] = ...,
    explain: Literal[True] = ...,
    extended_meta: Literal[True] = ...,
    page_size: int = ...,
    retries: int = ...,
    backoff_seconds: float = ...,
    api_key: str = ...,
) -> Results[ExtendedMeta, ExplainedResult]: ...


@overload
def search(
    query: str,
    index: Union[Index, Set[Index]] = ...,
    minimal: Literal[True] = ...,
    explain: Literal[False] = ...,
    extended_meta: Literal[False] = ...,
    page_size: int = ...,
    retries: int = ...,
    backoff_seconds: float = ...,
    api_key: str = ...,
) -> Results[Meta, MinimalResult]: ...


@overload
def search(
    query: str,
    index: Union[Index, Set[Index]] = ...,
    minimal: Literal[True] = ...,
    explain: Literal[False] = ...,
    extended_meta: Literal[True] = ...,
    page_size: int = ...,
    retries: int = ...,
    backoff_seconds: float = ...,
    api_key: str = ...,
) -> Results[ExtendedMeta, MinimalResult]: ...


@overload
def search(
    query: str,
    index: Union[Index, Set[Index]] = ...,
    minimal: Literal[True] = ...,
    explain: Literal[True] = ...,
    extended_meta: Literal[False] = ...,
    page_size: int = ...,
    retries: int = ...,
    backoff_seconds: float = ...,
    api_key: str = ...,
) -> Results[Meta, ExplainedMinimalResult]: ...


@overload
def search(
    query: str,
    index: Union[Index, Set[Index]] = ...,
    minimal: Literal[True] = ...,
    explain: Literal[True] = ...,
    extended_meta: Literal[True] = ...,
    page_size: int = ...,
    retries: int = ...,
    backoff_seconds: float = ...,
    api_key: str = ...,
) -> Results[ExtendedMeta, ExplainedMinimalResult]: ...


@overload
def search(
    query: str,
    index: Union[Index, Set[Index]] = ...,
    minimal: bool = ...,
    explain: bool = ...,
    extended_meta: bool = ...,
    page_size: int = ...,
    retries: int = ...,
    backoff_seconds: float = ...,
    api_key: str = ...,
) -> Results[
    Union[Meta, ExtendedMeta],
    Union[
        MinimalResult,
        ExplainedMinimalResult,
        Result,
        ExplainedResult,
    ],
]: ...


def search(
    query: str,
    index: Union[Index, Set[Index]] = DEFAULT_INDEX,
    minimal: bool = DEFAULT_MINIMAL,
    explain: bool = DEFAULT_EXPLAIN,
    extended_meta: bool = DEFAULT_EXTENDED_META,
    page_size: int = DEFAULT_SIZE,
    retries: int = DEFAULT_RETRIES,
    backoff_seconds: float = DEFAULT_BACKOFF_SECONDS,
    api_key: str = DEFAULT_API_KEY,
) -> Results[
    Union[Meta, ExtendedMeta],
    Union[
        MinimalResult,
        ExplainedMinimalResult,
        Result,
        ExplainedResult,
    ],
]:
    def load_page(start: int, size: int) -> Results[
        Union[Meta, ExtendedMeta],
        Union[
            MinimalResult,
            ExplainedMinimalResult,
            Result,
            ExplainedResult,
        ],
    ]:
        return search_page(
            api_key=api_key,
            query=query,
            index=index,
            minimal=minimal,
            explain=explain,
            extended_meta=extended_meta,
            start=start,
            size=size,
            retries=retries,
            backoff_seconds=backoff_seconds,
        )

    return LazyResultSequence(
        page_size,
        load_page,
    )


@overload
def search_page(
    query: str,
    index: Union[Index, Set[Index]] = ...,
    minimal: Literal[False] = ...,
    explain: Literal[False] = ...,
    extended_meta: Literal[False] = ...,
    start: int = ...,
    size: int = ...,
    retries: int = ...,
    backoff_seconds: float = ...,
    api_key: str = ...,
) -> Results[Meta, Result]: ...


@overload
def search_page(
    query: str,
    index: Union[Index, Set[Index]] = ...,
    minimal: Literal[False] = ...,
    explain: Literal[False] = ...,
    extended_meta: Literal[True] = ...,
    start: int = ...,
    size: int = ...,
    retries: int = ...,
    backoff_seconds: float = ...,
    api_key: str = ...,
) -> Results[ExtendedMeta, Result]: ...


@overload
def search_page(
    query: str,
    index: Union[Index, Set[Index]] = ...,
    minimal: Literal[False] = ...,
    explain: Literal[True] = ...,
    extended_meta: Literal[False] = ...,
    start: int = ...,
    size: int = ...,
    retries: int = ...,
    backoff_seconds: float = ...,
    api_key: str = ...,
) -> Results[Meta, ExplainedResult]: ...


@overload
def search_page(
    query: str,
    index: Union[Index, Set[Index]] = ...,
    minimal: Literal[False] = ...,
    explain: Literal[True] = ...,
    extended_meta: Literal[True] = ...,
    start: int = ...,
    size: int = ...,
    retries: int = ...,
    backoff_seconds: float = ...,
    api_key: str = ...,
) -> Results[ExtendedMeta, ExplainedResult]: ...


@overload
def search_page(
    query: str,
    index: Union[Index, Set[Index]] = ...,
    minimal: Literal[True] = ...,
    explain: Literal[False] = ...,
    extended_meta: Literal[False] = ...,
    start: int = ...,
    size: int = ...,
    retries: int = ...,
    backoff_seconds: float = ...,
    api_key: str = ...,
) -> Results[Meta, MinimalResult]: ...


@overload
def search_page(
    query: str,
    index: Union[Index, Set[Index]] = ...,
    minimal: Literal[True] = ...,
    explain: Literal[False] = ...,
    extended_meta: Literal[True] = ...,
    start: int = ...,
    size: int = ...,
    retries: int = ...,
    backoff_seconds: float = ...,
    api_key: str = ...,
) -> Results[ExtendedMeta, MinimalResult]: ...


@overload
def search_page(
    query: str,
    index: Union[Index, Set[Index]] = ...,
    minimal: Literal[True] = ...,
    explain: Literal[True] = ...,
    extended_meta: Literal[False] = ...,
    start: int = ...,
    size: int = ...,
    retries: int = ...,
    backoff_seconds: float = ...,
    api_key: str = ...,
) -> Results[Meta, ExplainedMinimalResult]: ...


@overload
def search_page(
    query: str,
    index: Union[Index, Set[Index]] = ...,
    minimal: Literal[True] = ...,
    explain: Literal[True] = ...,
    extended_meta: Literal[True] = ...,
    start: int = ...,
    size: int = ...,
    retries: int = ...,
    backoff_seconds: float = ...,
    api_key: str = ...,
) -> Results[ExtendedMeta, ExplainedMinimalResult]: ...


@overload
def search_page(
    query: str,
    index: Union[Index, Set[Index]] = ...,
    minimal: bool = ...,
    explain: bool = ...,
    extended_meta: bool = ...,
    start: int = ...,
    size: int = ...,
    retries: int = ...,
    backoff_seconds: float = ...,
    api_key: str = ...,
) -> Results[
    Union[Meta, ExtendedMeta],
    Union[
        MinimalResult,
        ExplainedMinimalResult,
        Result,
        ExplainedResult,
    ],
]: ...


def search_page(
    query: str,
    index: Union[Index, Set[Index]] = DEFAULT_INDEX,
    minimal: bool = DEFAULT_MINIMAL,
    explain: bool = DEFAULT_EXPLAIN,
    extended_meta: bool = DEFAULT_EXTENDED_META,
    start: int = DEFAULT_START,
    size: int = DEFAULT_SIZE,
    retries: int = DEFAULT_RETRIES,
    backoff_seconds: float = DEFAULT_BACKOFF_SECONDS,
    api_key: str = DEFAULT_API_KEY,
) -> Results[
    Union[Meta, ExtendedMeta],
    Union[
        MinimalResult,
        ExplainedMinimalResult,
        Result,
        ExplainedResult,
    ],
]:
    index_set: Set[Index]
    if isinstance(index, Set):
        index_set = index
    else:
        index_set = {index}

    request: Union[Request]
    response_type: Union[
        Type[MinimalSearchResponse],
        Type[ExplainedMinimalSearchResponse],
        Type[SearchResponse],
        Type[ExplainedSearchResponse],
        Type[ExtendedMetaMinimalSearchResponse],
        Type[ExplainedExtendedMetaMinimalSearchResponse],
        Type[ExtendedMetaSearchResponse],
        Type[ExplainedExtendedMetaSearchResponse],
    ]
    request = Request(
        apikey=api_key,
        query=query,
        start=start,
        size=size,
        index=index_set,
        explain=explain,
        minimal=minimal,
        extended_meta=extended_meta,
    )
    if not extended_meta:
        if minimal:
            if not explain:
                response_type = MinimalSearchResponse
            else:
                response_type = ExplainedMinimalSearchResponse
        else:
            if not explain:
                response_type = SearchResponse
            else:
                response_type = ExplainedSearchResponse
    else:
        if minimal:
            if not explain:
                response_type = ExtendedMetaMinimalSearchResponse
            else:
                response_type = ExplainedExtendedMetaMinimalSearchResponse
        else:
            if not explain:
                response_type = ExtendedMetaSearchResponse
            else:
                response_type = ExplainedExtendedMetaSearchResponse

    response = request_page(
        request=request,
        response_type=response_type,
        endpoint="_search",
        retries=retries,
        backoff_seconds=backoff_seconds,
    )
    return response  # type: ignore
