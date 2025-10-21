# RestBench

## 📊 Benchmark Details

**Name**: RestBench

**Overview**: To fully evaluate the performance of RestGPT, we propose RestBench, a high-quality benchmark which consists of two real-world scenarios and human-annotated instructions with gold solution paths.

**Data Type**: text (user instructions and gold API solution paths)

**Domains**:
- Natural Language Processing
- Web Services
- Entertainment

**Languages**:
- English

**Similar Benchmarks**:
- API-Bank
- Gorilla

**Resources**:
- [Resource](https://restgpt.github.io)
- [Resource](https://arxiv.org/abs/2306.06624)

## 🎯 Purpose and Intended Users

**Goal**: To assess the effectiveness of RestGPT in processing complex user instructions through RESTful APIs by providing a human-annotated benchmark comprising two realistic scenarios.

**Target Audience**:
- ML Researchers
- Industry Practitioners
- Model Developers

**Tasks**:
- Instruction Following
- API Call Planning
- API Response Parsing
- Tool / API Use

**Limitations**: Though the data scale is not large, these instructions are typical of frequently raised user requests.

## 💾 Data

**Source**: Two real-world scenarios: TMDB (movie database) and Spotify (music player). For these scenarios the authors filtered out 54 and 40 commonly used APIs respectively and obtained the corresponding OpenAPI Specifications; instructions and gold API solution paths were collected and annotated by experts.

**Size**: Test set: 100 instructions for TMDB and 57 instructions for Spotify; Development set: 10 instruction-solution pairs per scenario (20 total); Total test examples: 157; Total dev examples: 20.

**Format**: N/A

**Annotation**: Manual annotation by 6 experts who brainstormed instructions and annotated gold API solution paths; two additional experts verified solvability and correctness.

## 🔬 Methodology

**Methods**:
- Automated metrics (Correct Path Rate, Success Rate, ∆Solution Len.)
- Human evaluation (for Success Rate determination)

**Metrics**:
- Correct Path Rate
- Success Rate
- ∆Solution Len.
- Number of API calls

**Calculation**: Correct Path Rate: model-generated API call path is considered correct if it contains the gold API call path as a subsequence (elements not necessarily contiguous). Success Rate: determined by human evaluation of whether the model result successfully fulfills the user query. ∆Solution Len. = (1/Ns) * sum_{i=0..Ns-1} (Li_real - Li_gold) * I(i,success), where Ns is number of successfully accomplished instructions, Li_real and Li_gold are actual and gold number of API calls for the i-th instruction, and I(i,success) indicates successful completion.

**Interpretation**: A higher Correct Path Rate and higher Success Rate indicate better performance at planning and fulfilling instructions. A smaller ∆Solution Len. indicates better planning efficiency (fewer additional API calls required).

**Baseline Results**: Reported results (excerpt from Table 4): RestGPT (text-davinci-003): TMDB Success 75.0%, Correct Path 79.0%, ∆Solution Len. +0.55; Spotify Success 72.7%, Correct Path 74.5%, ∆Solution Len. +0.25. Baselines: Offline: TMDB Success 29.0%, CP 33.0%, ∆+1.52; DEPS: TMDB 38.0%/43.0%/+1.20; ReAct: TMDB 44.0%/57.0%/+0.76; Reflexion: TMDB 52.0%/59.0%/+1.37. Ablations: RestGPT w/o Planner: TMDB Success 44.0%, CP 57.0%; w/o Parser: TMDB Success 46.0%, CP 53.0%. Additional model variants and numbers are reported in Table 4 of the paper.

**Validation**: Annotation verification by two additional experts to ensure solvability and correctness of solution paths; human evaluation used to determine Success Rate; gold API solution paths used as ground truth for Correct Path Rate.

## ⚠️ Targeted Risks

**Risk Categories**:
- Robustness
- Accuracy

**Atlas Risks**:
- **Robustness**: Hallucination
- **Accuracy**: Poor model accuracy

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Not Applicable

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
