FROM python:3

WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN git clone https://github.com/AntoanetaStoyanova/PROJECT-IMBD.git 

EXPOSE 8080

ENTRYPOINT ["streamlit", "run", "code_API_Streamlit.py"]

