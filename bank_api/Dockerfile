FROM python:3.11
RUN mkdir /bank_api
WORKDIR /bank_api
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod a+x docker/*.sh
