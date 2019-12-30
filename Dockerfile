FROM rpkyle/heroku-docker-r:3.6.2_heroku18

# on build, copy application files
COPY . /app/

# on build, for installing additional dependencies etc.
RUN if [ -f "/app/onbuild" ]; then bash /app/onbuild; fi;

# on build, for backward compatibility, look for /app/Aptfile and if it exists, install the packages contained
RUN if [ -f "/app/Aptfile" ]; then apt-get update -q && cat Aptfile | xargs apt-get -qy install && rm -rf /var/lib/apt/lists/*; fi;

# on build, for backward compatibility, look for /app/init.R and if it exists, execute it
RUN if [ -f "/app/init.R" ]; then /usr/bin/R --no-init-file --no-save --quiet --slave -f /app/init.R; fi;

CMD cd /app && /usr/bin/R --no-save -f /app/run.R
