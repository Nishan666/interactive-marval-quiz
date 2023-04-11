FROM python

RUN mkdir -p /home/app

COPY ./quizApp /home/app

CMD ["python3","home/app/quiz.py"]