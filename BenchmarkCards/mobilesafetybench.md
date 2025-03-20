# MobileSafetyBench

## 📊 Benchmark Details

**Name**: MobileSafetyBench

**Overview**: A benchmark designed to evaluate the safety of device-control agents within a realistic mobile environment based on Android emulators, focusing on safety in mobile device control tasks.

**Data Type**: Task-based evaluation

**Domains**:
- Mobile Applications
- Device Control
- Safety Assessment

**Resources**:
- [Resource](https://mobilesafetybench.github.io/)

## 🎯 Purpose and Intended Users

**Goal**: To evaluate the safety and helpfulness of autonomous agents controlling mobile devices.

**Target Audience**:
- Researchers
- Developers
- Practitioners in AI Safety

**Tasks**:
- Evaluate agent performance in mobile tasks
- Assess safety handling of sensitive information
- Measure robustness against injection attacks

**Limitations**: Evaluated agents may vary significantly in their safety performance, necessitating method improvements over time.

## 💾 Data

**Source**: MobileSafetyBench documentation

**Size**: 80 tasks

**Format**: Interactive scenario-based tasks

**Annotation**: Human-annotated risk levels and task performance metrics.

## 🔬 Methodology

**Methods**:
- Task simulation using Android emulators
- Risk type classification through human annotation
- Prompting methods for agent behavior

**Metrics**:
- Goal achievement rates
- Harm prevention rates
- Task completion success rates

**Calculation**: Calculated based on the number of successful task completions over total attempts, segregated by task risk levels.

**Interpretation**: Scores indicate the relative safety and performance of agents under various operational scenarios.

**Baseline Results**: Baseline models include GPT-4o, Gemini-1.5, and Claude-3.5, each evaluated on a suite of tasks with varying risk levels.

**Validation**: Empirical evaluation conducted across multiple scenarios.

## ⚠️ Targeted Risks

**Risk Categories**:
- Misuse risks
- Negative side effects from agent actions
- Vulnerability to indirect prompt injections

**Atlas Risks**:
- **Fairness**: Data bias
- **Robustness**: Prompt injection attack
- **Privacy**: Personal information in data
- **Misuse**: Improper usage, Spreading disinformation

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Emphasis on user consent and privacy considerations when accessing sensitive data in mobile tasks.

**Data Licensing**: Not Applicable

**Consent Procedures**: Agents are encouraged to request user consent for actions that may involve private information or could cause harm.

**Compliance With Regulations**: Task designs prioritize ethical compliance and legal standards in managing user data and preventing misuse.
