from json import load as json_load
from urllib.parse import parse_qs
from urllib.parse import urlparse
from urllib.parse import urlencode
from urllib.parse import urlunparse
from urllib.request import urlopen

from conllu import parse as conllu_parse

from logger import logger


_PROCESS_URL = "https://lindat.mff.cuni.cz/services/udpipe/api/process?tokenizer&tagger&parser"

__all__ = ["process"]


def _get(url):
    logger.info(f"GET request {url}")
    with urlopen(url) as response:
        logger.info(f"Got response {response.code}")
        json = json_load(response)
        logger.debug(f"JSON response:\n{repr(json)}")
        return json


def _process_url(data):
    parsed_url = urlparse(_PROCESS_URL)
    parsed_query = parse_qs(parsed_url.query, keep_blank_values=True)
    composed_query = urlencode({**parsed_query, "data": data}, doseq=True)
    composed_url = parsed_url._replace(query=composed_query)
    return urlunparse(composed_url)


def process(data):
    logger.info(f"Input is “{data}”")
    url = _process_url(data)
    response = _get(url)
    result = response["result"]
    logger.debug(f"Raw result:\n{result}")
    return conllu_parse(result)
