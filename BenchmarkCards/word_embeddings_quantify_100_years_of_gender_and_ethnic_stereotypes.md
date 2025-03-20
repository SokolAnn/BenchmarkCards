<div align="center">

# Word Embeddings Quantify 100 Years of Gender and Ethnic Stereotypes

<small><em>Original: 1711.08412v1.json</em></small>

<hr style="height:2px;border-width:0;color:gray;background-color:#007acc">

<p>
<img src="https://img.shields.io/badge/NaturalLanguageProcessing-blue?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGwSURBVDhPjZLPSxtBFMe/s5tkE7PRqBhjQKwgFj3Ug5dignoTL/4FHrz1qIjHCl568NSLiojgwasn8SJYsAqCUigWTG1jiMuSsO6PzWTnvSTb1mLpCx8Y5vH9zHvzRpRKJTQaDZRKpfv1ev2JEOKBptr9eTJNs6jrert/OLg4Ho/L3W73QcgVnkqSMEHsXqlUSjLh3DeHItRqNfc7BcGMrusjTdOGqqpeidx7g4K3mUzmKB6P78fjA6lpWsXzvJu+/YdMp9PrDGo2m0u+70fZUCm93/DtJZRIJH6yofl8PsonPgtKbJpmK5PJnOXz+Us69hn1xWLxje/78W63u+H7wRmEvC1oNBoRx3FiZMhut7tZLBZf0fEzoVkEx0aj0RWaOBDVahU5jjOiHh1K7zgOnpJ5y7ZtYdu2X4BR13VFPp/3CoWCm0wm39JEe0JySGjJcZyNTqfjuK67atu2BhAWCoUZ6qs0cZdCJiL8IKlU6vP29naMfn/B3cxms7her49ITTqdVpPJ5Mna2trLcDj8ie6NGYTw1Ov1Iq7rhlhJ27YnmqYNQ6HQIBKJ/KJrf0n8D78BoVOBAJYE9eEAAAAASUVORK5CYII=" alt="Natural Language Processing" style="margin-right:5px;">
<img src="https://img.shields.io/badge/Sociology-blue?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGwSURBVDhPjZLPSxtBFMe/s5tkE7PRqBhjQKwgFj3Ug5dignoTL/4FHrz1qIjHCl568NSLiojgwasn8SJYsAqCUigWTG1jiMuSsO6PzWTnvSTb1mLpCx8Y5vH9zHvzRpRKJTQaDZRKpfv1ev2JEOKBptr9eTJNs6jrert/OLg4Ho/L3W73QcgVnkqSMEHsXqlUSjLh3DeHItRqNfc7BcGMrusjTdOGqqpeidx7g4K3mUzmKB6P78fjA6lpWsXzvJu+/YdMp9PrDGo2m0u+70fZUCm93/DtJZRIJH6yofl8PsonPgtKbJpmK5PJnOXz+Us69hn1xWLxje/78W63u+H7wRmEvC1oNBoRx3FiZMhut7tZLBZf0fEzoVkEx0aj0RWaOBDVahU5jjOiHh1K7zgOnpJ5y7ZtYdu2X4BR13VFPp/3CoWCm0wm39JEe0JySGjJcZyNTqfjuK67atu2BhAWCoUZ6qs0cZdCJiL8IKlU6vP29naMfn/B3cxms7her49ITTqdVpPJ5Mna2trLcDj8ie6NGYTw1Ov1Iq7rhlhJ27YnmqYNQ6HQIBKJ/KJrf0n8D78BoVOBAJYE9eEAAAAASUVORK5CYII=" alt="Sociology" style="margin-right:5px;">
<img src="https://img.shields.io/badge/MachineLearning-blue?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAGwSURBVDhPjZLPSxtBFMe/s5tkE7PRqBhjQKwgFj3Ug5dignoTL/4FHrz1qIjHCl568NSLiojgwasn8SJYsAqCUigWTG1jiMuSsO6PzWTnvSTb1mLpCx8Y5vH9zHvzRpRKJTQaDZRKpfv1ev2JEOKBptr9eTJNs6jrert/OLg4Ho/L3W73QcgVnkqSMEHsXqlUSjLh3DeHItRqNfc7BcGMrusjTdOGqqpeidx7g4K3mUzmKB6P78fjA6lpWsXzvJu+/YdMp9PrDGo2m0u+70fZUCm93/DtJZRIJH6yofl8PsonPgtKbJpmK5PJnOXz+Us69hn1xWLxje/78W63u+H7wRmEvC1oNBoRx3FiZMhut7tZLBZf0fEzoVkEx0aj0RWaOBDVahU5jjOiHh1K7zgOnpJ5y7ZtYdu2X4BR13VFPp/3CoWCm0wm39JEe0JySGjJcZyNTqfjuK67atu2BhAWCoUZ6qs0cZdCJiL8IKlU6vP29naMfn/B3cxms7her49ITTqdVpPJ5Mna2trLcDj8ie6NGYTw1Ov1Iq7rhlhJ27YnmqYNQ6HQIBKJ/KJrf0n8D78BoVOBAJYE9eEAAAAASUVORK5CYII=" alt="Machine Learning" style="margin-right:5px;">
</p>

</div>

## Table of Contents

