# WebGen-Bench

## 📊 Benchmark Details

**Name**: WebGen-Bench

**Overview**: WebGen-Bench is a novel benchmark designed to measure an LLM-based agent’s ability to create multi-file website codebases from scratch. It includes diverse instructions for website generation and corresponding test cases to evaluate the functionalities of the generated websites.

**Data Type**: website-generation instructions and test cases

**Domains**:
- Natural Language Processing
- Computer Vision

**Languages**:
- English

**Similar Benchmarks**:
- SWE-Bench
- SWE-Lancer

**Resources**:
- [GitHub Repository](https://github.com/mnluzimu/WebGen-Bench)

## 🎯 Purpose and Intended Users

**Goal**: To systematically evaluate LLM-based agents’ ability to construct websites from scratch based on natural language instructions.

**Target Audience**:
- ML Researchers
- Software Developers
- Web Developers

**Tasks**:
- Website Generation

**Limitations**: N/A

## 💾 Data

**Source**: Collected web development project descriptions from platforms like Upwork, Freelancer, and Proginn.

**Size**: 10,152 project descriptions, 6,667 website-generation instructions, 647 test cases

**Format**: N/A

**Annotation**: Created through the efforts of human annotators and GPT-4o.

## 🔬 Methodology

**Methods**:
- Automated testing using WebVoyager
- Human evaluation for accuracy checks

**Metrics**:
- Accuracy
- Appearance Score

**Calculation**: Accuracy was calculated using the formula Accuracy = (NYes + 0.5 × NPartial) / NTotal × 100%.

**Interpretation**: Higher accuracy indicates better website functionality as per generation instructions.

**Baseline Results**: Best accuracy achieved was 38.2% by WebGen-LM-32B.

**Validation**: Systematic validation of instruction and test case alignment through manual review.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
- **Accuracy**: Unrepresentative data, Poor model accuracy

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: MIT License

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
