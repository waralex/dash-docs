import time
import pytest
import sys
from retrying import retry
import selenium

def _retry_if_stale_error(exception):
    return isinstance(
        exception,
        selenium.common.exceptions.StaleElementReferenceException
    )


@retry(
    retry_on_exception=_retry_if_stale_error,
    stop_max_attempt_number=5,
    wait_exponential_multiplier=1000,
    wait_exponential_max=10000
)
def retry_wait_for_text_to_equal(dash_doc, selector, text):
    dash_doc.wait_for_text_to_equal(
        selector,
        text,
        timeout=20
    )


@pytest.mark.skipif(
    sys.version_info < (3, 7),
    reason="skip non-essential, potentially flaky tests"
)
def test_page_menu_001(dash_doc):
    dash_doc.driver.get(dash_doc.server_url + '/testing')
    dash_doc.wait_for_element_by_id("page-menu--links")
    testing_links = [
        'Dash Testing',
        'Install',
        'Caveats',
        'Example',
        'Dash for R testing',
        'Fixtures',
        'APIs',
        'Selenium Overview',
        'Element Locators',
        'Waits',
        'Browser APIs',
        'Dash APIs',
        'Debugging',
        'Verify your test environment',
        'Run the CI job locally',
        'Increase the verbosity of pytest logging level',
        'Selenium Snapshots',
        'Percy Snapshots',
    ]

    for i in range(len(testing_links)):
        retry_wait_for_text_to_equal(
            dash_doc,
            '#page-menu--link-{}'.format(i),
            testing_links[i],
        )

    dash_doc.find_element('#logo-home').click()
    dash_doc.wait_for_element_by_id("page-menu--links")

    home_links = [
        'Dash User Guide',
        'What\'s Dash?',
        'Dash Tutorial',
        'Dash Callbacks',
        'Open Source Component Libraries',
        'Creating Your Own Components',
        'Beyond the Basics',
        'Production',
        'Getting Help',
        'Dash Enterprise',
    ]

    for i in range(len(home_links)):
        retry_wait_for_text_to_equal(
            dash_doc,
            '#page-menu--link-{}'.format(i),
            home_links[i]
        )
