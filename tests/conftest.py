import pytest
from dash.testing.browser import Browser
from dash.testing.application_runners import ProcessRunner
from tutorial.chapter_index import chapters


@pytest.fixture(scope="session")
def doc_server():
    with ProcessRunner() as server:
        server(raw_command="python run.py", port=8060, start_timeout=60)
        yield server


@pytest.fixture
def dash_doc(doc_server, request):
    with Browser(
        browser=request.config.getoption("webdriver"),
        remote=request.config.getoption("remote"),
        remote_url=request.config.getoption("remote_url"),
        headless=request.config.getoption("headless"),
        options=request.config.hook.pytest_setup_options(),
        percy_finalize=request.config.getoption("nopercyfinalize"),
    ) as browser:
        browser.server_url = doc_server.url
        browser.wait_for_element("#wait-for-layout")
        browser.wait_for_element(".toc .toc--chapter-content")
        yield browser


@pytest.fixture(scope="session")
def chapter_map():
    yield [v["url"] for _, v in chapters.items()]
