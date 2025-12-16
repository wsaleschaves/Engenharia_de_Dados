# 📊 MVP – Engenharia de Dados  
## Análise das Bolsas do Prouni no Brasil (2005–2019)

Este repositório apresenta um **MVP (Minimum Viable Product) de Engenharia de Dados**, cujo objetivo é a construção de um **pipeline de dados em nuvem**, utilizando **Databricks, Apache Spark, Delta Lake e modelagem dimensional**, para análise das bolsas concedidas pelo **Programa Universidade para Todos (Prouni)**.

O projeto cobre todo o ciclo de dados — da ingestão à análise — seguindo a **arquitetura Medallion (Bronze, Silver e Gold)** e entregando uma **camada analítica confiável e otimizada para BI**.

---

## 🎯 1. Objetivo do Projeto

O objetivo deste MVP é **consolidar, tratar, padronizar e analisar** os dados do Prouni, resolvendo o problema da **ausência de uma visão integrada e estruturada** sobre o comportamento das bolsas concedidas no Brasil.

O pipeline contempla:

- Ingestão de dados brutos  
- Limpeza e padronização  
- Modelagem dimensional (Esquema Estrela)  
- Criação de dimensões e tabela fato  
- Disponibilização de dados para análises e BI  

### Perguntas Analíticas Respondidas

- Qual o volume total de bolsas concedidas ao longo dos anos?
- Quais cursos recebem mais bolsas?
- Como as bolsas se distribuem por região, estado e município?
- Qual o perfil dos beneficiários (sexo, raça/cor e idade)?
- Quais instituições concentram o maior número de bolsas?
- Qual a proporção entre bolsas integrais e parciais?
- Há tendência de crescimento ou redução nas concessões ao longo do tempo?

---

## ✅ 1.1 Resultados Esperados

Ao final do projeto, são entregues:

- Um **Lakehouse confiável** com camadas Bronze → Silver → Gold  
- Um **modelo estrela completo**, com tabela fato e dimensões usando surrogate keys  
- Dados padronizados e prontos para consumo via BI e análises exploratórias  
- Insights sobre o acesso ao ensino superior e políticas educacionais  

---

## 🌐 2. Fonte dos Dados

Os dados utilizados são **públicos e abertos**, sem restrições de confidencialidade.

- **Fonte:** Kaggle – *Brasil Students Scholarship (Prouni) 2005–2019*  
- 🔗 https://www.kaggle.com/datasets/lfarhat/brasil-students-scholarship-prouni-20052019  

A base consiste em arquivos CSV consolidados contendo milhões de registros com informações sobre:

- Tipo de bolsa  
- Curso  
- Instituição  
- Localização  
- Perfil do beneficiário  

---

## 🧱 3. Arquitetura do Pipeline (Medallion)

O pipeline foi desenvolvido seguindo a **arquitetura Medallion**, garantindo governança, rastreabilidade e qualidade dos dados.

### 🥉 Bronze – Dados Brutos
- Armazena os dados exatamente como recebidos da fonte  
- Sem transformações  
- Serve como backup histórico e base para auditorias  

### 🥈 Silver – Dados Refinados
- Padronização de textos  
- Correção de tipos de dados  
- Tratamento de datas  
- Remoção de duplicatas  
- Normalização de categorias  

### 🥇 Gold – Camada Analítica
- Modelo dimensional (Esquema Estrela)  
- Tabela fato + dimensões  
- Dados prontos para análises e BI  

---

## 📐 4. Modelagem Dimensional

Foi aplicada **modelagem dimensional em Esquema Estrela**, amplamente utilizada em projetos de BI por sua eficiência analítica e simplicidade de consultas.

### 📊 Tabela Fato – `fato_prouni_gold`

Cada linha representa **uma bolsa concedida**, contendo:

- Ano da concessão  
- Chaves substitutas das dimensões  
- Informações institucionais, acadêmicas e do beneficiário  

### 📊 Dimensões Criadas

- `dim_instituicao_gold`
- `dim_curso_gold`
- `dim_tipo_bolsa_gold`
- `dim_turno_gold`
- `dim_localizacao_gold`
- `dim_beneficiario_gold`
- `dim_tempo_gold`

Todas as dimensões utilizam **surrogate keys (cod_*)**, garantindo:

- Integridade referencial  
- Melhor performance  
- Redução de redundância  
- Facilidade de manutenção  

---

## 📚 5. Catálogo de Dados (Resumo)

**Tabela Fato – `fato_prouni_gold`**
- Ano da concessão  
- Códigos das dimensões  
- Base para todas as métricas e análises  

**Dimensões**
- Instituição: dados da IES  
- Curso: nome e padronização  
- Tipo de bolsa: integral ou parcial  
- Turno: modalidade de horário  
- Localização: região, UF e município  
- Beneficiário: sexo, raça, idade e nascimento  
- Tempo: anos analisados  

---

## 🧪 6. Qualidade e Governança dos Dados

Durante o ETL foram tratados diversos problemas de qualidade:

- Padronização de textos (maiúsculas, acentuação, espaços)  
- Correção de datas em múltiplos formatos  
- Tratamento de valores inválidos e inesperados  
- Remoção de duplicatas em dimensões e fato  
- Tratamento consciente de valores nulos  
- Validação de integridade antes da carga na Gold  

Essas etapas garantiram **consistência, confiabilidade e robustez** dos dados finais.

---

## 📊 7. Análises e Principais Resultados

### 🔹 Evolução das Bolsas ao Longo do Tempo
- Tendência inicial de crescimento  
- Oscilações relacionadas a contexto econômico e políticas públicas  
- Atenção à incompletude dos anos mais recentes  

### 🔹 Cursos com Mais Bolsas
- Forte concentração em cursos como:
  - Administração  
  - Pedagogia  
  - Direito  
  - Enfermagem  

### 🔹 Distribuição Geográfica
- Concentração em regiões mais populosas  
- Forte presença em grandes centros urbanos  

### 🔹 Perfil dos Beneficiários
- Predominância de jovens entre 18 e 39 anos  
- Maior participação feminina  
- Maior concentração entre beneficiários pardos e pretos  

### 🔹 Instituições
- Concentração em instituições privadas de grande porte  

### 🔹 Tipo de Bolsa
- Predominância de bolsas integrais  
- Reforço do caráter social do programa  

---

## 🏁 8. Atingimento dos Objetivos

Todos os objetivos definidos no início do projeto foram **plenamente atingidos**. O pipeline construído possibilitou análises estruturadas, confiáveis e reprodutíveis, respondendo às perguntas analíticas propostas.

---

## 🚀 9. Conclusão

Este MVP demonstra a aplicação prática de conceitos de **Engenharia de Dados** em um cenário real de política pública, entregando uma base analítica robusta e preparada para BI e análises avançadas.

O projeto consolida conhecimentos teóricos por meio de uma solução escalável, organizada e alinhada às melhores práticas do mercado.
