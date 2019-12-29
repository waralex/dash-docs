FROM plotly/heroku-docker-r:dash
ENV PORT=8080
CMD "/usr/bin/R --no-save -f /app/run.R"
