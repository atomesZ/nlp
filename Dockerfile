FROM python:3.9

WORKDIR /app

EXPOSE 8888

RUN pip3 install jupyter

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

# Load data for notebooks into a cache
COPY preloader.py preloader.py

RUN python3 preloader.py

COPY . .

CMD ["jupyter", "notebook", "--no-browser","--NotebookApp.token=''","--NotebookApp.password=''","--allow-root", "--ip=0.0.0.0", "--port=8888"]

