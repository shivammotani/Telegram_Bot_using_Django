from .models import * 

def create_entry(id,text):
    d=0
    s=0
    f=0
    if(text == 'stupid'):
        s = 1
    elif(text == 'fat'):
        f = 1
    elif(text == 'dumb'):
        d = 1
    noOfCalls.objects.create(
        user_id = id,
        stupid = s,
        fat = f,
        dumb = d
    )


def updateDb(ids, text):
    db_id = noOfCalls.objects.filter(user_id = ids)
    if not db_id.exists():
        create_entry(ids,text)
    else:
        a = noOfCalls.objects.get(user_id = ids)
        if(text == 'stupid'):
            a.stupid = a.stupid + 1
        elif(text == 'fat'):
            a.fat = a.fat + 1
        elif(text == 'dumb'):
            a.dumb = a.dumb + 1
        a.save()
    

