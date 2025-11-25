# StorySeek

## 📊 Benchmark Details

**Name**: StorySeek

**Overview**: StorySeek is a semi-automatic dataset containing over 1,000 user stories with corresponding goals and project context, constructed to evaluate goal-driven requirements elicitation.

**Data Type**: user stories

**Domains**:
- Software Engineering

**Languages**:
- English

**Resources**:
- [Resource](https://huggingface.co/datasets/SoftACE/StorySeek)
- [GitHub Repository](https://github.com/SoftACE-Lab/goal2story)

## 🎯 Purpose and Intended Users

**Goal**: To support research and industry applications in requirements engineering, aiding in the identification and generation of user stories based on project goals.

**Target Audience**:
- ML Researchers
- Industry Practitioners

**Tasks**:
- Requirements Elicitation

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from real-world Agile projects hosted on GitLab, utilizing the NEODATASET collection.

**Size**: 1,005 records

**Format**: JSON

**Annotation**: Semi-automatic dataset construction with validation using LLMs.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Agent-based validation

**Metrics**:
- Factuality Hit Rate (FHR)
- Quality And Consistency Evaluation (QuACE)

**Calculation**: FHR measures the ratio of generated user stories that align with real project data, while QuACE evaluates the quality and goal alignment of the stories.

**Interpretation**: Higher FHR indicates better alignment with requirements, and higher QuACE scores signify better quality and relevance to goals.

**Baseline Results**: Comparative results showed Goal2Story outperforming Super-Agent using standard metrics.

**Validation**: Validation done through automated assessments and human evaluation.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Accuracy

**Atlas Risks**:
- **Privacy**: Data privacy rights alignment
- **Accuracy**: Unrepresentative data

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data is constructed from public GitLab projects ensuring participant anonymity.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
