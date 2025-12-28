import spacy
import random
from pathlib import Path

TRAIN_DATA = [
    ("Add 2 cups of rice", [(4, 5, "QUANTITY"), (6, 10, "UNIT"), (14, 18, "INGREDIENT")]),
    ("Use 1 tablespoon olive oil", [
        (4, 5, "QUANTITY"),
        (6, 16, "UNIT"),
        (17, 26, "INGREDIENT")
    ]),
    ("Chop 3 cloves garlic", [
        (5, 6, "QUANTITY"),
        (7, 13, "UNIT"),
        (14, 20, "INGREDIENT")
    ])
]

def train():
    nlp = spacy.blank("en")
    ner = nlp.add_pipe("ner")

    labels = ["INGREDIENT", "QUANTITY", "UNIT"]
    for label in labels:
        ner.add_label(label)

    optimizer = nlp.initialize()

    for epoch in range(20):
        random.shuffle(TRAIN_DATA)
        losses = {}

        for text, annotations in TRAIN_DATA:
            doc = nlp.make_doc(text)
            ents = []
            for start, end, label in annotations:
                span = doc.char_span(start, end, label=label)
                if span:
                    ents.append(span)
            doc.ents = ents

            example = spacy.training.Example.from_dict(
                doc,
                {"entities": annotations}
            )
            nlp.update([example], drop=0.3, losses=losses)

        print(f"Epoch {epoch+1} - Loss: {losses['ner']}")

    output_dir = Path("model/ingredient_ner")
    output_dir.mkdir(parents=True, exist_ok=True)
    nlp.to_disk(output_dir)

if __name__ == "__main__":
    train()
