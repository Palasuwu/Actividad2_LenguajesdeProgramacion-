# Actividad2_LenguajesdeProgramacion

## Descripción del Ejercicio 
Este proyecto implementa un **lexer (scanner)** para analizar código Java. Tokeniza el código fuente identificando palabras reservadas, identificadores, números, cadenas, operadores y delimitadores.

## Estructura del programa
- `lexer.py` - Analizador léxico principal que convierte código fuente en tokens
- `token_data.py` - Definición de tipos de tokens y palabras reservadas
- `symbol_table.py` - Tabla de símbolos que registra identificadores y su frecuencia
- `main.py` - Archivo de prueba con ejemplo de código Java

## Cómo Ejecutar
```bash
python main.py
```

## Características
- Reconoce comentarios (`//` y `/* */`)
- Identifica palabras reservadas de Java
- Maneja números enteros y decimales
- Procesa cadenas de texto
- Genera tabla de símbolos con frecuencia de identificadores
- Muestra tokens organizados por línea de código

## Salida
El programa imprime:
1. Lista secuencial de tokens (tipo, valor, línea, columna)
2. Tabla de símbolos con frecuencia de cada identificador

   
<img width="585" height="726" alt="Screenshot 2026-02-01 at 6 34 32 PM" src="https://github.com/user-attachments/assets/a94ffbc8-41e3-455f-b2de-6a6af632bad8" />

<img width="585" height="403" alt="Screenshot 2026-02-01 at 6 34 49 PM" src="https://github.com/user-attachments/assets/faabfc6f-10eb-40e6-90be-3611e7bb3f48" />
