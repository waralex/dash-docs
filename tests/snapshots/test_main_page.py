def test_snap001_index_page_links(dash_doc):
    dash_doc.wait_for_element(".toc .toc--chapter-content")
    dash_doc.percy_snapshot("index - 1")
    ids = (
        elem.get_property("id")
        for elem in dash_doc.driver.find_elements_by_tag_name("a")
    )
    resources = [
        id_
        for id_ in ids
        if id_.startswith("/") and id_ != "/external-resources"
    ]
    for resource in resources:
        dash_doc.visit_and_snapshot(
            resource, hook_id="wait-for-page-{}".format(resource)
        )
