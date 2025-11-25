# SentiPers: A Sentiment Analysis Corpus for Persian

## 📊 Benchmark Details

**Name**: SentiPers: A Sentiment Analysis Corpus for Persian

**Overview**: We outline the entire process of developing an annotated sentiment corpus, SentiPers, which covers formal and informal written contemporary Persian. The corpus contains more than 26,000 sentences and benefits from special characteristics such as quantifying the positiveness or negativity of an opinion through assigning a number within a specific range to any given sentence. SentiPers consists of annotation at document-level, sentence-level, and entity/aspect level.

**Data Type**: text (annotated sentences with opinion and target tags; aspect-level annotations; XML documents)

**Domains**:
- Natural Language Processing

**Languages**:
- Persian

**Similar Benchmarks**:
- Hu and Liu dataset
- MPQA
- Cornell movie review dataset
- JDPA sentiment corpus
- Twitter sentiment corpus (Pak and Paroubek)
- Amazon product reviews dataset (Blitzer et al.)
- OCA (Opinion Corpus for Arabic)
- AWATIF
- ChnSenti-Corp
- MLSA
- NTCIR multilingual opinion analysis
- USAGE
- BS Data
- hellokish dataset

**Resources**:
- [GitHub Repository](https://github.com/phosseini/sentipers)
- [Resource](https://www.digikala.com/)

## 🎯 Purpose and Intended Users

**Goal**: Developing an annotated sentiment corpus, SentiPers, covering formal and informal contemporary Persian; providing a rich resource annotated at document-, sentence-, and aspect-level and quantifying sentiment intensity with a five-point polarity range.

**Target Audience**:
- Researchers interested in Persian and in the area of sentiment analysis

**Tasks**:
- Sentiment Analysis
- Aspect-based Sentiment Analysis
- Document-level Sentiment Classification
- Sentence-level Sentiment Classification
- Aspect/Entity Extraction (target and opinion word annotation)

**Limitations**: Annotation challenges include subjective nature of annotation, ambiguous opinion holders, antithetical opinions within sentences, and difficulty selecting correct reference targets; inter-annotator agreement varies by task.

## 💾 Data

**Source**: Reviews crawled from Digikala (Persian online shopping website).

**Size**: 26,767 sentences; 270 XML documents; 515,387 tokens; 17,635 unique words; 26,996 opinion words; 21,375 target words.

**Format**: XML (HTML pages converted to XML files; sentences have unique IDs within XML structure).

**Annotation**: Manual annotation by four annotators (Persian native speakers) trained with an annotation guideline; an experienced annotator reviewed all annotated documents. Annotations at document-, sentence-, and aspect-level; tags include Target, Opinion, and Keyword; sentence and document polarity values drawn from the set {-2, -1, 0, +1, +2}.

## 🔬 Methodology

**Methods**:
- Manual annotation (human annotators following annotation guideline)
- Annotation software with XPath-based HTML-to-XML extraction and annotation editor
- Inter-annotator agreement measurement (Fleiss's kappa for polarity assignment)
- Agreement for tagged anchors measured using anchor overlap method (Wiebe et al. 2005)

**Metrics**:
- Inter-Annotator Agreement (Fleiss's kappa for polarity assignment; reported as Task Agreement %)
- Agreement for tags measured by anchor overlap proportion
- Corpus statistics (sentence count, token count, unique words, counts of opinion and target words)

**Calculation**: For polarity assignment, Fleiss's kappa measure was used with three categories: positive, neutral, negative. For tag agreement, the anchor overlap method from Wiebe et al. (2005) was used: agr(A|B) = |A_matching_B| / |A|. Corpus statistics (counts) computed by the annotation software.

**Interpretation**: Inter-annotator agreement should be interpreted relative to the difficulty of the annotation task. Reported agreement (Task Agreement %) values are provided per task (polarity assignment and tag annotation).

**Validation**: Annotators were trained on guidelines and sample documents; an experienced annotator reviewed annotations; inter-annotator agreement was computed (Fleiss's kappa for polarity assignment and anchor-overlap for tags) to assess annotation reliability.

## ⚠️ Targeted Risks

**Risk Categories**:
- Data Laws

**Atlas Risks**:
- **Data Laws**: Data usage restrictions

## 🔒 Ethical and Legal Considerations

**Privacy And Anonymity**: Not Applicable

**Data Licensing**: Corpus is publicly available for research and non-commercial activities; Digikala terms and conditions state site information is allowed to be used for non-commercial activities with referring to Digikala.

**Consent Procedures**: Not Applicable

**Compliance With Regulations**: Not Applicable
