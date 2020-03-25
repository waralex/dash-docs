import pytest
import sys

@pytest.mark.skipif(sys.version_info < (3, 6), reason="requires python3.6 or higher")
def test_sidebar001(dash_doc):
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
        dash_doc.wait_for_text_to_equal(
            '#page-menu--link-{}'.format(i),
            testing_links[i]
        )

    dash_doc.find_element('#logo-home').click()


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
        dash_doc.wait_for_text_to_equal(
            '#page-menu--link-{}'.format(i),
            home_links[i]
        )
