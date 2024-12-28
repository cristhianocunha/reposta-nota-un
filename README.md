# Os operadores lógicos, que retornam valores lógicos (verdadeiro ou falso), permitem realizar testes em expressões relacionais compostas. Esses operadores são fundamentais para criar condições mais complexas em algoritmos e são representados por: E , OU  e NAO. Segue o algoritmo abaixo como referência para responder às questões 1 e 2:


Algoritmo "Operadores lógicos"
Var
    A,B,C, D, G: logico
Inicio
    A <- (12 > 10) OU (12 < 10)   
    B <- (32 * (4 - 2) > 69) OU (35 * (4 - 2) > 69)  
    C <- ((32 / 4) - 3 = 5) E ((26 + 6) / 4 = 5)  
    D <- NAO (14 / 2 * 3 > 21) 
    G <- VERDADEIRO E VERDADEIRO OU FALSO 
Fimalgoritmo

## 1) Os resultados das expressões lógicas abaixo, usando o operador E, são respectivamente:

A E B E C,                 A E B E D,                  A E D E G

## 2) Os resultados das expressões lógicas abaixo, usando os operadores OU e E, são respectivamente: 

A E (B OU C),                B E (D OU G),                (B OU G) E C

## 3) Uma empresa remunera seus funcionários com R$ 32,50 por hora trabalhada. No entanto, para salários superiores a R$ 1.800,00, aplica-se um desconto de 8% referente ao Imposto de Renda (IR). Dado o número de horas trabalhadas por um funcionário, determine o salário bruto, o salário líquido, considerando o desconto do IR, se aplicável.
