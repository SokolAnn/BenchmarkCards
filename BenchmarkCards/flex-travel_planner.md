# FLEX-TRAVEL PLANNER

## 📊 Benchmark Details

**Name**: FLEX-TRAVEL PLANNER

**Overview**: Flex-TravelPlanner evaluates language models' ability to reason flexibly in dynamic planning scenarios, introducing two evaluation settings: sequential constraint introduction and scenarios with prioritized competing constraints.

**Data Type**: text

**Domains**:
- Natural Language Processing

**Languages**:
- English

**Similar Benchmarks**:
- TravelPlanner

**Resources**:
- [GitHub Repository](https://github.com/juhyunohh/FlexTravelBench)

## 🎯 Purpose and Intended Users

**Goal**: To assess the flexible reasoning abilities of language agents in dynamic, multi-turn planning scenarios.

**Target Audience**:
- ML Researchers
- Model Developers

**Tasks**:
- Planning

**Limitations**: N/A

## 💾 Data

**Source**: Flex-TravelPlanner dataset constructed from TravelPlanner data.

**Size**: N/A

**Format**: JSON

**Annotation**: N/A

## 🔬 Methodology

**Methods**:
- Automated metrics

**Metrics**:
- Constraint Pass Rate

**Calculation**: Constraint Pass Rate is calculated as the ratio of passed constraints to total constraints across all plans.

**Interpretation**: Higher Constraint Pass Rate indicates better planning performance under dynamic constraints.

**Baseline Results**: N/A

**Validation**: Evaluated models in zero-shot settings with structured references.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Fairness

**Atlas Risks**:
No specific atlas risks defined

**Demographic Analysis**: N/A

**Potential Harm**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
