# Autômato
Disciplina: Complexidade de Algoritmos
Implemente um simulador de autômatos finitos determinísticos, sendo que a entrada para o programa é dada por um arquivo no formato:

<ul>
  <li>q0</li>
  <li>a b</li>
  <li>q0 q1 q2 q3</li>
  <li>q1 q3</li>
  <li>q0 q1 a</li>
  <li>q1 q1 a</li>
  <li>q1 q2 b</li>
  <li>q2 q1 b</li>
  <li>q2 q3 a</li>  
</ul>

Onde:
Linha 1 define o estado inicial
Linha 2 define os símbolos do alfabeto
Linha 3 define o conjunto de estados
Linha 4 define o conjunto de estados finais
Linhas 5 - fim do arquivo definem as transições entre os estados

Após ler o arquivo, o usuário deve entrar com uma palavra (via teclado), e o programa deve responder com “Aceita”, casa a palavra seja aceita pela linguagem definida pelo autônome, ou “Rejeita”, caso contrário.
