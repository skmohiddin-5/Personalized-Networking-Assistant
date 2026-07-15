import wikipedia


def get_fact(topic):
    try:
        summary = wikipedia.summary(topic, sentences=2)
        return summary
    except Exception:
        return "No reliable information found on Wikipedia."