- [📊 Benchmark Details](#-benchmark-details)
- [🎯 Purpose and Intended Users](#-purpose-and-intended-users)
- [💾 Data](#-data)
- [🔬 Methodology](#-methodology)
- [⚠️ Targeted Risks](#️-targeted-risks)
- [🔒 Ethical and Legal Considerations](#-ethical-and-legal-considerations)

<hr>

## 📊 Benchmark Details

<table>
<tr><td width="20%" align="center"><strong>Name</strong></td><td>
Word Embeddings Quantify 100 Years of Gender and Ethnic Stereotypes
</td></tr>
<tr><td width="20%" align="center"><strong>Overview</strong></td><td>
The paper develops a framework to demonstrate how the temporal dynamics of word embeddings can be leveraged to quantify changes in stereotypes and attitudes toward women and ethnic minorities in the U.S. over the 20th and 21st centuries.
</td></tr>
<tr><td width="20%" align="center"><strong>Data Type</strong></td><td>
Text data from historical documents and U.S. Census data
</td></tr>
<tr><td width="20%" align="center"><strong>Domains</strong></td><td>
<ul>
<li>Natural Language Processing</li>
<li>Sociology</li>
<li>Machine Learning</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Languages</strong></td><td>
<ul>
<li>English</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Similar Benchmarks</strong></td><td>
</td></tr>
<tr><td width="20%" align="center"><strong>Resources</strong></td><td>
<ul>
<li><a href="Dataset of word embeddings trained on historical texts">Resource</a></li>
<li><a href="U.S. Census data">Resource</a></li>
<li><a href="Code and embeddings available at https://github.com/nikhgarg/EmbeddingDynamicStereotypes">GitHub Repository</a></li>
</ul>
</td></tr>
</table>

## 🎯 Purpose and Intended Users

<table>
<tr><td width="20%" align="center"><strong>Goal</strong></td><td>
To quantify historical shifts in gender and ethnic stereotypes using word embeddings.
</td></tr>
<tr><td width="20%" align="center"><strong>Target Audience</strong></td><td>
<ul>
<li>Researchers in linguistics</li>
<li>Sociologists</li>
<li>Data scientists</li>
<li>Practitioners in NLP</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Tasks</strong></td><td>
<ul>
<li>Analyze changes in language and stereotypes over time</li>
<li>Validate findings against external data such as census</li>
<li>Develop methods for quantifying stereotypes</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Limitations</strong></td><td>
None
</td></tr>
<tr><td width="20%" align="center"><strong>Out of Scope Uses</strong></td><td>
</td></tr>
</table>

## 💾 Data

<table>
<tr><td width="20%" align="center"><strong>Source</strong></td><td>
Google News dataset, Google Books, and U.S. Census data
</td></tr>
<tr><td width="20%" align="center"><strong>Size</strong></td><td>
Datasets include 100 years of text data
</td></tr>
<tr><td width="20%" align="center"><strong>Format</strong></td><td>
Historical text corpora and vectors
</td></tr>
<tr><td width="20%" align="center"><strong>Annotation</strong></td><td>
Word vectors trained to represent words and their semantic relationships
</td></tr>
</table>

## 🔬 Methodology

<table>
<tr><td width="20%" align="center"><strong>Methods</strong></td><td>
<ul>
<li>Word embeddings</li>
<li>Statistical analysis</li>
<li>Regression</li>
<li>Temporal analysis</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Metrics</strong></td><td>
<ul>
<li>Relative norm distance</li>
<li>Cosine similarity</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Calculation</strong></td><td>
Calculating the relative strength of association between groups and neutral words.
</td></tr>
<tr><td width="20%" align="center"><strong>Interpretation</strong></td><td>
The changes in embeddings reflect social shifts and trends in demographics.
</td></tr>
<tr><td width="20%" align="center"><strong>Baseline Results</strong></td><td>
None
</td></tr>
<tr><td width="20%" align="center"><strong>Validation</strong></td><td>
Validated against historical census data and crowd-sourced stereotype scores
</td></tr>
</table>

## ⚠️ Targeted Risks

<table>
<tr><td width="20%" align="center"><strong>Risk Categories</strong></td><td>
<ul>
<li>Bias in word embeddings</li>
<li>Temporal changes in language representation</li>
</ul>
</td></tr>
<tr><td width="20%" align="center"><strong>Atlas Risks</strong></td><td>
No specific atlas risks defined
</td></tr>
<tr><td width="20%" align="center"><strong>Demographic Analysis</strong></td><td>
None
</td></tr>
<tr><td width="20%" align="center"><strong>Potential Harm</strong></td><td>
None
</td></tr>
</table>

## 🔒 Ethical and Legal Considerations

<table>
<tr><td width="20%" align="center"><strong>Privacy And Anonymity</strong></td><td>
Not Applicable
</td></tr>
<tr><td width="20%" align="center"><strong>Data Licensing</strong></td><td>
Data provided under appropriate usage rights consistent with the sources.
</td></tr>
<tr><td width="20%" align="center"><strong>Consent Procedures</strong></td><td>
Not Applicable
</td></tr>
<tr><td width="20%" align="center"><strong>Compliance With Regulations</strong></td><td>
Not Applicable
</td></tr>
</table>

<hr>

<div align="center">
<p><em>This benchmark card was automatically generated.</em></p>
</div>