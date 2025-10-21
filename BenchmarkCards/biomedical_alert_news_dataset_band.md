# Biomedical Alert News Dataset (BAND)

## 📊 Benchmark Details

**Name**: Biomedical Alert News Dataset (BAND)

**Overview**: To address this gap, we introduce the Biomedical Alert News Dataset (BAND), which includes 1,508 samples from existing reported news articles, open emails, and alerts, as well as 30 epidemiology-related questions.

**Data Type**: text (news articles, open emails, alerts; question-answering pairs)

**Domains**:
- Natural Language Processing
- Epidemiology
- Public Health

**Languages**:
- English

**Similar Benchmarks**:
- A global dataset of pandemic-and epidemic-prone disease outbreaks
- The world health organization’s disease outbreak news: A retrospective database
- Developing a disease outbreak event corpus

**Resources**:
- [GitHub Repository](https://github.com/fuzihaofzh/BAND)
- [Resource](https://arxiv.org/abs/2305.14480)
- [Resource](https://promedmail.org/)
- [Resource](https://labelstud.io/)

## 🎯 Purpose and Intended Users

**Goal**: This dataset aims to empower NLP systems to analyze and address several critical questions, which aids the current surveillance systems in identifying significant trends and providing insights on how to improve disease surveillance and management.

**Target Audience**:
- Epidemiologists
- Natural Language Processing Researchers

**Tasks**:
- Named Entity Recognition
- Question Answering
- Event Extraction

**Limitations**: The dataset primarily focuses on disease outbreak news reports obtained from ProMED-mail, which may introduce bias towards certain types of outbreaks or regions. The annotation process is subjective and relies on human annotators, which can introduce potential biases and inconsistencies. The dataset predominantly focuses on English-language news articles, limiting its generalizability to other languages and regions.

## 💾 Data

**Source**: 1,508 samples from reported news articles, open emails, and alerts. Raw collection originated from ProMED-mail (initially collected 36,788 raw ProMED-mail alerts from December 2009 to December 2021); candidate selection and manual searches on ProMED, Wikipedia, and media news platforms were used to supplement sparse cases.

**Size**: 1,508 examples

**Format**: N/A

**Annotation**: Annotation performed by a professional annotation company using a LabelStudio interface. Question selection and sample filtering were done with Ph.D.-level experts in epidemiology and public health. Annotation pipeline includes ethics check, feasibility check, preliminary annotation, consistency checks, quality checks, expert feedback, and four annotation batches (40, 710, 110, 660 samples).

## 🔬 Methodology

**Methods**:
- Model-based evaluation (fine-tuning of T5, BART, GPT2, GPTNEO, OPT, Galactica, BLOOM)
- Zero-shot evaluation (ChatGPT)
- Automated metrics evaluation (Precision/Recall/F1, Accuracy / Exact Match Accuracy)

**Metrics**:
- Precision
- Recall
- F1 Score
- Accuracy
- Exact Match Accuracy

**Calculation**: For QA the paper uses exact match accuracy and normalizes occurrences of 'N/A', 'Unknown', 'na', and 'nan' to 'Cannot Infer' before evaluation. NER and EE are evaluated using Precision, Recall, and F1 over extracted entities/attributes.

**Interpretation**: The paper reports that supervised models (fine-tuned on BAND) outperform zero-shot ChatGPT for NER and QA. For QA, decoder-only models generally outperform encoder-decoder models; for EE, encoder-decoder models perform better than decoder-only models. Higher reported Accuracy / F1 indicates better model performance on the BAND tasks.

**Baseline Results**: NER (Random split) F1: CRFBased 0.625, TokenBased 0.660, SpanBased 0.642, ChatGPT 0.339. QA (Rand split) Accuracy: T5 0.674, Bart 0.666, GPT2 0.663, GPTNEO 0.695, OPT 0.699, Galactica 0.717, BLOOM 0.735, ChatGPT 0.497. EE Overall F1: T5 60.88, Bart 60.86, GPT2 45.34, OPT 48.27, GPTNEO 34.34, Galactica 49.33, BLOOM 48.40, ChatGPT 47.71.

**Validation**: Annotation validation included a consistency check where five annotators annotated the same 40 samples (results reported in Appendix Table 9), quality checks after each annotation batch with expert feedback, manual reviews, and an ethics review/approval by the faculty research ethics committee.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Privacy
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Privacy**: Personal information in data

**Demographic Analysis**: Victim distribution by host type: Human 69.4%, Animal 24.8%, Plant 5.8%. The paper also provides distributions for disease types, countries, provinces, cities, pathogens, symptoms, and year coverage.

**Potential Harm**: ['Detection of intentional release (intentful release) of pathogens', 'Identifying vulnerable populations (e.g., elderly, children, pregnant women)', 'Detection/prevention of privacy breaches (identification of personal information in texts)']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The project passed an ethics panel review; annotators performed ethics checks and samples violating ethical rules were removed. The paper states that all raw corpus used is sourced from publicly available internet data and that no private or sensitive information was utilized.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
