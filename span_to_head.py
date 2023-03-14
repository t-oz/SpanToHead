# author: tyler osborne
# 03/14/2023

import spacy
def spanToHead(doc, span_start, span_end):

    # check Spacy documentation for different alignment mode options
    span = doc.char_span(span_start, span_end, alignment_mode='expand')

    # use token.i for token index, token.idx for character offset
    return span.root.idx, span.root.idx + len(span.root.text)
if __name__ == '__main__':

    # loading model -- use en_core_web_sm for faster performance; the large model is more accurate, however
    nlp = spacy.load("en_core_web_lg")

    text = "John said that Mary is coming to dinner."

    # span = "Mary is coming to dinner"
    span_start = 15
    span_end = len(text) - 1

    # parsing raw text to Spacy doc object
    doc = nlp(text)

    spacy_head_start, spacy_head_end = spanToHead(doc, span_start, span_end)

    print("Raw sentence: " + text)
    print("Span: " + text[span_start:span_end])
    print("Predicted head word: " + text[spacy_head_start:spacy_head_end])