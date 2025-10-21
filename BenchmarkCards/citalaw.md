# CitaLaw

## 📊 Benchmark Details

**Name**: CitaLaw

**Overview**: CitaLaw is the first benchmark designed to evaluate LLMs' ability to produce legally sound responses with appropriate citations. It features a diverse set of legal questions for both laypersons and practitioners, paired with a comprehensive corpus of law articles and precedent cases.

**Data Type**: question-answering pairs

**Domains**:
- Legal

**Languages**:
- Chinese

**Similar Benchmarks**:
- ALCE
- WebCiteS
- LawBench
- LAiW
- LexEval

**Resources**:
- [GitHub Repository](https://github.com/CSHaitao/LexiLaw)
- [GitHub Repository](https://github.com/FudanDISC/DISC-LawLLM)
- [GitHub Repository](https://github.com/irlab-sdu/fuzi.mingcha)
- [GitHub Repository](https://github.com/LiuHC0428/LAW-GPT)
- [GitHub Repository](https://github.com/siat-nlp/HanFei)
- [GitHub Repository](https://github.com/DUTIR-LegalIntelligence/Tailing)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the capability of LLMs to generate legally grounded responses with accurate and context-aware citations.

**Target Audience**:
- Legal Practitioners
- ML Researchers

**Tasks**:
- Legal Question Answering

**Limitations**: The benchmark is primarily sourced from the Chinese legal system, which may limit its applicability to other jurisdictions.

## 💾 Data

**Source**: Data includes approximately 50,000 law articles and multiple precedent cases collected from various legal databases.

**Size**: 500,000 documents

**Format**: JSON

**Annotation**: Manually annotated by legal experts.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- MAUVE
- ROUGE
- BERTScore
- Syllogism-based evaluation

**Calculation**: Metrics are calculated using a combination of established evaluation criteria for fluency, correctness, and citation quality.

**Interpretation**: Results are interpreted based on alignment of generated responses with expected logical structures in legal reasoning.

**Baseline Results**: Comparisons made against multiple LLMs including both open-domain and legal-specific models.

**Validation**: Validated through comparison with human judgments in legal context.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: The datasets used include publicly available documents, ensuring compliance with data privacy standards.

**Data Licensing**: Various licenses including Apache-2.0 and MIT for different components.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Ensured compliance with data privacy and legal standards.
