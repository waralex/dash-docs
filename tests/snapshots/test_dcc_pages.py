def test_snap200_dcc_resources(chapter_map, dash_doc):
    dcc_resources = [
        _ for _ in chapter_map if _.startswith("/dash-core-components")
    ]
    for resource in dcc_resources:
        dash_doc.visit_and_snapshot(
            resource, hook_id="wait-for-page-{}".format(resource)
        )


def test_snap300_dds_resources(chapter_map, dash_doc):
    dds_resources = [
        _ for _ in chapter_map if _.startswith("/dash-deployment-server")
    ]
    for resource in dds_resources:
        dash_doc.visit_and_snapshot(
            resource, hook_id="wait-for-page-{}".format(resource)
        )


def test_snap400_dashtable_resources(chapter_map, dash_doc):
    table_resources = [
        _ for _ in chapter_map if _.startswith("/datatable/")
    ]
    for resource in table_resources:
        dash_doc.visit_and_snapshot(
            resource, hook_id="wait-for-page-{}".format(resource)
        )


def test_snap500_cytoscape_resources(chapter_map, dash_doc):
    cytoscapes = [
        _ for _ in chapter_map if _.startswith("/cytoscape/")
    ]
    for resource in cytoscapes:
        dash_doc.visit_and_snapshot(
            resource, hook_id="wait-for-page-{}".format(resource)
        )
