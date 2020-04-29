import random

def handle_uploaded_file(f):
    randomvalue=str(random.randint(0,100))
    f.name='GL'+randomvalue+str(f.name).replace(" ",'')
    with open('home/static/upload/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)