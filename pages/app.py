import json



def citeste_json(nume_fisier):

   try:
      with open(nume_fisier,'r',encoding='utf-8') as fisier:
         date =json.load(fisier)
         return date
   except FileNotFoundError:
      print("Fisierul {nume_fisier} nu a fost gasit")
   except json.JSONDecodeError:
      print(f"Fisierul {nume_fisier} nu este un JSON valid.")
   return None

if __name__== "__main__":
   nume_fisier="quiz.json"
   date=citeste_json(nume_fisier)
   if date is not None:
      print("Continutul fisierului JSON:",date)


