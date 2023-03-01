# Automated Extraction of IoT Critical Objects from IoT Storylines, Requirements and User Stories via NLP

This repository has the code and dataset used in the paper: Automated Extraction of IoT Critical Objects from IoT Storylines, Requirements and User Stories via NLP

## Abstract

The first step to design a resilient Internet of Things (IoT) application is to identify IoT critical objects (services, device and resource) in the design phase.
However, this step is a time-intensive task, because they are manually identified from storyline, requirements and user stories and have others challenges.
In this work, we assessed the usefulness of Named Entity Recognition (NER) models to automatically  identify IoT critical objects as a way to make a modelling process less plausible for error and faster. This
was performed with development of five NER models based on five different architectures (Spacy, BERT, Transformers, LSTM-CRF and ELMo)
that were trained and tested with a large dataset with 7396
annotated sentences. Our results indicate that the all NER models had a significant performance, but BERT had the best one and can be useful
to support the time-intensive step of the early stages of the development of resilient IoT systems.
Furthermore, these NER models have a high potential to be extended to a framework to automatically extract IoT critical objects from documents (storyline and requirements) and list all possible IoT threats and resilient countermeasures that can be used in the design of an resilient IoT application.
