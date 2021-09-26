def owl_count(text):

    count = 0
    
    report = []
    
    text = text.lower()
    
    for index, word in enumerate(text.split()):
    
        if word.find("owl") > -1:
    
            count += 1
            
            report += [index,]
            
    print("There were " + str(count) + """ words that contained "owl".""")
    
    print("They occurred at indices: " + str(report))


text = input("Enter some text")

owl_count(text)