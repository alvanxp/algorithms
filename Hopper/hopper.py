import queue
class Question:
    def __init__(self, question, yes, no, answer = None, root=False):
        self.question = question
        self.yes = yes
        self.no = no
        self.root = root
        self.answer = answer

class Anwser:
    def __init__(self, text, question):
        self.text = text
        self.question = question


def CalculateAnswer(qs, parent, output):    
    if qs == None:
        if parent != None:
            #print("parent")
            output.clear()
            CalculateAnswer(parent, None, output)
        return
    
    print(qs.question)
    print(qs.yes.text+","+ qs.no.text)
    value = input("ingrese su respuesta:\n")
    if qs.root:
        parent = qs
    
    if qs.yes != None and qs.yes.text == value:           
        output.append(qs.question)
        output.append(value)
        if qs.yes.question == None and qs.answer == value:             
            return
        
        #print(parent)             
        CalculateAnswer(qs.yes.question, parent, output)
    
    if qs.no != None and qs.no.text == value:       
        output.append(qs.question)
        output.append(value)
        if qs.no.question == None and qs.answer == value:             
            return        
        #print(parent)             
        CalculateAnswer(qs.no.question,parent, output)

#Question("Hola que tal?", None)
question = Question("Te gustaria ir a Jugar?",  Anwser("si",Question("a que lugar quieres ir?",
Anwser("playa", None), Anwser("rio", Question("sabes nadar?", Anwser("si", None), Anwser("no", None), "si"))
,"playa")), Anwser("no", None), "no",True)

queue = []

CalculateAnswer(question, None, queue)
print("=======================================")
print(len(queue))
while len(queue) > 0:
    print(queue.pop(0))