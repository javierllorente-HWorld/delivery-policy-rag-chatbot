# Delivery Policy RAG Chatbot

Chatbot simple para responder preguntas sobre políticas de delivery usando documentos internos.

Es la sexta etapa de un roadmap técnico personal de 8 proyectos que armé para repasar bases, practicar con ejemplos concretos y mejorar mi lado técnico paso a paso.

La idea de este proyecto fue entender cómo funciona un flujo básico de RAG: cargar documentos, dividir el contenido, guardar embeddings y recuperar la información más relevante para responder una pregunta.

---

## Qué hace

* Lee documentos desde una carpeta local.
* Divide el contenido en partes más pequeñas.
* Crea embeddings del contenido.
* Guarda la información en ChromaDB.
* Busca fragmentos relacionados con la pregunta.
* Responde mostrando también la fuente del documento.

---

## En qué me enfoqué

* Entender el flujo básico de un sistema RAG.
* Practicar carga y división de documentos.
* Trabajar con embeddings.
* Usar una base vectorial simple.
* Relacionar preguntas con información tomada de documentos internos.

---

## Estado del proyecto

Etapa 6 de 8 del roadmap técnico personal.

Proyecto de práctica enfocado en RAG, embeddings y consulta de documentos internos simulados.


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

