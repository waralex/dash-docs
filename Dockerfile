FROM plotly/heroku-docker-r:3.6.2_heroku18

RUN /usr/bin/R --no-save --quiet --slave -e "install.packages(c('remotes', 'later', 'jsonlite', 'rjson', 'listenv', 'anytime', 'readr', 'heatmaply', 'bezier', 'png', 'foreach', 'glue', 'stringr')); remotes::install_github('rpkyle/debbie'); debbie::install_deb('magick')"

# on build, copy application files
COPY . /app/

# look for /app/Aptfile and if it exists, install the packages contained
RUN if [ -f "/app/Aptfile" ]; then apt-get -qy update && cat Aptfile | xargs apt-get --quiet --yes --allow-downgrades --allow-remove-essential --allow-change-held-packages -o Dpkg::Options::="--force-confdef" -o Dpkg::Options::="--force-confold" install && rm -rf /var/lib/apt/lists/*; fi;

# look for /app/init.R and if it exists, execute it
RUN if [ -f "/app/init.R" ]; then /usr/bin/R --no-init-file --no-save --quiet --slave -f /app/init.R; fi;

CMD cd /app && /usr/bin/R --no-save -f /app/run.R
