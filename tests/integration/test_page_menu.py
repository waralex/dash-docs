import time
import pytest
import sys
import selenium

def retry_wait_for_text_to_equal(dash_doc, selector, text):
    i = 0
    while True:
        i += 1
        try:
            return dash_doc.wait_for_text_to_equal(
                selector,
                text,
                timeout=20
            )
        except selenium.common.exceptions.StaleElementReferenceException as e:
            if i == 10:
                raise Exception(
                    'Attempted 10 times to check that {} == "{}"'.format(
                        selector,
                        text
                    )
                )
            time.sleep(3)
        except Exception as e:
            raise e


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
