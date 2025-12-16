# Engenharia_de_Dados

Análise de Bolsas do Prouni no Brasil

Este repositório apresenta um MVP (Minimum Viable Product) de Engenharia de Dados, desenvolvido com foco na construção de um pipeline de dados em arquitetura Lakehouse, utilizando Databricks, Apache Spark, Delta Lake e modelagem dimensional (Esquema Estrela) para análise das bolsas concedidas pelo Programa Universidade para Todos (Prouni).
O projeto cobre todo o ciclo de dados: ingestão, tratamento, padronização, modelagem, governança e análise, culminando em uma camada analítica otimizada para Business Intelligence e análises exploratórias.

1. Objetivo do Projeto

O objetivo principal deste MVP é construir um pipeline de dados robusto e reprodutível capaz de consolidar e analisar os dados do Prouni, proporcionando uma visão estruturada sobre a concessão de bolsas de estudo no Brasil.

O pipeline foi desenhado para:
Ingerir dados públicos em formato bruto
Tratar e padronizar informações inconsistentes
Modelar os dados em um esquema estrela
Disponibilizar uma camada analítica confiável (Gold)
Permitir análises históricas, demográficas e regionais

Problema de Negócio
Os dados do Prouni, apesar de públicos, não estão prontos para análise direta, pois apresentam:
Fragmentação por entidades
Inconsistências de texto e categorias
Problemas de duplicidade
Datas em múltiplos formatos
Ausência de um modelo analítico estruturado
Este MVP resolve esse problema ao entregar um Data Lakehouse organizado, preparado para responder perguntas estratégicas sobre o acesso ao ensino superior no Brasil.

Perguntas Analíticas Respondidas

O projeto foi estruturado para responder, entre outras, as seguintes perguntas:
Qual o volume total de bolsas concedidas ao longo dos anos?
Quais cursos recebem mais bolsas?
Como as bolsas se distribuem por região, estado e município?
Qual o perfil dos beneficiários (sexo, raça/cor, idade)?
Quais instituições concentram o maior número de bolsas?
Qual a proporção entre bolsas integrais e parciais?
Existe tendência de crescimento ou redução nas concessões ao longo do tempo?

1.1 Resultados Esperados

Ao final do projeto, são entregues:
Um Lakehouse confiável com camadas Bronze → Silver → Gold
Um modelo dimensional completo (Esquema Estrela)
Tabela fato e dimensões com surrogate keys
Dados padronizados e prontos para consumo por BI
Base sólida para análises exploratórias e dashboards
Insights sobre políticas públicas e acesso ao ensino superior

2. Fonte dos Dados e Coleta

Os dados utilizados são públicos e abertos, sem restrições de confidencialidade, contendo informações sobre bolsas concedidas pelo Prouni entre 2005 e 2019.

📌 Fonte Principal

Kaggle – Brasil Students Scholarship (Prouni) 2005–2019
🔗 https://www.kaggle.com/datasets/lfarhat/brasil-students-scholarship-prouni-20052019

Características da Base
Arquivo CSV consolidado
Milhões de registros
Informações sobre:
Tipo de bolsa (integral/parcial)
Curso
Instituição
Turno
Localização
Perfil do beneficiário

2.1 Tabela Fato – Prouni

A tabela fato do projeto, denominada fato_prouni_gold, representa o evento central do modelo: a concessão de uma bolsa.

Ela consolida informações como:
Ano da concessão
Instituição de ensino
Curso
Tipo de bolsa
Turno
Localização do beneficiário
Perfil demográfico do aluno
Cada linha da tabela fato corresponde a uma bolsa concedida, permitindo análises temporais, regionais e demográficas.

2.2 Dimensões e Surrogate Keys

Na camada Gold, foram criadas dimensões independentes, cada uma com sua surrogate key (cod_*), garantindo:

Integridade referencial
Melhor performance de consultas
Redução de redundância
Facilidade de manutenção

Dimensões Criadas
dim_instituicao_gold
dim_curso_gold
dim_tipo_bolsa_gold
dim_turno_gold
dim_localizacao_gold
dim_beneficiario_gold
dim_tempo_gold

Todas as dimensões são derivadas da camada Silver, já tratadas e padronizadas.
