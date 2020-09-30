using Dash, DashCoreComponents, DashHtmlComponents, Printf

function LoadExampleCode(filename, wd = nothing)
  example_file_as_string = read(filename, String)
  example_ready_for_eval = example_file_as_string
  replacements = [
      r"app.layout =" => "layout ="
      r"app =.*dash\((.*?)\)"m => ""
      r"run_server\(.*?\)" => ""
      r"callback!\(.*?\)"m => ""
  ]
  for replacement in replacements
    example_ready_for_eval = replace(example_ready_for_eval, replacement)
  end
  if !isnothing(wd)
    currentWd = pwd()
    newWd = string(currentWd, "/", wd)
    example_ready_for_eval = string("cd(example_ready_for_eval, newWd)")
  end
  println(example_ready_for_eval)

  include_string(Main, example_ready_for_eval)
  return (
      layout = html_div(
          className = "example-container",
          children = layout,
          style = Dict("marginBottom" => "10px"),
      ),
      source_code = html_div(
          children = dcc_markdown(
              @sprintf("```julia\n%s\n```", example_file_as_string)
          ),
          className = "code-container",
          style = Dict("borderLeft" => "thin lightgrey solid"),
      ),
  )
end

function LoadAndDisplayComponent(example_string)
  return html_div(
    (
      html_div(
        children = dcc_markdown(@printf("```Julia\n%s```", example_string)),
        className = "code-container",
        style = Dict("borderLeft" => "thin lightgrey solid")
      ),
      html_div(
        children = include_string(Main, example_string),
        className = "example-container",
        style = Dict("marginBottom" => "10px", "overflow-x" => "initial")
      ),
    )
  )
end

function LoadAndDisplayComponent2(example_string)
  return html_div(
    (
      html_div(
        children = dcc_markdown(@printf("```Julia\n%s```", example_string)),
        className = "code-container",
        style = Dict("borderLeft" => "thin lightgrey solid")
      ),
      html_div(
        children = include_string(Main, example_string),
        className = "example-container",
        style = Dict("marginBottom" => "10px", "padding-bottom" => "30px")
      ),
    )
  )
end
