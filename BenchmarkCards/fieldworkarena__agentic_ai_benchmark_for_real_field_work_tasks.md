# FieldWorkArena: Agentic AI Benchmark for Real Field Work Tasks

## 📊 Benchmark Details

**Name**: FieldWorkArena: Agentic AI Benchmark for Real Field Work Tasks

**Overview**: This paper proposes FieldWorkArena, a benchmark for agentic AI targeting real-world field work, specifically to evaluate agents in monitoring and reporting safety and health incidents in real world work environments.

**Data Type**: multimodal

**Domains**:
- Manufacturing
- Logistics

**Languages**:
- English

**Similar Benchmarks**:
- WebArena
- VisualWebArena
- WorkArena++

**Resources**:
- [Resource](https://en-documents.research.global.fujitsu.com/fieldworkarena/)

## 🎯 Purpose and Intended Users

**Goal**: To provide a benchmark suite aimed at promoting the introduction of agentic AI in performing monitoring tasks in real-world field work environments.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Planning
- Perception
- Action

**Limitations**: N/A

## 💾 Data

**Source**: Data obtained from actual work sites including videos from factories and warehouses, work manuals, and related safety regulations.

**Size**: 400 queries, 61 evaluation videos, 31 evaluation images

**Format**: N/A

**Annotation**: Manually annotated ground truth data validated by multiple workers.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Accuracy is calculated based on the ratio of correct tasks to total tasks.

**Interpretation**: Higher accuracy indicates better performance of the agentic AI in real-world tasks.

**Validation**: Tasks validated against ground truths generated through interviews with workers.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness
- Transparency

**Atlas Risks**:
- **Accuracy**: Unrepresentative data
- **Fairness**: Data bias
- **Transparency**: Lack of training data transparency

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Consent was obtained from all workers appearing in the footage, and necessary face blurring was performed.

**Data Licensing**: Data is licensed under a special-purpose license that does not allow commercial use.

**Consent Procedures**: All video data collected with consent from individuals.

**Compliance With Regulations**: Not Applicable
