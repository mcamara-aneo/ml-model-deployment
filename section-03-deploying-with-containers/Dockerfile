FROM python:3.9.16

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/titanic-survivor-api

ARG PIP_EXTRA_INDEX_URL

# Install requirements, including from Gemfury
ADD ./titanic-survivor-api /opt/titanic-survivor-api/
RUN pip install --upgrade pip
RUN pip install -r /opt/titanic-survivor-api/requirements.txt

RUN chmod +x /opt/titanic-survivor-api/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]
