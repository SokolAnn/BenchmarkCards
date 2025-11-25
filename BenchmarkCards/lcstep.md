# LCStep

## 📊 Benchmark Details

**Name**: LCStep

**Overview**: LCStep is a novel procedural knowledge dataset created from LangChain tutorials, designed to test systems’ domain adaptation ability in procedural question answering tasks.

**Data Type**: procedural knowledge steps

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- RecipeNLG
- CHAMP

**Resources**:
- [Resource](https://arxiv.org/abs/2409.01344)

## 🎯 Purpose and Intended Users

**Goal**: To test systems' ability to perform procedural question answering using new procedural knowledge.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Procedural Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Collected from 180 tutorial pages of the LangChain website.

**Size**: 276 procedures

**Format**: N/A

**Annotation**: LLM-enabled pipeline with human oversight and quality review.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- F1 Score
- BLEU Score
- Pairwise evaluation

**Calculation**: Metrics calculated based on evaluations comparing the AAG system against baseline methods.

**Interpretation**: A higher score indicates better performance in producing coherent and plausible procedural steps.

**Baseline Results**: AAG outperforms baselines including Zero-Shot, Few-Shot, RAG, and ReAct.

**Validation**: The system's performance was validated through ablation studies on its various components.

## ⚠️ Targeted Risks

**Risk Categories**:
- Fairness
- Accuracy

**Atlas Risks**:
- **Fairness**: Output bias
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: ['Misinformation in procedural outputs']

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
