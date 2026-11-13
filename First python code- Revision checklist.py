done=[ ]
english_topics=["anthology revision", "great gatsby", "all my sons", "english essays", "nea non fiction"]
done=[ ]
politics_topics=["uk general election", "usa comparative", "uk topic general", "key thinkers and ideologies", "politics essays"]
done=[ ]
economics_topics=["past papers", "micro y1", "macro y1", "micro y2", "macro y2", "uplearn"]


while True:
    print("Revision Checklist A levels")
    print("============================")
    print()
    print("English A level")
    print("----------------")
    for topic in english_topics:
        if topic in done:
            print("[x]",topic)
        else:
                print("[ ]",topic)
    print()

    print("Politics A level")
    print("-----------------")
    for topic in politics_topics:
        if topic in done:
            print("[x]",topic)
        else:
                print("[ ]",topic)
    print()
        
    print("Economics A level")
    print("------------------")
    for topic in economics_topics:
        if topic in done:
            print("[x]",topic)
        else:
            print("[ ]",topic)
    print()
            
    answer=input("tick/untick ").lower()
    if answer in done:
        done.remove(answer)
    else:

        done.append(answer)
        
          

        
         


