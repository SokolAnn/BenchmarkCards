# MultiTerraPath Dataset

## 📊 Benchmark Details

**Name**: MultiTerraPath Dataset

**Overview**: MultiTerraPath is a synthetic dataset for evaluating model performance in cost-efficient path planning across multiple terrains, containing 1,000 maps sized 500×500, each with defined traversal costs and obstacles.

**Data Type**: maps

**Domains**:
- Robotics

**Languages**:
- English

**Resources**:
- [Resource](N/A)

## 🎯 Purpose and Intended Users

**Goal**: To provide a dataset for evaluating the performance of path planning algorithms in diverse terrain environments.

**Target Audience**:
- ML Researchers
- Robotics Practitioners

**Tasks**:
- Cost-efficient Path Planning
- Obstacle-avoidance Path Planning

**Limitations**: N/A

## 💾 Data

**Source**: Synthetic generation of maps and obstacle information as defined in the dataset description.

**Size**: 1,000 maps

**Format**: JSON

**Annotation**: Automatically generated for traversal costs and terrain descriptions.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Human evaluation

**Metrics**:
- Relative Precision (RP)
- Improvement Ratio (IR)

**Calculation**: Calculated as the ratio of improved paths to suggested paths and the proportion of valid paths incorporating LLM-Advisor.

**Interpretation**: Higher RP and IR indicate better path planning performance resulting from the LLM-Advisor.

**Baseline Results**: Improvement Ratio for A* and LLM-A* integration with LLM-Advisor achieved up to 82.50%.

**Validation**: Experimental results validated through comparative analysis with other existing path planning methods.

## ⚠️ Targeted Risks

**Risk Categories**:
- Accuracy
- Bias

**Atlas Risks**:
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
