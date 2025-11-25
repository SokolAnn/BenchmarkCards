# METAKP (On-Demand Keyphrase Generation)

## 📊 Benchmark Details

**Name**: METAKP (On-Demand Keyphrase Generation)

**Overview**: METAKP is a large-scale benchmark comprising four datasets, 7500 documents, and 3760 goals across news and biomedical domains with human-annotated keyphrases, aimed at evaluating on-demand keyphrase generation which is conditioned on specific high-level goals or intents.

**Data Type**: keyphrase-document pairs

**Domains**:
- Natural Language Processing
- Biomedical

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/uclanlp/MetaKP)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of METAKP is to provide a benchmark for evaluating models designed for on-demand keyphrase generation, assessing their ability to generate keyphrases that conform to specific user-defined goals.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- On-Demand Keyphrase Generation
- Goal Relevance Assessment

**Limitations**: N/A

## 💾 Data

**Source**: The datasets are curated from existing keyphrase prediction datasets including KPTimes, DUC2001, KPBiomed, and PubMed.

**Size**: 7500 documents

**Format**: JSON

**Annotation**: Human-annotated keyphrases and goals, with a labeling pipeline that combines GPT-4 and human annotators.

## 🔬 Methodology

**Methods**:
- Supervised fine-tuning
- Unsupervised self-consistency prompting

**Metrics**:
- Satisfaction Rate
- SemF1
- Abstain F1

**Calculation**: Metrics are calculated based on the model's generated keyphrases in relation to human-annotated references for goal-conformance.

**Interpretation**: Higher scores indicate better performance in generating relevant keyphrases according to specified goals.

**Baseline Results**: Results show the best performance of Flan-T5-XL with 0.609 SemF1, and GPT-4o with 0.548 SemF1 under the self-consistency prompting.

**Validation**: Evaluated with both in-distribution and out-of-distribution test sets.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy
- Safety

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Unrepresentative data
- **Societal Impact**: Impact on affected communities

**Demographic Analysis**: N/A

**Potential Harm**: The framework may inadvertently generate misleading keyphrases that conform to incorrect goals, leading to misinformation.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: The datasets used are either in the public domain or come with licenses; however, specific licensing information for some datasets is not specified.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
