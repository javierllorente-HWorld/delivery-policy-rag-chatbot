# Delivery Policy RAG Chatbot

Chatbot RAG para consultar políticas de delivery usando Python, Sentence Transformers y ChromaDB.

## Stack

- Python 3.12
- Sentence Transformers
- all-MiniLM-L6-v2
- ChromaDB
- Chroma Cloud
- ONNX Runtime

## Estado actual

El proyecto ya funciona con:

- Lectura de archivos `.txt` desde `documents/`
- Creación de chunks simples
- Generación de embeddings con `all-MiniLM-L6-v2`
- Guardado en Chroma Cloud
- Búsqueda semántica desde consola
- Respuesta con fuente del documento

## Problemas encontrados

ChromaDB local en Windows fallaba al ejecutar:

```python
collection.add(...)
El proceso se cerraba sin traceback y devolvía:

-1073741819

Esto indica un crash nativo de Windows.

Se probaron distintas versiones de ChromaDB. Las versiones 1.x instalaban pero crasheaban en add(). Las versiones 0.x pedían compilar chroma-hnswlib, lo cual requería Microsoft Visual C++ Build Tools.

Solución actual

Se usa Chroma Cloud para mantener ChromaDB como vector database sin cambiar el stack principal.

Nota sobre API key

En este proyecto de práctica la API key puede estar visible en el código porque no contiene información importante ni se usa para producción.

Uso

Cargar documentos:

py -3.12 src/ingest.py

Ejecutar chatbot:

py -3.12 src/main.py
Documentos

Los archivos deben estar en:

documents/

## Commit

Ejecutá:

```powershell
git status
git add .
git commit -m "Add working Chroma Cloud RAG prototype"
git push