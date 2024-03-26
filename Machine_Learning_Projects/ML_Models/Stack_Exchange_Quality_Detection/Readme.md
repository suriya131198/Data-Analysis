# Stack Exchange Question Quality Detection
- we have an xml file names posts which taken from stack overflow
- we have to parse it and convert it and then need to build a classification model to classify the question quality

### Quality is determined by,
- Good-Quality questions: Questions for which score is greater than 5 and answer count is greater than 0 should be labelled as good quality questions.<br>
- Low-Quality questions: Questions for which the score is between 0 to 5 and having no answers should be labelled as low-quality questions.
- Very-low quality questions: Questions which have negative scores