count = 10     #global
def update_count():
    count = 5  #local
    print('Inside:', count)

update_count()
print('Outside:', count)