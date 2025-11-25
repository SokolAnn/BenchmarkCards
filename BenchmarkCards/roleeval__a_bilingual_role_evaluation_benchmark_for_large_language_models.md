# RoleEval: A Bilingual Role Evaluation Benchmark for Large Language Models

## 📊 Benchmark Details

**Name**: RoleEval: A Bilingual Role Evaluation Benchmark for Large Language Models

**Overview**: RoleEval is a bilingual benchmark designed to assess the memorization, utilization, and reasoning capabilities of role knowledge, comprised of RoleEval-Global and RoleEval-Chinese, with 6,000 Chinese-English parallel multiple-choice questions focusing on 300 influential people and fictional characters.

**Data Type**: multiple-choice questions

**Domains**:
- Natural Language Processing

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- PersonaChat
- Personal-Dialog
- RoleBench

**Resources**:
- [GitHub Repository](https://github.com/Magnetic2014/RoleEval)

## 🎯 Purpose and Intended Users

**Goal**: To systematically examine the ability of large language models in capturing, understanding, and reasoning over role knowledge, which is crucial for role-playing applications.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Knowledge Assessment
- Reasoning Assessment

**Limitations**: The benchmark may become outdated due to the dynamic nature of real-world knowledge about characters.

## 💾 Data

**Source**: Questions were manually created and verified based on encyclopedia sources such as Wikipedia and Baidu Baike.

**Size**: 6,000 questions

**Format**: JSON

**Annotation**: Manual annotation with hybrid quality checks combining automatic and human verification.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy

**Calculation**: Metrics calculated based on the correct answers provided by the models in response to the multiple-choice questions.

**Interpretation**: Higher accuracy indicates better performance in capturing and reasoning over role knowledge.

**Baseline Results**: The performance of various models, especially comparisons between GPT-4 and Chinese LLMs, was evaluated across questions.

**Validation**: The benchmark was validated through extensive evaluations under zero- and few-shot settings.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Accuracy

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: The benchmark includes a diverse set of characters drawn from various cultural contexts.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: All materials used were sourced from public domain and verified encyclopedias, ensuring no privacy infringement.

**Data Licensing**: All data is gathered from public sources, aimed at non-commercial use adhering to copyright regulations.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
