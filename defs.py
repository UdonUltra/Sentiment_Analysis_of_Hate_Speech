# Creating a TextProcessor object
import spacy
language_model = spacy.load('en_core_web_sm')

class TextProcessor:
    def __init__(self, model_name="en_core_web_sm"):
        self.language_model = spacy.load(model_name)

    def apply_ner(self, text):
        doc = self.language_model(text)
        entities = [ent.text for ent in doc.ents if ent.label_ in ['GPE', 'LOC']]
        return ' '.join(entities)

    def apply_pos(self, text):
        doc = self.language_model(text)
        pos_filtered = [token.text for token in doc if token.pos_ in ['NOUN', 'VERB']]
        return ' '.join(pos_filtered)
    
    def clean_text_from_entities(self, text):
        doc = self.language_model(text)
        entities = [ent.text for ent in doc.ents]

        # Menghapus entitas dari teks
        for entity in entities:
            text = text.replace(entity, '')
        return text.strip()

text_processor = TextProcessor()

def process_chunk(chunk):
    # Apply NER and clean_text_from_entities functions to each row in the chunk
    chunk['ner_text'] = chunk['Content'].apply(text_processor.apply_ner)
    chunk['text_without_entities'] = chunk['Content'].apply(text_processor.clean_text_from_entities)
    return chunk