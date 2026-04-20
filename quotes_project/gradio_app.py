import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re
from database import SessionLocal
import models

def get_all_quotes_df():
    db = SessionLocal()
    try:
        quotes = db.query(models.Quote).all()
        data = [{
            "id": q.id,
            "text": q.text,
            "author": q.author,
            "category": q.category
        } for q in quotes]
        return pd.DataFrame(data)
    finally:
        db.close()

def show_quotes():
    df = get_all_quotes_df()
    if df.empty:
        return []
    return df[["id", "text", "author", "category"]].values.tolist()

def word_count_plot():
    df = get_all_quotes_df()
    if df.empty:
        fig = plt.figure()
        plt.text(0.5, 0.5, "Нет данных", ha="center", va="center")
        plt.axis("off")
        return fig

    text = " ".join(df["text"].tolist()).lower()
    words = re.findall(r"[a-zA-Z']+", text)

    stopwords = {
        "the", "and", "is", "a", "an", "of", "to", "in", "it", "that",
        "for", "on", "with", "as", "be", "at", "by", "this", "are", "was",
        "i", "me", "my", "we", "our", "you", "your",
        "he", "his", "him", "they", "them", "their"
    }

    words = [w for w in words if w not in stopwords and len(w) > 2]
    counter = Counter(words).most_common(10)

    labels = [x[0] for x in counter]
    values = [x[1] for x in counter]

    fig = plt.figure(figsize=(8, 4))
    plt.bar(labels, values)
    plt.xticks(rotation=45)
    plt.title("Top 10 Words in Quotes")
    plt.tight_layout()
    return fig

def build_gradio():
    with gr.Blocks() as demo:
        gr.Markdown("# Quotes Management and Analysis")

        btn_table = gr.Button("Показать все цитаты")
        table_output = gr.Dataframe(
            headers=["id", "text", "author", "category"],
            datatype=["number", "str", "str", "str"],
            interactive=False
        )

        btn_plot = gr.Button("Показать частоту слов")
        plot_output = gr.Plot()

        btn_table.click(fn=show_quotes, outputs=table_output)
        btn_plot.click(fn=word_count_plot, outputs=plot_output)

    return demo