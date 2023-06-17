FROM python:3.9-bullseye AS build-env

#creating dir
RUN mkdir /backend
WORKDIR /backend
RUN touch sample.txt

#installing requriments
COPY requirements.txt .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

#installing internal requriments
ARG GIT_TOKEN
COPY internal-requirements.txt .
RUN for pkg in $(cat internal-requirements.txt);do pip3 install $(python -c "import sys;pkg, ver = sys.argv[1].split('==');print(f'git+https://{sys.argv[2]}@github.com/BankBuddy/bud-core-{pkg}-lib@{ver}')" $pkg $GIT_TOKEN);done

# for oracleDB
RUN apt update
RUN apt install libaio1 -y
RUN mkdir -p /opt/oracle
ADD assets/instantclient_19_6 /opt/oracle/instantclient_19_6
RUN sh -c "echo /opt/oracle/instantclient_19_6 > /etc/ld.so.conf.d/oracle-instantclient.conf" && \
    ldconfig && \
    LD_LIBRARY_PATH=/opt/oracle/instantclient_19_6

COPY . /backend

#distroless
FROM gcr.io/distroless/python3-debian11
COPY --from=build-env --chown=nonroot:nonroot /backend /backend
COPY --from=build-env --chown=nonroot:nonroot /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build-env --chown=nonroot:nonroot /opt/oracle /opt/oracle
COPY --from=build-env --chown=nonroot:nonroot /usr/lib/x86_64-linux-gnu/ /usr/lib/x86_64-linux-gnu/
COPY --from=build-env --chown=nonroot:nonroot /lib/x86_64-linux-gnu/ /usr/lib/x86_64-linux-gnu/
COPY --from=build-env --chown=nonroot:nonroot /usr/local/bin /usr/local/bin
COPY --from=build-env --chown=nonroot:nonroot /backend/logs /bot/backend
COPY --from=build-env --chown=nonroot:nonroot /backend/libpython3.9.so.1.0 /usr/lib/x86_64-linux-gnu/
#Run true needed as intermediate container error is being thrown during build stage giving issue in pipeline build
RUN true

ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_19_6
ENV PYTHONPATH=/usr/local/lib/python3.9/site-packages
ENV PYTHONUNBUFFERED=1
WORKDIR /backend
USER nonroot


CMD ["/usr/local/bin/gunicorn", "-w", "4", "--bind", "0.0.0.0:8000", "main.asgi:application", "-k", "uvicorn.workers.UvicornWorker"]
