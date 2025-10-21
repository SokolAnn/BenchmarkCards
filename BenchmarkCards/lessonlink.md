# LessonLink

## 📊 Benchmark Details

**Name**: LessonLink

**Overview**: LessonLink is the first dataset of real-world tutoring lessons, featuring 3,500 segments linked to 116 SAT math problems and spanning 24,300 minutes of instruction.

**Data Type**: text

**Domains**:
- Natural Language Processing
- Education

**Languages**:
- English

**Resources**:
- [GitHub Repository](https://github.com/rosewang2008/posr)

## 🎯 Purpose and Intended Users

**Goal**: To study conversation structure in educational contexts by linking tutoring conversations with reference materials.

**Target Audience**:
- ML Researchers
- Educators
- Curriculum Developers

**Tasks**:
- Segmentation
- Information Retrieval

**Limitations**: N/A

## 💾 Data

**Source**: Real-world tutoring transcripts from Schoolhouse.world linked to SAT math problem worksheets.

**Size**: 3,500 segments, 24,300 minutes of instruction

**Format**: JSON

**Annotation**: Annotated by 3 experts using a structured approach to ensure high-quality segments based on conversation structure.

## 🔬 Methodology

**Methods**:
- Human evaluation
- Automated metrics

**Metrics**:
- Accuracy
- Segmentation and Retrieval Score (SRS)
- WindowDiff
- Pk

**Calculation**: Metrics are calculated based on segment accuracy and retrieval performance, adapted with time-awareness.

**Interpretation**: Higher SRS or Accuracy indicates better segmentation and retrieval performance.

**Baseline Results**: POSR methods outperform independent segmentation and retrieval pipelines significantly.

**Validation**: Evaluation based on a large test set of 270 transcripts.

## ⚠️ Targeted Risks

**Risk Categories**:
- Privacy
- Fairness

**Atlas Risks**:
- **Privacy**: Personal information in data
- **Fairness**: Data bias

**Demographic Analysis**: N/A

**Potential Harm**: Explores the potential for improving educational practices but must ensure student data privacy.

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Data shared with de-identified transcripts to protect student privacy.

**Data Licensing**: CC Noncommercial 4.0 License.

**Consent Procedures**: Consent obtained from parents and students for research use of de-identified data.

**Compliance With Regulations**: Not Applicable
