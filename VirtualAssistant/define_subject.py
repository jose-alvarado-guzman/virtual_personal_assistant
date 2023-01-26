import re
import wikipedia

def get_definition(subject : str) -> str:
    regex = r"(can you)?\s*(please)?\s*(define|tell me)\s*(what|who)?\s*(is)?\s*|\?"
    clean_subject = re.sub(regex,"",subject.lower())
    print(clean_subject)
    try:
        wiki_response = wikipedia.summary(clean_subject, sentences=3)
        response = re.sub(r"\([^)]*\)|'","",wiki_response)
        response = re.sub(r"\s+"," ", response)
    except wikipedia.exceptions.DisambiguationError:
        response = "This concept is ambuigous, please be more specific"
    except wikipedia.exceptions.PageError:
        response = "Sorry, I currently do not know the answer to this."
    return response

if __name__ == "__main__":
    print(get_definition("can you define artificial intelligence (AI)?"))
