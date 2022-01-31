from loguru import logger
from spacy_streamlit import visualize_ner
import spacy


def test(sent):

    try:
        nlp = spacy.load("saved_model")

        text = nlp(sent)
        vis = visualize_ner(text, labels=nlp.get_pipe("ner").labels)
        text_entities = [
            (entity, entity.ent_type_) for entity in text if entity.ent_type_
        ]

        entity_name_list = []
        entity_type_list = []

        for i in range(len(text_entities)):
            for j in range(0, 2):
                if j == 0:
                    entity_name_list.append(text_entities[i][j])
                else:
                    entity_type_list.append(text_entities[i][j])

        string_type = ""
        for entity_type in range(0, len(entity_type_list)):
            st = str(entity_type_list[entity_type])
            string_type = string_type + "/ " + st

        string_name = ""
        for entity_name in range(0, len(entity_name_list)):
            s = str(entity_name_list[entity_name])
            string_name = string_name + "/ " + s

        return string_name, string_type

    except Exception as e:

        logger.exception(e)
        return None
