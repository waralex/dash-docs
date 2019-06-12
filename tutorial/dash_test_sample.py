# 1. imports of your dash app
import dash_html_components as html
import dash


# 2. give each testcase a tcid, and pass the fixture
# as a function argument, less boilerplate
def test_bsly001_falsy_child(dash_duo):

    # 3. define your app inside the test function
    app = dash.Dash(__name__)
    app.layout = html.Div(id="nully-wrapper", children=0)

    # 4. host the app locally in a thread
    dash_duo.start_server(app)

    # 5. use wait_for_* if your target element is the result of a callback,
    # keep in mind even the initial rendering can trigger callbacks
    dash_duo.wait_for_text_to_equal("#nully-wrapper", "0", timeout=4)

    # 6. use this form if its present is expected at the action point
    assert dash_duo.find_element("#nully-wrapper").text == "0"

    # 7. use python builtin assert statement, and describe your
    # criteria as an assertion message after the comma.
    assert dash_duo.get_logs() == [], "browser console contain no error"

    # 8. visual testing with percy snapshot
    dash_duo.percy_snapshot("bsly001-layout")
