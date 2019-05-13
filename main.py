import json
import file_service

class Algoritimun:
  group = [] # Conjunto de estados
  alphabet = [] # Alfabeto aceito
  sequence = [] # Sequencia de valores
  matrix = [] # Matriz de transições
  initial_state = "" # String identificando estado inicial
  final_state = [] # Array de estados finais
  
  def __init__(self, group, alphabet, sequence, matrix, initialState, finalState):
    self.group = group
    self.alphabet = alphabet
    self.sequence = sequence
    self.matrix = matrix
    self.initial_state = initialState
    self.final_state = finalState

  def validate(self):
    validating = True
    matrix = self.matrix

    count = 0
    currentObj = None
    root = []
    statesDescribing = ""
    key = ""

    outcoming = ""
    while(validating):
      
      # First of all, search for the initial_state
      
      if root == []:
        for array in matrix:
          if self.initial_state in array:
            root = array[self.initial_state]
            print("Estado inicial -> " + list(array.keys())[0])
            outcoming += "Estado inicial -> " + list(array.keys())[0] + "\n"
            statesDescribing = list(array.keys())[0] + " "
            break
        currentObj = root
      
      
      print("Símbolo lido -> " + str(self.sequence[count]))
      outcoming += "Símbolo lido -> " + str(self.sequence[count]) + "\n"
      statesDescribing += key + " "                  
      print("Estados correntes -> " + statesDescribing)
      outcoming += "Estados correntes -> " + statesDescribing + "\n"


      for obj in currentObj:
        
        if self.sequence[count] in list(obj.values())[0]:
        
          
          key = list(obj.keys())[0]

          
          if key in self.final_state:
            validating = False
            outcoming += "Estado final -> " + str(self.final_state) + "\n"
            print("Estado final -> " + str(self.final_state) + "\n")
            file_service.File.createResultFileWith("ACEITO")
            print("Aceito -> Arquivo criado em outcoming_result.txt")
            outcoming += "Sequencia Aceita \n"
            file_service.File.createOutcomingFileWith(outcoming)

          else:
            validating = True
            currentObj = self.getObjectForKey(key)

            break
          
        else:
          validating = False
      
      if (count == len(self.sequence) - 1): 
        validating = False
        
        file_service.File.createResultFileWith("REJEITADO")
        print("Rejeitado -> Arquivo criado em outcoming_result.txt")
        outcoming += "Sequencia Rejeitada \n"
        file_service.File.createOutcomingFileWith(outcoming)
      count += 1
  
  def getObjectForKey(self, key):
    
    for array in self.matrix:
      if key in array:

        return array[key]


      

rawFile = file_service.File.readFile()

json = json.loads(rawFile)

afn = Algoritimun(json["group"], json["alphabet"], json["sequence"], json["matrix"], json["initial_state"], json["final_state"])

afn.validate()
