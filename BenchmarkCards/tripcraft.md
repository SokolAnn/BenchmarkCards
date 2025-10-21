# TripCraft

## 📊 Benchmark Details

**Name**: TripCraft

**Overview**: TripCraft is a spatio-temporally coherent travel planning dataset that integrates real-world constraints, including public transit schedules, event availability, diverse attraction categories, and user personas for enhanced personalization.

**Data Type**: travel planning queries

**Domains**:
- Natural Language Processing
- Travel

**Languages**:
- English

**Similar Benchmarks**:
- TravelPlanner
- TravelPlanner+

**Resources**:
- [Resource](https://arxiv.org/abs/2502.20508)

## 🎯 Purpose and Intended Users

**Goal**: To establish a new benchmark for LLM-driven personalized travel planning, offering a realistic, constraint-aware framework for itinerary generation.

**Target Audience**:
- ML Researchers
- Travel Industry Practitioners
- Model Developers

**Tasks**:
- Travel Planning
- Personalized Itinerary Generation

**Limitations**: N/A

## 💾 Data

**Source**: Constructed from real-world data sources through web scraping and open-source tools.

**Size**: 1000 travel queries

**Format**: Structured data in JSON format

**Annotation**: Annotated by 25 human annotators through multiple refinement rounds.

## 🔬 Methodology

**Methods**:
- Human annotation
- Automated metrics

**Metrics**:
- Temporal Meal Score
- Temporal Attraction Score
- Spatial Score
- Ordering Score
- Persona Score

**Calculation**: Metrics are calculated based on the alignment of itinerary details with user preferences and constraints.

**Interpretation**: Higher scores indicate better alignment with temporal, spatial, and persona consistency.

**Validation**: Validated through human annotation and expert review of the generated itineraries.

## ⚠️ Targeted Risks

**Risk Categories**:
- Bias
- Safety
- Accuracy

**Atlas Risks**:
- **Fairness**: Data bias
- **Accuracy**: Poor model accuracy

**Demographic Analysis**: N/A

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Fully anonymized sensitive personal details; aggregate demographic statistics provided with consent.

**Data Licensing**: Dataset and codebase will be made publicly available upon acceptance.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
