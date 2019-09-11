def test_snap002_external_resources(dash_doc):
    driver = dash_doc.driver
    resource = "/external-resources"
    driver.get(dash_doc.server_url + resource)
    dash_doc.wait_for_element_by_id("wait-for-page-{}".format(resource))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    dash_doc.percy_snapshot(resource)


def test_snap100_search(dash_doc):
    dash_doc.driver.get(dash_doc.server_url + "/search")
    dash_doc.wait_for_element_by_id("search-input")
    dash_doc.percy_snapshot("search-blank")
    search = dash_doc.find_element("#search-input")
    dash_doc.clear_input(search)
    search.send_keys("dropdown")
    dash_doc.wait_for_element("#hits .ais-hits--item")
    dash_doc.percy_snapshot("search-dropdown")
