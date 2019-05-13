# itc_simulator

Este repositório representa um trabalho acadêmico.

Se trata de um Simulador de Autômato Finitito Não Determinístico - AFN, foi desenvolvido em Python e contém um repositório teste online em https://repl.it/@DanielSilveira/afn-simulator.

# Como executar

O algorítmo lê um arquivo com o serviço [file_service](file_service.py) e lê um arquivo .json que fica localizado em [incoming.json](incoming.json).

Este arquivo contém os dados de execução do algorítmo, este se compõem em:

```
{
  "group": ["q1", "q2", "q3"], # Contém todo o conjunto de estados
  "alphabet": [0, 1], # Alfabeto aceito
  "sequence": [0, 1, 0, 1, 1, 1], # Conjunto de sequência
  "matrix":     #  Matriz de estados, deve ser composto por um array geral, um objeto com um estado 
    [           # como chave, e em relação com essa chave, um array contento um estado como chave e
      { "q1": [ #  em relação com essa chave, um array contendo os valores aceitos naquele estado
          {"q2":[1]},
          {"q1":[0,1]}
        ]
      },
      { "q2":[
          {"q3": [0, "*"]}
        ]
      },
      { "q3":[
          {"q4":[1]}
        ]
      },
      { "q4":[
          {"q4":[0,1]}
        ]
      }
    ],
  "initial_state": "q1", # O estado inicial
  "final_state": ["q4"]  # Conjunto de estados finais
}
```

# Resultado

O resultado do algorítmo é gerado em [outcoming_result.txt](outcoming_result.txt)

A sequência do algorítmo é gerado em [outcoming.txt](outcoming.txt)
