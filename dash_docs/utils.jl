using Dash, DashCoreComponents, DashHtmlComponents, Printf

function LoadExampleCode(filename, wd = nothing)
  example_file_as_string = read(filename, String)
  example_ready_for_eval = example_file_as_string
  replacements = [
      r"app.layout =" => "layout ="
      r"app =.*dash\((.*?)\)"m => ""
      r"run_server(app, \"0.0.0.0\", 8000)" => ""
  ]
  for replacement in replacements
    example_ready_for_eval = replace(example_ready_for_eval, replacement)
  end
  if !isnothing(wd)
    currentWd = pwd()
    newWd = string(currentWd, "/", wd)
    example_ready_for_eval = string("cd(example_ready_for_eval, newWd)")
  end
  include_string(Main, example_ready_for_eval)
  return (
      "layout" => html_div(
          className = "example-container",
          style = ("margin-bottom" => "10px",)
      ),
      "source_code" => html_div(
          children = dcc_markdown(
              @sprintf("```julia\n%s```", example_file_as_string)
          ),
          className = "code-container",
          style = ("border-left" => "thin lightgrey solid",)
      ),
  )
end

function LoadAndDisplayComponent(example_string)
  return html_div(
    (
      html_div(
        children = dcc_markdown(@printf("```julia %s```", example_string)),
        className = "code-container",
        style = ("border-left" => "thin lightgrey solid",)
      ),
      html_div(
        children = include_string(Main, example_string)
        className = "example-container",
        style = ("margin-bottom" => "10px", "overflow-x" => "initial", )
      ),
    )
  )
end

function LoadAndDisplayComponent2(example_string)
  return html_div(
    (
      html_div(
        children = dcc_markdown(@printf("```julia %s```", example_string)),
        className = "code-container",
        style = ("border-left" => "thin lightgrey solid",)
      ),
      html_div(
        children = include_string(Main, example_string),
        className = "example-container",
        style = ("margin-bottom" => "10px", "padding-bottom" => "30px", )
      ),
    )
  )
end
