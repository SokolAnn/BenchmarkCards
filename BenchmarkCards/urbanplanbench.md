# UrbanPlanBench

## 📊 Benchmark Details

**Name**: UrbanPlanBench

**Overview**: UrbanPlanBench is a comprehensive benchmark designed to evaluate the efficacy of Large Language Models (LLMs) in urban planning. It measures performance across fundamental principles, professional knowledge, and management and regulations aligned with the qualifications expected of human planners.

**Data Type**: multiple-choice questions

**Domains**:
- Urban Planning

**Languages**:
- Chinese
- English

**Similar Benchmarks**:
- SuperGLUE
- BIG-Bench

**Resources**:
- [GitHub Repository](https://github.com/tsinghua-fib-lab/PlanBench)

## 🎯 Purpose and Intended Users

**Goal**: The primary objective of UrbanPlanBench is to assess the capabilities of LLMs in urban planning and catalyze their integration into practical workflows by providing a standardized evaluation framework.

**Target Audience**:
- ML Researchers
- Urban Planners
- AI Practitioners

**Tasks**:
- Question Answering

**Limitations**: N/A

## 💾 Data

**Source**: Generated from urban planning textbooks and past urban planning exams.

**Size**: 30,000 instruction pairs

**Format**: CSV

**Annotation**: Manually curated and transformed into structured multiple-choice format.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Accuracy

**Calculation**: Metrics are calculated based on the proportion of correctly answered questions in UrbanPlanBench.

**Interpretation**: Higher accuracy indicates better performance in understanding urban planning concepts.

**Baseline Results**: Current LLMs generally perform below the certification bar of professional urban planners.

**Validation**: System-level validation against the urban planner qualification examination standards.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy

**Atlas Risks**:
- **Accuracy**: Poor model accuracy, Unrepresentative data

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
