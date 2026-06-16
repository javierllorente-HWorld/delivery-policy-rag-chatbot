# Delivery Policy RAG Chatbot

Chatbot simple para responder preguntas sobre políticas de delivery usando documentos internos.

## Qué hace

El proyecto permite consultar políticas cargadas en archivos `.txt`.

El chatbot:

* Lee documentos desde la carpeta `documents`
* Divide el contenido en partes pequeñas
* Crea embeddings con `all-MiniLM-L6-v2`
* Guarda la información en Chroma
* Busca la política más relacionada con la pregunta
* Responde mostrando también la fuente del documento

## Stack usado

* Python 3.12
* Sentence Transformers
* all-MiniLM-L6-v2
* ChromaDB
* Chroma Cloud
* ONNX Runtime

## Cómo usar

Primero cargar los documentos:

```powershell
py -3.12 src/ingest.py
```

Después ejecutar el chatbot:

```powershell
py -3.12 src/main.py
```

Para salir:

```text
salir
```

## Ejemplo

Pregunta:

```text
¿Puedo pedir reembolso?
```

Respuesta:

```text
Las solicitudes de reembolso son revisadas por el equipo de soporte.
Los clientes pueden solicitar un reembolso dentro de las 48 horas posteriores a la entrega.

Fuentes:
- refund_policy.txt
```

## Estado del proyecto

El proyecto está funcionando como prototipo básico de RAG para consultar documentos internos simulados.
