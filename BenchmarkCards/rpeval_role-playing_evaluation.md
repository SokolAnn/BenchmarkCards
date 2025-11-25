# RPEval (Role-Playing Evaluation)

## 📊 Benchmark Details

**Name**: RPEval (Role-Playing Evaluation)

**Overview**: RPEval is designed to assess LLM role-playing capabilities across four key dimensions: emotional understanding, decision-making, moral alignment, and in-character consistency.

**Data Type**: scenario-based responses

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/yelboudouri/RPEval)

## 🎯 Purpose and Intended Users

**Goal**: To provide a reproducible evaluation method for the role-playing capabilities of Large Language Models.

**Target Audience**:
- ML Researchers
- Educators

**Tasks**:
- Role-Playing Evaluation

**Limitations**: Focus on single-turn interactions limits assessment of nuanced, long-term role-playing attributes.

## 💾 Data

**Source**: Generated character profiles and scenarios using OpenAI’s GPT-4o.

**Size**: 9018 scenarios

**Format**: N/A

**Annotation**: Crowdsourced responses from participants using an online platform.

## 🔬 Methodology

**Methods**:
- Automated metrics
- Crowdsourced evaluation

**Metrics**:
- Binary scoring for performance across core dimensions

**Calculation**: Scores are given based on correctness of emotional recognition and alignment with the character's decisions.

**Interpretation**: Higher scores indicate better role-playing ability across specified dimensions.

**Baseline Results**: Average scores calculated for evaluated models include GPT-4o (44.41%), Gemini-1.5-Pro (62.24%), and Llama 3.2 1B (39.33%).

**Validation**: Multiple test runs for each model were conducted to assess performance stability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety

**Atlas Risks**:
- **Misuse**: Non-disclosure, Improper usage

**Demographic Analysis**: N/A

**Potential Harm**: Potential for misuse through manipulation of role-playing scenarios.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Anonymity measures implemented in crowdsourced responses.

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
